import axios from 'axios';

const API_BASE = 'https://zwsnvt-8000.csb.app';

export interface AvatarResponse {
  mbti: string;
  avatar_base64: string;
}

export async function getAvatar(mbti: string): Promise<AvatarResponse> {
  try {
    const res = await axios.post<AvatarResponse>(`${API_BASE}/api/avatar`, { mbti });
    return res.data;
  } catch (err) {
    throw new Error('取得 Avatar 失敗');
  }
}

export interface ChatResponse {
  reply: string;
}

export async function chatWithAI(mbti: string, message: string): Promise<ChatResponse> {
  try {
    const res = await axios.post<ChatResponse>(`${API_BASE}/api/chat`, { mbti, message });
    return res.data;
  } catch (err) {
    throw new Error('AI 聊天失敗');
  }
} 