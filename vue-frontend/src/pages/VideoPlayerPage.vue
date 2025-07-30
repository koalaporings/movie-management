<template>
    <div class="video-player">
        <div class="video-container">
            <video
                width="800"
                height="450"
                controls
                :preload="auto"
                :src="getVideoUrl(movie.video_file)"
            >
                Your browser does not support the video tag.
            </video>
        </div>
        <div class="video-data">
            <div class="video-title">
                <img src="../assets/logo.svg" alt="Girl in a jacket" width="100" height="150">
                <h1>{{ movie.title ?? 'Sing'}}</h1>
            </div>
            <div class="video-description">
                <h3>Description</h3>
                {{ movie.description ?? `In the vibrant city of Calatonia, where anthropomorphic animals live, Buster Moon, an optimistic koala, struggles to save his beloved but failing theater. To revive its glory, he organizes a singing competition, mistakenly advertising a grand prize of $100,000 due to a printing error. This attracts a diverse group of contestants, each with their own dreams and challenges.

Among the hopefuls are Rosita, an overworked pig mother of 25 piglets yearning for her moment in the spotlight; Ash, a punk-rock porcupine navigating heartbreak and self-discovery; Johnny, a soulful gorilla torn between his passion for music and his father’s criminal expectations; Meena, a shy elephant with a powerful voice battling stage fright; and Mike, a brash mouse with big talent and an even bigger ego.

As the competition unfolds, the contestants form unexpected bonds, confront their fears, and rediscover their love for music. When disaster strikes and the theater collapses, Buster’s unwavering determination inspires everyone to come together for a final, heartfelt performance. Their show not only saves the theater but also transforms their lives, proving that dreams, resilience, and community can overcome any obstacle. "Sing" is a heartwarming celebration of perseverance, self-expression, and the unifying power of music.`}}
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

        getVideoUrl(path) {
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
    align-items: center;
}

.video-data {
    width: auto;
    margin-left: 20px;

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
