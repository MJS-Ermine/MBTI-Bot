import gradio as gr
import requests

API_BASE = "https://zwsmvt-8000.csb.app"

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
            return f"data:image/png;base64,{img_b64}"
    return None

def main():
    with gr.Blocks() as demo:
        gr.Markdown("# MBTI 伴侶聊天機器人 Demo")
        mbti = gr.Textbox(label="你的MBTI (如 INTJ)")
        msg = gr.Textbox(label="你想說的話")
        with gr.Row():
            gr.Button("推薦伴侶MBTI").click(fn=recommend, inputs=mbti, outputs="text")
            gr.Button("聊天").click(fn=chat, inputs=[mbti, msg], outputs="text")
            gr.Button("生成頭像").click(fn=avatar, inputs=mbti, outputs="image")
    demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main() 