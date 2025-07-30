<template>
    <div class="modal-backdrop" @click.self="close">
        <div class="modal-box">
            <p>{{ message }}</p>
            <button @click="$emit('close')">Close</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SimpleModal',
    props: {
        message: {
            type: String,
            default: 'This is a modal.'
        }
    },
    emits: ['close'],
    methods: {
        close() {
            this.$emit('close');
        }
    }
};
</script>

<style scoped>

.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgb(63, 55, 55);
    /* Transparent black background */
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.modal-box {
    background: rgb(24, 22, 22);
    padding: 1.5rem;
    border-radius: 4px;
    text-align: center;

    p {
        color: white;
    }
}
</style>
