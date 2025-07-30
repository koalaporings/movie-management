<template>
    <div class="button-group">
        <img
            src="../assets/logo.png"
            width="100px"
            height="60px"
        >
        <BaseButton
            type="secondary"
            label="Home"
            @click="$router.push('/home')"
        />
        <BaseButton
            type="secondary"
            label="Upload"
            @click="goToUpload"
        />
    </div>
</template>

<script>
import BaseButton from './generics/BaseButton.vue';

export default {
    components: {
        BaseButton
    },

    methods: {
        goToUpload() {
            this.$router.push({
                name: 'upload',
                query: {
                    status: 'create'
                }
            });
        }
    }
};
</script>

<style scoped>
    .button-group {
        left: 0;
        display: flex;

        img {
            margin-right: 20px;
        }

    }
</style>
