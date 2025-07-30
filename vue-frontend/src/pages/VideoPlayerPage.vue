<template>
    <div class="video-player">
        <div class="video-container">
            <video
                width="800"
                height="450"
                controls
                :preload="auto"
                :src="getUrl(movie.video_file)"
            >
                Your browser does not support the video tag.
            </video>
        </div>
        <div class="video-data">
            <div class="video-title">
                <img :src="getUrl(movie.thumbnail)" alt="Girl in a jacket" width="100" height="150">
                <h1>{{ movie.title }}</h1>
            </div>
            <div class="video-description">
                <h3>Description</h3>
                {{ movie.description }}
            </div>
            <div class="video-date">
                <h3>Date Added</h3>
                {{ movie.date_added ?? '07-30-25'}}
            </div>
        </div>
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

        getUrl(path) {
            return `${this.baseURL}${path}`
        }

    },
};
</script>

<style scoped>
    .video-player {
        display: flex;
        margin-top: 20px;
    }

    .video-container {
        min-width: 900px;
        height: 500px;
        display: flex;
        justify-content: center;
    }

    .video-data {
        width: auto;
        margin-left: 20px;
        margin-top: 50px;

        .video-title {
            display: flex;
            flex-direction: row;
            font-size: 24px;

            h1 {
                margin-left: 20px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
        }

        .video-description {
            font-size: 16px;
            margin-right: 20px;
            text-align: justify;

            h3 {
                font-size: 20px;
            }
        }

        .video-date {
            font-size: 16px;

            h3 {
                font-size: 20px;
            }
        }
    }

    .video-data > div {
        padding: 10px;
    }

</style>
