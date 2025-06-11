# MBTI 伴侶聊天機器人

## 專案簡介

本專案為一個雲端可展示的 AI 聊天/圖片生成後端，支援：
- MBTI 伴侶推薦
- OpenRouter.ai 聊天（LLM）
- Stable Horde 免費動漫頭像生成
- Gradio 前端互動展示（無需 JS/React）

## 1. 安裝依賴

```bash
pip install -r requirements.txt
```

## 2. 設定環境變數

請先至 [OpenRouter.ai](https://openrouter.ai/) 申請 API Key。

- 在本地：
  ```bash
  export OPENROUTER_API_KEY=你的token
  # 或於 .env 檔加入 OPENROUTER_API_KEY=你的token
  ```
- 在 CodeSandbox/Replit：
  於「環境變數」介面新增 `OPENROUTER_API_KEY`，值為你的 token，並重啟伺服器。

Stable Horde 圖片生成已內建公開測試 key，無需註冊。

## 3. 啟動 FastAPI 後端

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

- API 文件（Swagger UI）：
  - 本地： http://localhost:8000/docs
  - 雲端： https://<你的-sandbox-id>-8000.csb.app/docs

## 4. 啟動 Gradio 前端互動 Demo

```bash
python gradio_app.py
```
- CodeSandbox 會自動顯示 7860 埠口公開網址，所有人可用瀏覽器互動。

## 5. API 測試

- `/api/recommend`：推薦伴侶 MBTI
- `/api/chat`：MBTI 風格聊天
- `/api/avatar`：動漫頭像生成

可用 Swagger UI、curl、Postman 或 Gradio 前端測試。

## 6. 常見問題

- 404 Not Found：請確認訪問 `/docs` 或正確 API 路徑
- 401/403：請檢查 `OPENROUTER_API_KEY` 是否正確
- 500：請檢查 token 權限、API 配置，或貼上錯誤訊息協助排查

## 7. 推送到 GitHub

```bash
git add requirements.txt gradio_app.py README.md
# 如有其他異動一併加入
git commit -m "feat: 新增 Gradio 前端與自動化說明，完善 requirements"
git push
```

---

如需自動化測試腳本、API 範例、或遇到其他問題，請參考本 README 或聯絡專案協作者。
