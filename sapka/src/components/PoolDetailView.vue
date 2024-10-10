<script setup lang="ts">
const props = defineProps(['poolId'])
import { pools } from "../helpers/pools.ts";

var pool = pools.filter(obj => {
  return obj.id === props.poolId
});

console.log(pool);
</script>

<template>
  {{props.poolId}}
</template>

<style scoped>

</style>