import "./styles.css";
import MBTISelector from "./MBTISelector";
import AvatarCustomizer from "./AvatarCustomizer";
import { useState } from "react";

export default function App() {
  const [selectedMBTI, setSelectedMBTI] = useState("");
  const [recommended, setRecommended] = useState([]);
  const [avatarPrompt, setAvatarPrompt] = useState("");
  const [avatarImage, setAvatarImage] = useState("");

  const handleSelect = (mbti, partners) => {
    setSelectedMBTI(mbti);
    setRecommended(partners);
  };

  const handleGenerateAvatar = (prompt, config, imageUrl) => {
    setAvatarPrompt(prompt);
    setAvatarImage(imageUrl);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6 text-center">
        未來伴侶聊天機器人 💕
      </h1>

      <div className="max-w-md mx-auto">
        {/* Step 1: 選擇 MBTI */}
        <MBTISelector onSelect={handleSelect} />

        {/* Step 2: 顯示推薦伴侶 */}
        {recommended.length > 0 && (
          <div className="mt-6">
            <h3 className="text-lg font-medium mb-2">
              根據你是 <span className="font-bold">{selectedMBTI}</span>
              ，我們推薦你與：
            </h3>
            <ul className="list-disc list-inside">
              {recommended.map((p) => (
                <li key={p}>{p}</li>
              ))}
            </ul>

            {/* Step 3: Avatar 自訂元件 */}
            <AvatarCustomizer onGenerate={handleGenerateAvatar} />
          </div>
        )}

        {/* Step 4: 顯示最終 prompt */}
        {avatarPrompt && (
          <div className="mt-6 p-4 bg-green-100 rounded">
            <h3 className="font-semibold">生成的 Avatar 描述（prompt）：</h3>
            <p className="mt-2 text-sm font-mono text-gray-700">
              {avatarPrompt}
            </p>
          </div>
        )}

        {/* Step 5: 顯示生成的圖片 */}
        {avatarImage && (
          <div className="mt-4">
            <img
              src={avatarImage}
              alt="生成的伴侶 Avatar"
              className="rounded shadow w-full"
            />
          </div>
        )}
      </div>
    </div>
  );
}
