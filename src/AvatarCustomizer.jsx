import { useState } from "react";

export default function AvatarCustomizer({ onGenerate }) {
  const [form, setForm] = useState({
    gender: "female",
    style: "anime",
    personality: "gentle",
    outfit: "casual",
    color: "cool",
  });
  const [loading, setLoading] = useState(false);

  const labels = {
    gender: "性別",
    style: "風格",
    personality: "個性",
    outfit: "裝扮",
    color: "色系",
  };

  const options = {
    gender: ["female", "male", "androgynous"],
    style: ["anime", "realistic", "pixel", "fantasy"],
    personality: ["gentle", "cool", "playful", "intelligent"],
    outfit: ["suit", "school uniform", "casual", "wizard robe"],
    color: ["cool", "warm", "black and white", "colorful"],
  };

  const handleChange = (key, value) => {
    setForm((prev) => ({ ...prev, [key]: value }));
  };

  const handleGenerate = async () => {
    const prompt = `a ${form.personality} ${form.style} ${form.gender} wearing ${form.outfit}, ${form.color} color scheme, portrait, highly detailed`;

    setLoading(true);

    try {
      const response = await fetch(
        "https://hf.space/embed/hogiahien/counterfeit-v30-anime/api/predict/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ data: [prompt] }),
        }
      );

      const result = await response.json();
      const imageUrl = result.data[0];
      onGenerate(prompt, form, imageUrl);
    } catch (err) {
      alert("圖片生成失敗，請稍後再試");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded shadow mt-6">
      <h2 className="text-lg font-semibold mb-3">自訂你的伴侶 Avatar</h2>
      {Object.keys(options).map((key) => (
        <div className="mb-3" key={key}>
          <label className="block font-medium mb-1">{labels[key]}</label>
          <select
            className="w-full p-2 border rounded"
            value={form[key]}
            onChange={(e) => handleChange(key, e.target.value)}
          >
            {options[key].map((val) => (
              <option key={val} value={val}>
                {val}
              </option>
            ))}
          </select>
        </div>
      ))}

      <button
        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
        onClick={handleGenerate}
        disabled={loading}
      >
        {loading ? "生成中..." : "建立 Avatar"}
      </button>
    </div>
  );
}
