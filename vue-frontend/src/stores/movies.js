import { defineStore } from 'pinia';
import api from '@/auth/api';

export const useMovieStore = defineStore('/movies/movie', {
	actions: {
		async fetchMovies(limit=10, offset=0) {
            if (offset > 0){
                const response = await api.get('/movies/movie-list/', {params: {limit: limit, offset: offset}});
			    return response.data;
            } else {
                const response = await api.get('/movies/movie-list/');
			    return response.data;
            }

		},

		async getMovie(pk) {
			const response = await api.get('/movies/get-movie/', { params: { pk } });
			return response.data;
		},

		async createMovie(formData) {
			const response = await api.post('/movies/create-movie/', formData, {
				headers: { 'Content-Type': 'multipart/form-data' },
			});
			await this.fetchMovies();
			return response.data;
		},

		async updateMovie(pk, formData) {
			const response = await api.put('/movies/update-movie/', formData, { params: { pk } });
			await this.fetchMovies();
			return response.data;
		},

		async deleteMovie(pk) {
			const response = await api.delete('/movies/delete-movie/', { params: { pk } });
			return response.data;
		}
	}
})
