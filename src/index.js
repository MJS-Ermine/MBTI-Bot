import React from "react";
import ReactDOM from "react-dom/client"; // ✅ 注意這裡
import App from "./App";
import "./styles.css"; // Tailwind CSS

// ✅ 使用 createRoot
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
