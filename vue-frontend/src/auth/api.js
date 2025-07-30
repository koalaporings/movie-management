import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

const accessToken = localStorage.getItem('access_token');
if (accessToken) {
  api.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;
}

api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refresh_token');
        const res = await axios.post('http://localhost:8000/api/token/refresh/', {
          refresh: refreshToken,
        });

        const newAccess = res.data.access;
        localStorage.setItem('access_token', newAccess);
        api.defaults.headers.common['Authorization'] = `Bearer ${newAccess}`;
        originalRequest.headers['Authorization'] = `Bearer ${newAccess}`;
        return api(originalRequest);
      } catch (refreshError) {
        console.error('Refresh failed', refreshError);
        // Optionally redirect to login
      }
    }

    return Promise.reject(error);
  }
);

export default api;
