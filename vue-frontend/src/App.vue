<template>
    <div id="app">
        <div v-if="isNotLogin" class="header">
            <NavBar/>
        </div>
        <div class="body">
            <router-view />
        </div>
    </div>
</template>
<script>
import NavBar from './components/NavBar.vue';
export default {
    components: {
        NavBar
    },

    computed: {
        isNotLogin() {
            return this.$route.name !== 'login' && this.$route.name !== 'register';
        }
    },
};
</script>
<style>
    .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background-color: #111;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }

    body {
        margin-top: 80px;
    }
</style>
