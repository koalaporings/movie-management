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
            label="List"
            @click="$router.push('/upload')"
        />
        <BaseButton
            type="secondary"
            label="About"
            @click="$router.push('/watch')"
        />
    </div>
</template>

<script>
import BaseButton from './generics/BaseButton.vue';

export default {
    components: {
        BaseButton
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
