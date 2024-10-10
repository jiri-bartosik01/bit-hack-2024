<script setup lang="ts">
import {getPoolById, Pool} from "../helpers/pools.ts";
import {computed} from "vue";

const props = defineProps(['poolId']);

const pool: Pool = computed(() => {
  return getPoolById(props.poolId);
})
</script>

<template>
  <div v-if="pool">
    pool {{pool.id}}
  </div>
  <div v-else>
    neni pool
  </div>
</template>

<style scoped>

</style>