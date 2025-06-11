import { useState } from "react";

const mbtiList = [
  "INTJ",
  "INTP",
  "ENTJ",
  "ENTP",
  "INFJ",
  "INFP",
  "ENFJ",
  "ENFP",
  "ISTJ",
  "ISFJ",
  "ESTJ",
  "ESFJ",
  "ISTP",
  "ISFP",
  "ESTP",
  "ESFP",
];

const mbtiPartnerMap = {
  INTJ: ["ENFP", "INTP", "ENFJ"],
  INTP: ["ENFP", "INFJ", "ENTP"],
  ENTJ: ["INFP", "ENTP", "ISFP"],
  ENTP: ["INFJ", "ISFJ", "INFP"],
  INFJ: ["ENFP", "ENTP", "ISFP"],
  INFP: ["ENFJ", "INFJ", "ENFP"],
  ENFJ: ["INFP", "ISFP", "INFJ"],
  ENFP: ["INFJ", "INTJ", "ISFJ"],
  ISTJ: ["ESFP", "ISFJ", "ESTP"],
  ISFJ: ["ENTP", "ESFP", "ISFP"],
  ESTJ: ["INFP", "ISFP", "ESFP"],
  ESFJ: ["INTP", "ISFP", "ISTP"],
  ISTP: ["ESFJ", "ISFJ", "ENFP"],
  ISFP: ["ENFJ", "ESFJ", "INFP"],
  ESTP: ["ISFJ", "INFJ", "ENFP"],
  ESFP: ["ISTJ", "ISFJ", "INTP"],
};

export default function MBTISelector({ onSelect }) {
  const [selected, setSelected] = useState("");

  const handleChange = (e) => {
    const mbti = e.target.value;
    setSelected(mbti);
    const recommended = mbtiPartnerMap[mbti] || [];
    onSelect(mbti, recommended);
  };

  return (
    <div className="p-4 bg-white rounded shadow">
      <h2 className="text-xl font-semibold mb-2">請選擇你的 MBTI</h2>
      <select
        className="border rounded p-2 w-full"
        value={selected}
        onChange={handleChange}
      >
        <option value="">請選擇</option>
        {mbtiList.map((mbti) => (
          <option key={mbti} value={mbti}>
            {mbti}
          </option>
        ))}
      </select>
    </div>
  );
}
