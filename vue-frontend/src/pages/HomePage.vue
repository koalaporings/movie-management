<script>
import NavBar from "@/components/NavBar.vue";
import MovieCarousel from "@/components/MovieCarousel.vue";
import MovieList from "@/components/MovieList.vue";

export default {
    name: "HomePage",
    components: {
        NavBar,
        MovieCarousel,
        MovieList,
    },
    data() {
        return {
        featuredMovies: [
            { id: 1, title: "Inception", poster: "https://via.placeholder.com/400x200?text=Inception" },
            { id: 2, title: "Interstellar", poster: "https://via.placeholder.com/400x200?text=Interstellar" },
            { id: 3, title: "Tenet", poster: "https://via.placeholder.com/400x200?text=Tenet" },
        ],
        movieList: [
            { id: 4, title: "The Batman" },
            { id: 5, title: "Dune" },
            { id: 6, title: "Avengers: Endgame" },
        ],
        };
    },
}
</script>
<template>
    <div class="group">
        <div class="header">
            <NavBar/>
        </div>
        <div class="movie-carousel">
            <MovieCarousel :movies="featuredMovies" />
        </div>
        <div class="movie-list">
            <h2> Now Showing </h2>
            <MovieList :movies="movieList" />
        </div>
    </div>
</template>
<style scoped>
    .group {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        background-color: black;
    }

    .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background-color: #111;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }

    .movie-carousel {
        padding: 16px;
        height: 50%;
        width: 100%;
        align-content: center;
        box-sizing: border-box;
    }

    .movie-list {
        padding: 16px;
        height: auto;
        width: 100%;
        justify-items: center;
        box-sizing: border-box;
    }
</style>