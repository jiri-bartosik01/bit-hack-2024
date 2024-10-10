<script setup lang="js">
import {Chart, registerables} from "chart.js";
import {onMounted, ref, useTemplateRef} from "vue";

const canvas = useTemplateRef('canvas')

onMounted(() => {
  Chart.register(...registerables);
  const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
  const dataset = {
    label: 'My First Dataset',
    data: [65, 59, 80, 81, 56, 55, 40],
    fill: false,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1
  }
  const data = {
    labels: labels,
    datasets: [dataset]
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };

  new Chart(canvas.value, config);
});

</script>

<template>
  <div class="graph">
    <canvas ref="canvas"></canvas>
  </div>
</template>

<style scoped>
.graph {
  width: 100%;
  height: 100%;
}
</style>