<template>
    <div class="carousel">
        <span>{{ movies[currentIndex].title }}</span>
        <div class="carousel-controls">
            <button @click="prev">◀</button>
            <img :src="movies[currentIndex].thumbnail" :alt="movies[currentIndex].title" />

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

    watch: {
        movies: {
            handler() {
                this.currentIndex = 0;
            }
        }
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

    span {
        font-size: 32px;
        font-weight: 900;
    }
}
.carousel img {
    width: 400px;
    height: 600px;
}
.carousel-controls {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    margin-top: 10px;
    color: white
}
</style>
