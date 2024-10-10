<script setup lang="ts">
import {getPoolById, Pool} from "../helpers/pools.ts";
import {computed, ComputedRef} from "vue";
import PredictionGraph from "./PredictionGraph.vue";

const props = defineProps(['poolId']);

const pool: ComputedRef<Pool | undefined> = computed(() => {
  return getPoolById(props.poolId);
});

const returnToBasePath = () => {
  window.location.href = `/`; // Manually navigate to /pool/{poolId}
};
</script>

<template>
  <div style="height: 100%;" v-if="pool">
    pool {{pool.id}}
    <PredictionGraph></PredictionGraph>
  </div>
  <div v-else>
    <div class="d-flex flex-column min-vh-100 justify-content-center align-items-center">
      <div class="card border-danger" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">Ale ne!</h5>
          <h6 class="card-subtitle mb-2 text-body-secondary">Bazén nenalezen</h6>
          <p class="card-text">Zkontrolujte adresu nebo se vraťte na hlavní stranu.</p>
          <a @click="returnToBasePath" class="card-link">Seznam bazénů</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>