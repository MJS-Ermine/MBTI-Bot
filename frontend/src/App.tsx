import React, { useState } from 'react';
import { getAvatar, chatWithAI, AvatarResponse, ChatResponse } from './api';

const MBTI_LIST = [
  'INTJ', 'INTP', 'ENTJ', 'ENTP',
  'INFJ', 'INFP', 'ENFJ', 'ENFP',
  'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
  'ISTP', 'ISFP', 'ESTP', 'ESFP',
];

const App: React.FC = () => {
  const [mbti, setMbti] = useState<string>('INTJ');
  const [avatar, setAvatar] = useState<string>('');
  const [loadingAvatar, setLoadingAvatar] = useState<boolean>(false);
  const [chatInput, setChatInput] = useState<string>('');
  const [chatLog, setChatLog] = useState<{ from: 'user' | 'bot'; text: string }[]>([]);
  const [loadingChat, setLoadingChat] = useState<boolean>(false);
  const [error, setError] = useState<string>('');

  // 取得 AI 生成 avatar
  const handleGetAvatar = async () => {
    setLoadingAvatar(true);
    setError('');
    try {
      const res: AvatarResponse = await getAvatar(mbti);
      setAvatar(`data:image/png;base64,${res.avatar_base64}`);
    } catch (e) {
      setError('取得頭像失敗，請稍後再試');
    } finally {
      setLoadingAvatar(false);
    }
  };

  // 聊天
  const handleSendChat = async () => {
    if (!chatInput.trim()) return;
    setLoadingChat(true);
    setError('');
    setChatLog((log) => [...log, { from: 'user', text: chatInput }]);
    try {
      const res: ChatResponse = await chatWithAI(mbti, chatInput);
      setChatLog((log) => [...log, { from: 'bot', text: res.reply }]);
      setChatInput('');
    } catch (e) {
      setError('AI 回應失敗，請稍後再試');
    } finally {
      setLoadingChat(false);
    }
  };

  return (
    <div style={{ maxWidth: 480, margin: '0 auto', padding: 24 }}>
      <h1>未來伴侶聊天機器人</h1>
      <div style={{ margin: '16px 0' }}>
        <label>選擇你的 MBTI：</label>
        <select value={mbti} onChange={e => setMbti(e.target.value)}>
          {MBTI_LIST.map(type => (
            <option key={type} value={type}>{type}</option>
          ))}
        </select>
        <button onClick={handleGetAvatar} disabled={loadingAvatar} style={{ marginLeft: 8 }}>
          {loadingAvatar ? '生成中...' : '生成 AI 頭像'}
        </button>
      </div>
      {avatar && (
        <div style={{ margin: '16px 0' }}>
          <img src={avatar} alt="MBTI Avatar" style={{ width: 200, borderRadius: '50%' }} />
        </div>
      )}
      <div style={{ margin: '16px 0' }}>
        <label>AI 聊天：</label>
        <div style={{ border: '1px solid #ccc', minHeight: 120, padding: 8, marginBottom: 8 }}>
          {chatLog.map((msg, idx) => (
            <div key={idx} style={{ textAlign: msg.from === 'user' ? 'right' : 'left', color: msg.from === 'user' ? '#1976d2' : '#333' }}>
              <b>{msg.from === 'user' ? '你' : 'AI'}：</b>{msg.text}
            </div>
          ))}
        </div>
        <input
          type="text"
          value={chatInput}
          onChange={e => setChatInput(e.target.value)}
          onKeyDown={e => { if (e.key === 'Enter') handleSendChat(); }}
          disabled={loadingChat}
          style={{ width: '70%', marginRight: 8 }}
        />
        <button onClick={handleSendChat} disabled={loadingChat || !chatInput.trim()}>
          {loadingChat ? '傳送中...' : '傳送'}
        </button>
      </div>
      {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
    </div>
  );
};

export default App; 