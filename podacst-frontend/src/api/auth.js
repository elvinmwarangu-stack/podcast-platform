import { api } from './client';

const BASE_URL = import.meta.env.VITE_API_URL;

export const authApi = {
  login: async (username, password) => {
    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);

    const response = await fetch(`${BASE_URL}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: formData,
    });

    if (!response.ok) throw new Error('Login failed');
    return response.json();
  },

  register: (data) => api.post('/auth/register', data),

  forgotPassword: (email) => api.post('/auth/forgot-password', { email }),

  resetPassword: (token, new_password) =>
    api.post('/auth/reset-password', { token, new_password }),
};
