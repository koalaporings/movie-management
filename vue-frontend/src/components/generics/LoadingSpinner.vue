<template>
    <div :class="['spinner-overlay', { fullscreen: fullscreen }]">
        <div class="spinner"></div>
    </div>
</template>
<script>
export default {
    props: {
        fullscreen: {
            type: Boolean,
            default: false
        }
    }
};
</script>
<style scoped>
    .spinner-overlay {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 40px;
    }

    /* Fullscreen mode styles */
    .spinner-overlay.fullscreen {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 9999;
    }

    .spinner {
        width: 50px;
        height: 50px;
        border: 6px solid #ccc;
        border-top-color: #3498db;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to {
            transform: rotate(360deg);
        }
    }
</style>

