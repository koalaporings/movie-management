<template>
    <div class="upload">
        <div class="upload-header">
            <h2> Upload a Movie</h2>
        </div>
        <div class="form">
            <form @submit.prevent="submitForm" enctype="multipart/form-data">
                <div class="form-input">
                    <label for="title">Title:</label>
                    <br/>
                    <input type="text" id="title" v-model="form.title" required />
                </div>
                <div class="form-input">
                    <label for="description">Description:</label>
                    <br/>
                    <textarea id="description" v-model="form.description"></textarea>
                </div>
                <div class="form-input">
                    <label for="video">Video File:</label>
                    <br/>
                    <input type="file" id="video" @change="handleFile" accept="video/*, .mkv" required />
                </div>
            </form>
            <BaseButton
                class="form-submit"
                label="Submit"
                @click="uploadMovie"
            />
        </div>
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
    .upload {
        margin-top: 60px;
    }

    .upload-header {
        font-size: 24px;
    }

    .form {
        display: flex;
        flex-direction: column;

        .form-input {
            padding-top: 20px;

            input {
                width: 600px;
            }

            textarea {
                width: 600px;
                height: 100px;
            }
        }

        .form-submit {
            margin-top: 20px;
            width: 100px;
        }
    }
</style>
