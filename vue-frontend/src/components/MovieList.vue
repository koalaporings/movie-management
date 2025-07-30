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
        <div class="pagination">
            <button @click="prev" :disabled="currentPage === 1">◀</button>
            <button
                v-for="page in maxPages"
                :key="page"
                :class="{ active: page === currentPage }"
                @click="goToPage(page)"
                >
                {{ page }}
            </button>
            <button @click="next" :disabled="currentPage === count">▶</button>
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
        movies: {
            type: Array,
            required: true
        },

        count: {
            type: Number,
            required: true
        }
    },

    emits: ['refetch-movies'],

    data() {
        return {
            currentPage: 1,
            itemsPerPage: 10,
        }
    },

    computed: {
        paginatedMovies() {
            const start = (this.currentPage - 1) * this.itemsPerPage;
            const end = start + this.itemsPerPage;
            return this.movies.slice(start, end);
        },

        maxPages() {
            return Math.ceil(this.count / 10);
        }
    },

    methods: {
        ...mapActions(useMovieStore, ['deleteMovie', 'fetchMovies']),

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
        },

        next() {
            if (this.currentPage < this.maxPages) {
                this.currentPage++;
                this.$emit('refetch-movies', this.currentPage)
            }
        },

        prev() {
            if (this.currentPage > 1) {
                this.currentPage--;
                this.$emit('refetch-movies', this.currentPage)
            }
        },

        goToPage(page) {
            this.currentPage = page;
            this.$emit('refetch-movies', this.currentPage)
        },
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

.pagination {
    display: flex;
    margin-top: 20px;
    justify-content: center;
}
</style>
