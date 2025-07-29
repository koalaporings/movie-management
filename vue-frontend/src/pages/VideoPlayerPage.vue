<template>
    <div class="video-player">
        <h2>Video Player</h2>

        <video
            v-if="movie?.video_file"
            width="960"
            height="400"
            controls
            :preload="auto"
            :src="getVideoUrl(movie.video_file)"
        >
            Your browser does not support the video tag.
        </video>
    </div>
</template>

<script>

import { mapActions } from 'pinia';
import { useMovieStore } from '@/stores/movies';


export default {
    name: "VideoPlayerPage",
    data() {
        return {
            movie: null,
            baseURL: "http://localhost:8000"
        };
    },

    async created() {
        const pk = this.$route.query.pk;
        this.movie = await this.getMovie(pk);
    },

    methods: {
        ...mapActions(useMovieStore, ['getMovie']),

        getVideoUrl(path) {
            return `${this.baseURL}${path}`
        }
    },
};
</script>

<style scoped>
.video-player {
    max-width: 660px;
    margin: 0 auto;
    text-align: center;
}
.controls {
    margin-top: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
}
input[type="range"] {
    width: 100%;
    margin-top: 10px;
}
</style>
