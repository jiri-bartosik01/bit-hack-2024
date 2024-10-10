<script setup lang="ts">
import PoolListView from "./components/PoolListView.vue";
import {onBeforeUnmount, onMounted, ref} from "vue";

const currentId = ref();

const updateCurrentId = () => {
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
};

// Lifecycle hooks
onMounted(() => {
  updateCurrentId();
  console.log(currentId.value);
  window.addEventListener('popstate', updateCurrentId);
});

onBeforeUnmount(() => {
  window.removeEventListener('popstate', updateCurrentId);
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
  <div v-else> <!-- Detail page -->
    <h1>Detail Page for ID: {{ currentId }}</h1>
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