import { api } from './client';

export const commentsApi = {
  getByPodcast: (podcastId) => api.get(`/comments/podcast/${podcastId}`),
  create: (data) => api.post('/comments/', data),
  delete: (id) => api.delete(`/comments/${id}`),
};
