<template>
    <div class="upload">
        <div class="upload-header">
            <h2> {{ isCreate ? 'Upload a Movie' : 'Update Movie' }}</h2>
        </div>
        <div class="form">
            <form @submit.prevent="uploadMovie" enctype="multipart/form-data">
                <div class="form-input">
                    <label for="title">Title</label>
                    <br/>
                    <input
                        v-model="form.title"
                        type="text"
                        id="title"
                        required />
                </div>
                <div class="form-input">
                    <label for="description">Description</label>
                    <br/>
                    <textarea id="description" v-model="form.description"></textarea>
                </div>
                <div class="form-input">
                    <label for="video">Thumbnail</label>
                    <br/>
                    <input type="file" id="thumbnail" @change="handleImageFile" accept=".jpg, .jpeg, .png" required />
                </div>
                <div class="form-input">
                    <label for="video">Video File</label>
                    <br/>
                    <input type="file" id="video" @change="handleFile" accept=".mp4, .ogv, .webm" required />
                </div>
                <BaseButton
                    class="form-submit"
                    label="Submit"
                />
            </form>
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
                video: null,
                thumbnail: null
            },
            isSubmitting: false
        }
    },

    computed: {
        isCreate() {
            return this.$route.query.status === 'create';
        },

        isUpdate() {
            return this.$route.query.status === 'update';
        },

        moviePk() {
            return this.$route.query?.pk;
        },

        hasFormErrors() {
            return this.isCreate && (!this.form.title || !this.form.description || !this.form.video || !this.form.thumbnail);
        },
    },

    async mounted() {
        if (this.isUpdate){
            const response = await this.getMovie(this.moviePk);
            this.form.title = response.title;
            this.form.description = response.description;
        }
    },

    methods: {
        ...mapActions(useMovieStore, ['createMovie', 'updateMovie', 'getMovie']),

        handleImageFile(event) {
            this.form.thumbnail = event.target.files[0];
        },

        handleFile(event) {
            this.form.video = event.target.files[0];
        },

        validateData() {
            if (this.isCreate) {
                if (this.hasFormErrors) {
                    return false;
                }
            }

            return true;
        },

        async uploadMovie(){
            this.isSubmitting = true;
            const valid = this.validateData();
            if (!valid) return;

            const formData = new FormData();
            if (this.form.title) formData.append('title', this.form.title);
            if (this.form.description) formData.append('description', this.form.description);
            if (this.form.video) formData.append('video_file', this.form.video);
            if (this.form.thumbnail) formData.append('thumbnail', this.form.thumbnail)

            if (this.isCreate) await this.createMovie(formData)
            else await this.updateMovie(this.moviePk, formData)
            this.isSubmitting = false;
        }
    }
}
</script>
<style scoped>
    .upload {
        margin-left: 50px;
        margin-top: 60px;
    }

    .upload-header {
        font-size: 24px;
    }

    .form {
        display: flex;
        flex-direction: column;
        font-size: 20px;

        .form-input {
            padding-top: 20px;

            input {
                width: 400px;
                height: 30px;
                font-size: 16px;
            }

            textarea {
                width: 1000px;
                height: 250px;
                font-size: 16px;
            }
        }

        .form-submit {
            margin-top: 20px;
            margin-left: -2px;
            width: 100px;
        }
    }
</style>
