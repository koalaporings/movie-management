<template>
    <div class="button-group">
        <img
            width="50px"
            height="50px"
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
            margin-right: 4px;
        }

    }
</style>
