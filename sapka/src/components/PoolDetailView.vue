<script setup lang="ts">
import {getPoolById, Pool} from "../helpers/pools.ts";
import {computed, ComputedRef} from "vue";
import PredictionGraph from "./PredictionGraph.vue";

const props = defineProps(['poolId']);

const pool: ComputedRef<Pool | undefined> = computed(() => {
  return getPoolById(props.poolId);
})
</script>

<template>
  <div style="height: 100%;" v-if="pool">
    pool {{pool.id}}
    <PredictionGraph></PredictionGraph>
  </div>
  <div v-else>
    neni pool
  </div>
</template>

<style scoped>

</style>