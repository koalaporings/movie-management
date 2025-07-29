<template>
    <div class="button-group">
        <BaseButton
            type="primary"
            label="Home"
            @click="$router.push('/home')"
        />
        <BaseButton
            type="primary"
            label="List"
            @click="$router.push('/upload')"
        />
        <BaseButton
            type="primary"
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
        display: flex;
        justify-content: space-evenly;
    }
</style>