import api from './api';

export async function login(username, password) {
    try {
        const response = await api.post('/api/token/', {
            username,
            password,
        });

        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        api.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access;

        return true;
    } catch (error) {
        console.error('Login failed:', error);
        return false;
    }
}
