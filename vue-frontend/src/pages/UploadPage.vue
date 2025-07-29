<template>
    <div class="form">
        <form @submit.prevent="submitForm" enctype="multipart/form-data">
            <div class="form-input">
                <label for="title">Title:</label>
                <input type="text" id="title" v-model="form.title" required />
            </div>
            <div class="form-input">
                <label for="description">Description:</label>
                <textarea id="description" v-model="form.description"></textarea>
            </div>
            <div class="form-input">
                <label for="video">Video File:</label>
                <input type="file" id="video" @change="handleFile" accept="video/*, .mkv" required />
            </div>
            <BaseButton
                label="Submit"
                @click="uploadMovie"
            />
        </form>
    </div>
</template>
<script>
import { mapActions } from 'pinia';
import { useMovieStore } from '@/stores/movies';
import BaseButton from '@/components/generics/BaseButton.vue';

export default {
    name: "UploadPage",

    components: {
        BaseButton
    },

    data() {
        return {
            form: {
                title: '',
                description: '',
                video: null
            }
        }
    },

    methods: {
        ...mapActions(useMovieStore, ['createMovie']),

        handleFile(event) {
            this.form.video = event.target.files[0];
        },

        async uploadMovie(){
            const formData = new FormData();
            formData.append('title', this.form.title);
            formData.append('description', this.form.description);
            formData.append('video_file', this.form.video);
            
            await this.createMovie(formData)
        }
    }
}
</script>
<style scoped>
    .form {
        display: flex;
        margin-top: 60px;
        justify-content: center;

        .form-input {
            padding-top: 20px;
        }
    }
</style>