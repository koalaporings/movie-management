<script>
export default {
    name: "BaseButton",
    props: {
        type: {
            type: String,
            default: "primary",
            required: false,
        },
        label: {
            type: String,
            required: false,
        }
    },
    computed: {
        btnClass() {
            return `btn btn-${this.type}`;
        },
    },
};
</script>

<template>
    <button :class="btnClass" @click="$emit('click')">
        <slot>{{ label }}</slot>
    </button>
</template>

<style scoped>
.btn {
    padding: 10px 20px;
    font-size: 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

/* Variants */
.btn-primary {
    background-color: #007bff;
    color: white;
}

.btn-primary:hover {
    background-color: #0069d9;
}

.btn-secondary {
    background-color: #6c757d;
    color: white;
}

.btn-secondary:hover {
    background-color: #5a6268;
}

.btn-danger {
    background-color: #dc3545;
    color: white;
}

.btn-danger:hover {
    background-color: #c82333;
}
</style>