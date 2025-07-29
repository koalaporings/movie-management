<script>
import NavBar from './components/NavBar.vue';
export default {
    components: {
        NavBar
    }
};
</script>
<template>
    <div id="app">
        <div class="header">
            <NavBar/>
        </div>
        <div class="body">
            <router-view />
        </div>
    </div>
</template>
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
        padding: 72px;
    }
</style>