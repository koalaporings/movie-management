import api from './api';

export async function register(username, password) {
  try {
    const response = await api.post('/movies/register/', { username, password });
    return { success: true, message: response.data.message };
  } catch (error) {
    return {
      success: false,
      message: error.response?.data?.error || 'Registration failed',
    };
  }
}
