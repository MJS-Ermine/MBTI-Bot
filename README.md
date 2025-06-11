# MBTI 伴侶聊天機器人

## 專案簡介

本專案為一個雲端可展示的 AI 聊天/圖片生成後端，支援：
- MBTI 伴侶推薦
- OpenRouter.ai 聊天（LLM）
- Stable Horde 免費動漫頭像生成
- Gradio 前端互動展示（無需 JS/React）

---

## 1. 安裝依賴

```bash
pip install -r requirements.txt
```

---

## 2. 每位組員必須自行註冊 OpenRouter.ai 並設定自己的 token

> **安全提醒：本專案 repo 內不會有任何 API token 洩露，請每位組員依下列步驟自行註冊與設定。**

### (A) 註冊 OpenRouter.ai 並取得 API Key
1. 前往 [OpenRouter.ai](https://openrouter.ai/) 註冊帳號。
2. 登入後，進入「API Keys」頁面。
3. 點擊「Create API Key」產生新金鑰，複製並妥善保存。

### (B) 在 CodeSandbox 設定環境變數
1. 開啟你的專案。
2. 點選左上角「☰」主選單（Menu）。
3. 選擇 **Env variables**（環境變數）。
4. 新增一個環境變數：
   - 名稱：`OPENROUTER_API_KEY`
   - 值：貼上你自己的 OpenRouter token
5. 按下「Save」或「✓」儲存。
6. **務必重啟（Restart）你的 workspace**，讓變數生效。

> 參考官方說明：[CodeSandbox - Environment variables and secrets](https://codesandbox.io/docs/learn/environment/secrets)

### (C) 本地開發可於終端機設定：
```bash
export OPENROUTER_API_KEY=你的token
# 或於 .env 檔加入 OPENROUTER_API_KEY=你的token
```

### (D) Stable Horde 圖片生成已內建公開測試 key，無需註冊。

---

## 3. 啟動 FastAPI 後端

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
- API 文件（Swagger UI）：
  - 本地： http://localhost:8000/docs
  - 雲端： https://<你的-sandbox-id>-8000.csb.app/docs

---

## 4. 啟動 Gradio 前端互動 Demo

```bash
python gradio_app.py
```
- CodeSandbox 會自動顯示 7860 埠口公開網址，所有人可用瀏覽器互動。

---

## 5. API 測試

- `/api/recommend`：推薦伴侶 MBTI
- `/api/chat`：MBTI 風格聊天
- `/api/avatar`：動漫頭像生成

可用 Swagger UI、curl、Postman 或 Gradio 前端測試。

---

## 6. 常見問題

- 404 Not Found：請確認訪問 `/docs` 或正確 API 路徑
- 401/403：請檢查 `OPENROUTER_API_KEY` 是否正確
- 500：請檢查 token 權限、API 配置，或貼上錯誤訊息協助排查

---

## 7. 推送到 GitHub

```bash
git add requirements.txt gradio_app.py README.md
# 如有其他異動一併加入
git commit -m "feat: 新增 Gradio 前端與自動化說明，完善 requirements"
git push
```

---

## 8. 安全性說明
- 本 repo 內**不會有任何 API token**，請每位組員自行註冊、設定自己的金鑰。
- CodeSandbox 的環境變數只對該用戶可見，fork 不會自動帶出。
- 請勿將 token 寫入程式碼或 commit 到 repo。

---

如需自動化測試腳本、API 範例、或遇到其他問題，請參考本 README 或聯絡專案協作者。
