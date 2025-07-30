<template>
    <div class="empty-state">
        <img src="../../assets/empty-state.png" alt="No data" class="empty-image"/>
        <h2>{{ title }}</h2>
        <p>{{ message }}</p>
        <div class="button">
            <button v-if="buttonText" @click="$emit('action')">
                {{ buttonText }}
            </button>
        </div>
    </div>
</template>

<script setup>
    defineProps({
        title: {
            type: String,
            default: 'Nothing here yet'
        },
        message: {
            type: String,
            default: 'Once you add some data, it will show up here.'
        },
        buttonText: {
            type: String,
            default: ''
        }
    })
</script>

<style scoped>
    .empty-state {
        margin-top: 20px;;
        text-align: center;
        padding: 2rem;
        color: #555;
    }

    .empty-image {
        max-width: 200px;
        margin-bottom: 1rem;
    }

    button {
        margin-top: 1rem;
        padding: 0.5rem 1rem;
        background: #2e7d32;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
</style>
