import { defineStore } from 'pinia';
import axios from 'axios';

export const useMovieStore = defineStore('movie', {
	actions: {
		async fetchMovies(limit=10, offset=0) {
            if (offset > 0){
                const response = await axios.get('movie-list/', {params: {limit: limit, offset: offset}});
			    return response.data;
            } else {
                const response = await axios.get('movie-list/');
			    return response.data;
            }

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
			return response.data;
		}
	}
})
