<script setup lang="js">
import {Chart, registerables} from "chart.js";
import {onMounted, useTemplateRef} from "vue";

const canvas = useTemplateRef('canvas')

onMounted(() => {
  // the opening hours is a list of values '08:00', '09:00, ..., '20:00'
  const openingHours = Array.from({length: 13}, (_, i) => `${i + 8}:00`);
  const currentHourOfDay = new Date().getHours();
  const currentHourIndex = currentHourOfDay - 8;

  Chart.register(...registerables);
  const labels = openingHours;
  const dataset = {
    data: [65, 59, 80, 81, 56, 55, 40, 30, 20, 10, 5, 1, 0],
    fill: true,
    tension: 0.35,
    pointBorderColor: 'rgba(30, 30, 30, 0.5)',
    pointBackgroundColor: 'rgba(30, 30, 30, 0.5)',
    segment: {
      borderColor: (context) => {
        return context.p0.parsed.x >= currentHourIndex ? 'rgba(75, 192, 192, 1)' : 'rgba(192, 75, 75, 1)';
      },
      borderDash: (context) => {
        // make the line dashed after the current hour of day
        console.log(`Calculating borderDash for ${context.p0.parsed.x}`);
        return context.p0.parsed.x >= currentHourIndex ? [8, 10] : undefined;
      },
      backgroundColor: (context) => {
        return context.p0.parsed.x >= currentHourIndex ? 'rgba(75, 192, 192, 0.1)' : 'rgba(192, 75, 75, 0.5)';
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
      legend: {
        display: false
      },
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