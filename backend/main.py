from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import requests
import base64
import threading
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MBTI_MATCH = {
    "INTJ": ["ENFP", "INTP", "ENFJ"],
    # ... 其餘 MBTI 配對 ...
}

MBTI_AVATAR_PROMPT = "anime style portrait, {mbti} personality, vibrant colors, upper body, detailed, trending on pixiv, masterpiece"

class MBTIRequest(BaseModel):
    mbti: str

class ChatRequest(BaseModel):
    mbti: str
    message: str

class AvatarRequest(BaseModel):
    mbti: str

# 快取每個 MBTI 對應的 base64 圖片
avatar_cache: Dict[str, str] = {}
cache_lock = threading.Lock()

@app.post("/api/recommend", response_model=List[str])
def recommend_mbti(req: MBTIRequest) -> List[str]:
    """根據 MBTI 推薦伴侶 MBTI"""
    return MBTI_MATCH.get(req.mbti.upper(), [])

@app.post("/api/chat")
def chat_with_ai(req: ChatRequest):
    """串接 OpenRouter.ai 免費 LLM API 進行聊天"""
    prompt = f"你是一個{req.mbti}型人格的虛擬伴侶，請用該人格風格回應：{req.message}"
    OR_API_URL = "https://openrouter.ai/api/v1/chat/completions"
    OR_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
    headers = {"Authorization": f"Bearer {OR_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "openrouter/llama-2-13b-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        resp = requests.post(OR_API_URL, headers=headers, json=payload, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        reply = data.get("choices", [{}])[0].get("message", {}).get("content", "抱歉，目前無法回應。")
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/avatar")
def generate_avatar(req: AvatarRequest):
    """根據 MBTI 產生動漫風格 avatar，並快取 base64 結果 (Stable Horde)"""
    mbti = req.mbti.upper()
    with cache_lock:
        if mbti in avatar_cache:
            return {"mbti": mbti, "avatar_base64": avatar_cache[mbti]}
    prompt = MBTI_AVATAR_PROMPT.format(mbti=mbti)
    SH_API_URL = "https://stablehorde.net/api/v2/generate/async"
    headers = {"apikey": "0000000000", "Content-Type": "application/json"}  # 公開測試 key
    payload = {
        "prompt": prompt,
        "params": {"n": 1, "width": 512, "height": 512}
    }
    try:
        resp = requests.post(SH_API_URL, json=payload, headers=headers, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        # Stable Horde 回傳 job id，需再 poll 結果
        job_id = data.get("id")
        if not job_id:
            raise HTTPException(status_code=500, detail="Stable Horde 未回傳任務 ID")
        # Poll 結果
        poll_url = f"https://stablehorde.net/api/v2/generate/status/{job_id}"
        for _ in range(30):  # 最多等 30 次
            poll_resp = requests.get(poll_url, headers=headers, timeout=10)
            poll_data = poll_resp.json()
            if poll_data.get("done") and poll_data.get("generations"):
                img_b64 = poll_data["generations"][0]["img"]
                with cache_lock:
                    avatar_cache[mbti] = img_b64
                return {"mbti": mbti, "avatar_base64": img_b64}
            import time; time.sleep(2)
        raise HTTPException(status_code=500, detail="Stable Horde 生成逾時")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 