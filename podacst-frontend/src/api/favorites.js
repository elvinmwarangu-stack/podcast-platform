import { api } from './client';

export const favoritesApi = {
  getAll: () => api.get('/favorites/'),
  add: (podcastId) => api.post(`/favorites/${podcastId}`, {}),
  remove: (podcastId) => api.delete(`/favorites/${podcastId}`),
};
