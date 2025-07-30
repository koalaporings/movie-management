<template>
    <ul class="movie-list">
        <div class="movie-list-header">
            <h2> Movie Catalouge </h2>
        </div>
        <div class="movie-list-container">
            <li v-for="movie in movies" :key="movie.id">
                <div class="movie-wrapper">
                    <div class="movie-data">
                        <div class="movie-title">
                            {{ movie.title }}
                        </div>
                    </div>
                    <div class="movie-actions">
                        <BaseButton
                            label="View"
                            @click="goToView(movie.id)"
                        />
                        <BaseButton
                            label="Update"
                            type="secondary"
                            @click="goToUpdate(movie.id)"
                        />
                        <BaseButton
                            label="Delete"
                            type="danger"
                            @click="true"
                        />
                    </div>
                </div>
            </li>
        </div>
    </ul>
</template>

<script>
import { mapActions } from 'pinia';
import { useMovieStore } from '@/stores/movies';
import BaseButton from './generics/BaseButton.vue';

export default {
    name: "MovieList",

    components: {
        BaseButton
    },

    props: {
        movies: Array,
    },

    methods: {
        ...mapActions(useMovieStore, ['deleteMovie']),

        deleteSelectedMovie(pk) {
            const response = this.deleteMovie(pk);
            console.log(response)
        },

        goToView(pk) {
            this.$router.push({
                name: 'watch',
                query: { pk: pk }
            });
        },

        goToUpdate(pk) {
            this.$router.push({
                name: 'upload',
                query: {
                    pk: pk,
                    status: 'update'
                }
            });
        }
    }
};
</script>

<style scoped>
.movie-list {
    top: 0;
    margin: 0 auto;
    padding: 0;
    list-style: none;
}

.movie-list-header {
    width: 100%;
    margin-bottom: 12px;
    top: 0;
    left: 0;

    h2 {
        font-size: 48px;
        font-weight: bolder;
    }
}

.movie-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: space-between;

    .movie-title {
        font-size: 24px;
    }
}


.movie-list li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
}
</style>
