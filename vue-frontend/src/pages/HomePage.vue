<template>
    <LoadingSpinner v-if="isLoading"/>
    <template v-else>
        <div v-if="movies.length" class="group">
            <div class="movie-carousel">
                <MovieCarousel :movies="movies" />
            </div>
            <div class="movie-list">
                <MovieList
                    :movies="movies"
                    :count="count"
                    @refetch-movies="refetchMovies"
                />
            </div>
        </div>
        <EmptyState
            v-else
            title="No movies to show"
            message="Upload movies to show the list of movies."
            button-text="Upload here"
            @action="goToUpload"
        />
    </template>
</template>

<script>
import { mapState, mapActions } from 'pinia';
import { useMovieStore } from '@/stores/movies';
import MovieCarousel from "@/components/MovieCarousel.vue";
import MovieList from "@/components/MovieList.vue";
import LoadingSpinner from '@/components/generics/LoadingSpinner.vue';
import EmptyState from '@/components/generics/EmptyState.vue';

export default {
    name: "HomePage",
    components: {
        MovieCarousel,
        MovieList,
        LoadingSpinner,
        EmptyState
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
        },

        goToUpload() {
            this.$router.push({
                name: 'upload',
                query: {
                    status: 'create'
                }
            });
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
