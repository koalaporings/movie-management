<template>
    <button :class="btnClass" :disabled="disabled" @click="$emit('click')" type="submit">
        <slot>{{ label }}</slot>
    </button>
</template>

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
        },

        disabled: {
            type: Boolean,
            default: false
        }
    },
    computed: {
        btnClass() {
            return `btn btn-${this.type}`;
        },
    },
};
</script>

<style scoped>
.btn {
    padding: 10px 20px;
    margin-left: 4px;
    margin-right: 4px;
    font-size: 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

/* Types */
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
