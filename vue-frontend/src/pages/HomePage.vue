<template>
    <LoadingSpinner v-if="isLoading"/>
    <div v-else class="group">
        <div class="movie-carousel">
            <MovieCarousel v-if="movies" :movies="movies" />
        </div>
        <div class="movie-list">
            <MovieList
                v-if="movies"
                :movies="movies"
                :count="count"
                @refetch-movies="refetchMovies"
            />
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'pinia';
import { useMovieStore } from '@/stores/movies';
import MovieCarousel from "@/components/MovieCarousel.vue";
import MovieList from "@/components/MovieList.vue";
import LoadingSpinner from '@/components/generics/LoadingSpinner.vue';

export default {
    name: "HomePage",
    components: {
        MovieCarousel,
        MovieList,
        LoadingSpinner
    },

    data() {
        return {
            movies: [],
            count: 0,
            itemsPerPage: 10,
            isLoading: true
        };
    },

    computed: {
        ...mapState(useMovieStore, ['movies'])
    },

    async mounted() {
        const response = await this.fetchMovies()
        this.movies = response.results;
        this.count = response.count;
        this.isLoading = false;
    },

    methods: {
        ...mapActions(useMovieStore, ['fetchMovies']),

        async refetchMovies(currentPage) {
            const response = await this.fetchMovies(this.itemsPerPage, this.itemsPerPage*(currentPage-1))
            this.movies = response.results;
            this.count = response.count;
        }
    },

}
</script>

<style scoped>
    .group {
        display: flex;
        flex-direction: row;
    }

    .movie-carousel {
        padding: 60px;
        height: auto;
        width: 100%;
        align-content: center;
        box-sizing: border-box;
    }

    .movie-list {
        padding: 16px;
        height: auto;
        width: 100%;
        box-sizing: border-box;
    }

    LoadingSpinner {
        height: 100%;
        width: 100%;
        align-items: center;
    }
</style>
