<template>
    <div class="carousel">
        <img :src="movies[currentIndex].poster" :alt="movies[currentIndex].title" />
        <div class="carousel-controls">
            <button @click="prev">◀</button>
            <span>{{ movies[currentIndex].title }}</span>
            <button @click="next">▶</button>
        </div>
    </div>
</template>

<script>
export default {
    name: "MovieCarousel",
    props: {
        movies: Array,
    },
    data() {
        return {
            currentIndex: 0,
        };
    },
    methods: {
        next() {
            this.currentIndex = (this.currentIndex + 1) % this.movies.length;
        },
        prev() {
            this.currentIndex = (this.currentIndex - 1 + this.movies.length) % this.movies.length;
        },
    },
};
</script>

<style scoped>
.carousel {
    text-align: center;
    margin: 20px auto;
}
.carousel img {
    max-width: 100%;
    max-height: 500px;
}
.carousel-controls {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    margin-top: 10px;
}
</style>
