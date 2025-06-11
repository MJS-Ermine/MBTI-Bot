import gradio as gr
import requests
import base64
from PIL import Image
import io

API_BASE = "https://zwsmvt-8000.csb.app"
MBTI_LIST = [
    "INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"
]

def recommend(mbti: str) -> str:
    resp = requests.post(f"{API_BASE}/api/recommend", json={"mbti": mbti})
    if resp.ok:
        return f"推薦伴侶 MBTI: {', '.join(resp.json())}"
    return f"錯誤: {resp.text}"

def chat(mbti: str, message: str) -> str:
    resp = requests.post(f"{API_BASE}/api/chat", json={"mbti": mbti, "message": message})
    if resp.ok:
        return resp.json().get("reply", "無回應")
    return f"錯誤: {resp.text}"

def avatar(mbti: str):
    resp = requests.post(f"{API_BASE}/api/avatar", json={"mbti": mbti})
    if resp.ok:
        img_b64 = resp.json().get("avatar_base64", "")
        if img_b64:
            try:
                img_bytes = base64.b64decode(img_b64)
                img = Image.open(io.BytesIO(img_bytes))
                return img
            except Exception as e:
                print("圖片解碼失敗：", e)
                return None
    return None

def main():
    with gr.Blocks() as demo:
        gr.Markdown("# MBTI 伴侶聊天機器人 Demo")
        mbti = gr.Dropdown(choices=MBTI_LIST, label="你的MBTI")
        msg = gr.Textbox(label="你想說的話")
        recommend_out = gr.Textbox(label="推薦結果")
        chat_out = gr.Textbox(label="AI回覆")
        avatar_out = gr.Image(label="AI頭像", type="pil")
        with gr.Row():
            gr.Button("推薦伴侶MBTI").click(fn=recommend, inputs=mbti, outputs=recommend_out)
            gr.Button("聊天").click(fn=chat, inputs=[mbti, msg], outputs=chat_out)
            gr.Button("生成頭像").click(fn=avatar, inputs=mbti, outputs=avatar_out)
    demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main() 