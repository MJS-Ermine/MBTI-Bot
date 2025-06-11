from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import requests
import base64
import threading

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
    """串接 HuggingFace 免費 LLM API 進行聊天"""
    prompt = f"你是一個{req.mbti}型人格的虛擬伴侶，請用該人格風格回應：{req.message}"
    HF_API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
    headers = {"Authorization": "Bearer hf_xxx"}  # 請填入你的 HuggingFace Token
    payload = {"inputs": prompt}
    try:
        resp = requests.post(HF_API_URL, headers=headers, json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return {"reply": data.get("generated_text", "抱歉，目前無法回應。")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/avatar")
def generate_avatar(req: AvatarRequest):
    """根據 MBTI 產生動漫風格 avatar，並快取 base64 結果"""
    mbti = req.mbti.upper()
    with cache_lock:
        if mbti in avatar_cache:
            return {"mbti": mbti, "avatar_base64": avatar_cache[mbti]}
    prompt = MBTI_AVATAR_PROMPT.format(mbti=mbti)
    HF_IMG_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
    headers = {"Authorization": "Bearer hf_xxx"}  # 請填入你的 HuggingFace Token
    payload = {"inputs": prompt}
    try:
        resp = requests.post(HF_IMG_API_URL, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        if resp.headers.get("content-type", "").startswith("image"):
            img_bytes = resp.content
            img_b64 = base64.b64encode(img_bytes).decode("utf-8")
            with cache_lock:
                avatar_cache[mbti] = img_b64
            return {"mbti": mbti, "avatar_base64": img_b64}
        else:
            raise HTTPException(status_code=500, detail="圖片生成失敗: " + resp.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 