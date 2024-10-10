<script setup lang="ts">
import {getPoolById, Pool} from "../helpers/pools.ts";
import {computed} from "vue";

const props = defineProps(['poolId']);

const pool: Pool = computed(() => {
  return getPoolById(props.poolId);
})


console.log(pool);

</script>

<template>

</template>

<style scoped>

</style>