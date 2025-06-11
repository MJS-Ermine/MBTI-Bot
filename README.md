# 未來伴侶聊天機器人（MBTI Bot）

## 專案結構

```
/
├── frontend/           # React (Vite) 前端
│   ├── public/
│   │   └── avatars/    # 16 張 MBTI 預設圖（請放在這裡）
│   └── src/
├── backend/            # FastAPI 後端
│   ├── main.py         # FastAPI 主程式
│   └── requirements.txt
└── README.md           # 專案說明
```

## 在 CodeSandbox 運行

1. 開啟 CodeSandbox，選擇 "Node + Python" 或 "Container" 模板。
2. 將本專案上傳或 clone。
3. 進入 `backend/`，安裝依賴：
   ```bash
   pip install -r requirements.txt
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
4. 進入 `frontend/`，安裝依賴並啟動：
   ```bash
   npm install
   npm run dev
   ```
5. 前端會自動 proxy `/api` 請求到 FastAPI。

## Avatar 圖片（AI 動漫風格自動生成）
- 系統會自動根據 MBTI 產生動漫風格頭像，並快取每個 MBTI 對應圖片。
- 無需手動上傳圖片。

## 聊天功能（HuggingFace 免費 API）
- 請註冊 [HuggingFace](https://huggingface.co/) 並取得免費 API Token。
- 編輯 `backend/main.py`，將 `hf_xxx` 替換為你的 Token。
- 預設使用 `facebook/blenderbot-400M-distill` 模型，可根據需求更換。

## HuggingFace API Token 取得與填寫
1. 前往 [HuggingFace 官網](https://huggingface.co/) 註冊/登入帳號。
2. 點右上角頭像 →「Settings」→「Access Tokens」。
3. 點「New token」，名稱自訂，Role 選「Read」。
4. 產生後複製 token（格式如 `hf_xxxxxxxxxxxxxxxxxxxxx`）。
5. 編輯 `backend/main.py`，將所有 `hf_xxx` 替換為你的 Token，例如：
   ```python
   headers = {"Authorization": "Bearer hf_abcdefgh1234567890"}
   ```
6. 若遇到 token 失效、API 無回應，請重新產生 token 並確認帳號未被限制。

## 注意事項
- CodeSandbox 有容量與運算限制，請壓縮圖片並避免放置大型檔案。
- 若需本地 LLM（如 Ollama），請改於本地或雲端 VM 部署。

---

如有問題，請聯絡專案負責人。
