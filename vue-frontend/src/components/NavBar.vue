<script>
import BaseButton from './generics/BaseButton.vue';

export default {
    components: {
        BaseButton
    }
};
</script>
<template>
    <div class="button-group">
        <BaseButton
            type="primary"
            label="Home"
        />
        <BaseButton
            type="primary"
            label="List"
        />
        <BaseButton
            type="primary"
            label="About"
        />
    </div>
</template>
<style scoped>
    .button-group {
        display: flex;
        justify-content: space-evenly;
    }
</style>