import { api } from './client';

export const podcastsApi = {
  getAll: () => api.get('/podcasts/'),
  getById: (id) => api.get(`/podcasts/${id}`),
  create: (data) => api.post('/podcasts/', data),
  update: (id, data) => api.put(`/podcasts/${id}`, data),
};
