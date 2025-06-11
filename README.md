# MBTI 伴侶聊天機器人

## 雲端 CodeSandbox 展示完整操作流程

### 1. 新增 OpenRouter API Token 環境變數
1. 前往 [OpenRouter.ai](https://openrouter.ai/) 註冊帳號並取得 API Key。
2. 在 CodeSandbox 左上角「☰」主選單 → 選 **Env variables**。
3. 新增一個環境變數：
   - 名稱：`OPENROUTER_API_KEY`
   - 值：你的 token
4. 按 Save/✓ 儲存，**然後重啟（Restart）workspace**。

### 2. 安裝所有依賴
```bash
pip install -r requirements.txt
```

### 3. 啟動 FastAPI 後端
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
- CodeSandbox 會自動分配公開網址（如 `https://xxxxxx-8000.csb.app`）。

### 4. 啟動 Gradio 前端互動 Demo
（開新終端機分頁，不要關掉 FastAPI）
```bash
python gradio_app.py
```
- CodeSandbox 會自動顯示 7860 埠口公開網址（如 `https://xxxxxx-7860.csb.app`），直接用瀏覽器打開即可互動展示。

### 5. （可選）API 文件測試
- 在瀏覽器開啟 `https://xxxxxx-8000.csb.app/docs` 可用 Swagger UI 測試 API。

### 6. 常見問題排查
- 若 Gradio 前端無法互動，請確認 FastAPI 8000 埠口有啟動且 token 設定正確。
- 若遇 401/403，請檢查 token 是否正確、是否有重啟服務。
- 若遇 500，請貼上錯誤訊息協助排查。

---

如有任何步驟遇到問題，請隨時貼錯誤訊息，我會協助你排查。
