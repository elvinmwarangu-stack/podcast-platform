import { api } from './client';

export const categoriesApi = {
  getAll: () => api.get('/categories/'),
  getById: (id) => api.get(`/categories/${id}`),
  create: (data) => api.post('/categories/', data),
};
