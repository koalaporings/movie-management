import { defineStore } from 'pinia';
import axios from 'axios';

export const useMovieStore = defineStore('movie', {
	state: () => ({
		movies: []
	}),

	actions: {
		async fetchMovies() {
			const response = await axios.get('movie-list/');
			this.movies = response.data;
		},

		async getMovie(pk) {
			const response = await axios.get('get-movie/', { params: { pk } });
			return response.data;
		},

		async createMovie(formData) {
			const response = await axios.post('create-movie/', formData, {
				headers: { 'Content-Type': 'multipart/form-data' },
			});
			await this.fetchMovies();
			return response.data;
		},

		async updateMovie(pk, formData) {
			const response = await axios.put('update-movie/', formData, { params: { pk } });
			await this.fetchMovies();
			return response.data;
		},
		
		async deleteMovie(pk) {
			const response = await axios.delete('delete-movie/', { params: { pk } });
			await this.fetchMovies();
			return response.data;
		}
	}
})