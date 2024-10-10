<script setup lang="ts">
import PoolListView from "./components/PoolListView.vue";
import {onBeforeUnmount, onMounted, Ref, ref} from "vue";
import PoolDetailView from "./components/PoolDetailView.vue";
import PredictionGraph from "./components/PredictionGraph.vue";

const currentId: Ref<null | number> = ref(null);

function updateCurrentId() {
  const path = window.location.pathname;
  const id = path.split('/')[1];
  if (id) {
    currentId.value = parseInt(id);
    if (isNaN(currentId.value)) {
      currentId.value = null;
    }
  } else {
    currentId.value = null;
  }
}

// Lifecycle hooks
onMounted(() => {
  updateCurrentId();
});

</script>

<template>
  <div v-if="currentId === null">
    <nav class="navbar navbar-expand-lg starex-bar">
      <div class="container-fluid mx-4">
        <img class="logo" src="./assets/starez.svg">
        <a class="navbar-brand" href="#">Obsazenost sportovišť</a>
      </div>
    </nav>
    <div class="container pt-4">
      <PoolListView/>
    </div>
  </div>
  <div style="height: 100%;" v-else> <!-- Detail page -->
    <PoolDetailView :pool-id="currentId"/>
  </div>
</template>

<style scoped>
  .logo {
    max-height: 28px;
  }

  .starex-bar {
    height: 100px;

  }
</style>