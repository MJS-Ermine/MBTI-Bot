import requests

API_BASE = "https://zwsnvt-8000.csb.app"  # 請依你的實際 CodeSandbox 域名調整

def test_avatar():
    url = f"{API_BASE}/api/avatar"
    data = {"mbti": "INTJ"}
    resp = requests.post(url, json=data)
    print("Avatar API 回應：", resp.status_code, resp.json())

def test_chat():
    url = f"{API_BASE}/api/chat"
    data = {"mbti": "INTJ", "message": "Hello!"}
    resp = requests.post(url, json=data)
    print("Chat API 回應：", resp.status_code, resp.json())

if __name__ == "__main__":
    test_avatar()
    test_chat() 