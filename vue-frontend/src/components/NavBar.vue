<template>
    <div class="button-group">
        <img src="../assets/logo.png" width="100px" height="60px" />

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

        <BaseButton
            class="logout-button"
            type="secondary"
            label="Logout"
            @click="handleLogout"
        />
    </div>
</template>

<script>
import BaseButton from './generics/BaseButton.vue';
import api from '@/auth/api';
export default {
    components: {
        BaseButton,
    },

    methods: {
        goToUpload() {
            this.$router.push({
                name: 'upload',
                query: {
                    status: 'create',
                },
            });
        },

        handleLogout() {
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');

            delete api.defaults.headers.common['Authorization'];

            this.$router.push('/login');
        },
    },
};
</script>

<style scoped>
.button-group {
    left: 0;
    display: flex;

    img {
        margin-right: 20px;
    }

    .logout-button {
        margin-left: auto;
    }
}
</style>
