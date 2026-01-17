import { api } from './client';

export const usersApi = {
  getMe: () => api.get('/users/me'),
  updateMe: (data) => api.put('/users/me', data),
  resetPassword: (data) => api.post('/users/me/reset-password', data),
};
