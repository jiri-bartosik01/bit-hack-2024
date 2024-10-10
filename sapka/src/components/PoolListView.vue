<script setup lang="ts">

import {pools} from "../helpers/pools.ts";

</script>

<template>
  <div class="container">
    <div class="card" style="width: 18rem;" v-for="pool in pools">
      <img class="card-img-top" :src="pool.imageUrl" alt="Card image cap">
      <div class="card-body">
        <h5 class="card-title">{{pool.name}}</h5>
        <p class="card-text">{{pool.description}}</p>
        <a href="#" class="btn btn-primary">Detail</a>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>