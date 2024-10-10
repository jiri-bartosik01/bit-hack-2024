<script setup lang="js">
import {Chart, registerables} from "chart.js";
import {onMounted, useTemplateRef} from "vue";

const canvas = useTemplateRef('canvas')

onMounted(() => {
  // the opening hours is a list of values '08:00', '09:00, ..., '20:00'
  const openingHours = Array.from({length: 13}, (_, i) => `${i + 8}:00`);

  Chart.register(...registerables);
  const labels = openingHours;
  const dataset = {
    label: 'Predikce počtu návštěvníků',
    data: [65, 59, 80, 81, 56, 55, 40, 30, 20, 10, 5, 1, 0],
    fill: false,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1,
    segment: {
      borderColor: (context) => {
        const value = context.p0.parsed.y;
        return value > 50 ? 'rgb(75, 192, 192)' : 'rgb(192, 75, 75)';
      },
      borderDash: (context) => {
        const value = context.p0.parsed.y;
        return value > 50 ? [] : [5, 15];
      }
    }
  }
  const data = {
    labels: labels,
    datasets: [dataset]
  };

  const config = {
    type: 'line',
    data: data,
    options: {
      fill: true
    }
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