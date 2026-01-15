const PRODUCTION_API_URL = 'https://podcast-platform.onrender.com';
const DEVELOPMENT_API_URL = 'http://localhost:8000';

let API_URL = import.meta.env.VITE_API_URL || (import.meta.env.DEV ? DEVELOPMENT_API_URL : PRODUCTION_API_URL);

const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

export const api = {
  async request(endpoint, options = {}) {
    try {
      const response = await fetch(`${API_URL}${endpoint}`, {
        ...options,
        headers: {
          'Content-Type': 'application/json',
          ...getAuthHeaders(),
          ...options.headers,
        },
      });
      if (!response.ok) {
        const error = await response.json().catch(() => ({ detail: 'Request failed' }));
        throw new Error(JSON.stringify(error));
      }
      return response.json();
    } catch (error) {
      // If in development and production URL fails, try localhost
      if (import.meta.env.DEV && API_URL === PRODUCTION_API_URL) {
        API_URL = DEVELOPMENT_API_URL;
        return this.request(endpoint, options);
      }
      throw error;
    }
  },

  get(endpoint) {
    return this.request(endpoint);
  },

  post(endpoint, data) {
    return this.request(endpoint, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },

  put(endpoint, data) {
    return this.request(endpoint, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  },

  delete(endpoint) {
    return this.request(endpoint, { method: 'DELETE' });
  },
};
