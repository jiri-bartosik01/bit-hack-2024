<script setup lang="ts">
import { pools } from "../helpers/pools.ts";
</script>

<template>

  <div class="row gy-5">
    <div class="col" v-for="pool in pools" :key="pool.id">
      <div class="card" style="width: 18rem;">
        <img class="card-img-top custom-img" :src="pool.imageUrl" alt="Card image cap">
        <div class="card-body">
          <h5 class="card-title">{{ pool.name }}</h5>
          <p class="card-text">{{ pool.description }}</p>
          <a href="#" class="btn btn-primary" @click="console.log(pool.id)">Detail</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.custom-img {
  height: 100px;
  object-fit: cover;
  width: 100%;
}

</style>
