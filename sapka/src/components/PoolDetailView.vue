<script setup lang="ts">
import {getPoolById, Pool} from "../helpers/pools.ts";
import {computed, ComputedRef, onMounted, ref} from "vue";
import PredictionGraph from "./PredictionGraph.vue";
import WeatherSunnyIcon from 'vue-material-design-icons/WeatherSunny.vue';
import WeatherCloudIcon from 'vue-material-design-icons/WeatherCloudy.vue'
import WeatherPartialIcon from 'vue-material-design-icons/WeatherPartlyCloudy.vue'
import TemperatureIcon from 'vue-material-design-icons/Thermometer.vue'
import RainIcon from 'vue-material-design-icons/Water.vue'

const loading = ref(true);

const props = defineProps(['poolId']);

const pool: ComputedRef<Pool | undefined> = computed(() => {
  return getPoolById(props.poolId);
});

const returnToBasePath = () => {
  window.location.href = `/`; // Manually navigate to /pool/{poolId}
};

async function getWeatherData(): Promise<{ temperature: number; rain: number; cloudCover: number } | undefined> {
  try {
    const response = await fetch(
        "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,rain,cloud_cover"
    );
    const data = await response.json();

    // Extract the necessary values
    const temperature = data.current.temperature_2m;
    const rain = data.current.rain;
    const cloudCover = data.current.cloud_cover;

    return {
      temperature,
      rain,
      cloudCover
    };
  } catch (error) {
    console.error("Error fetching weather data:", error);
    return undefined;
  }
}

const temperature = ref<number | null>(null);
const rain = ref<number | null>(null);
const cloudCover = ref<number | null>(null);

// Function to fetch the weather data
async function fetchWeatherData() {
  const weatherData = await getWeatherData();
  if (weatherData) {
    temperature.value = weatherData.temperature;
    rain.value = weatherData.rain;
    cloudCover.value = weatherData.cloudCover;
  }
  loading.value = false;
}

onMounted(() => {
  fetchWeatherData();
});
</script>

<template>
  <div style="height: 100%;" v-if="pool">
    <nav class="navbar bg-body-secondary px-4">
      <div class="container-fluid">
        <span class="navbar-brand mb-0 h1">{{pool.name}}</span>
        <a href="#" class="btn btn-outline-primary" @click="returnToBasePath">Ostatní sportoviště</a>
      </div>
    </nav>
    <div class="card mx-4 my-4">
      <div class="card-header d-flex">
        Informace o sportovišti
      </div>
      <div class="card-body">
        <div class="row d-flex align-items-stretch">
          <div class="col-12 col-md-4 py-2" style="min-width: 300px">
            <div class="card">
              <img class="custom-img" :src="pool.imageUrl">
              <div class="card-body">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">{{pool.description}}</li>
                  <li class="list-group-item">{{pool.covered ? "Krytý bazén" : "Venkovní bazén"}}</li>
                </ul>
              </div>
            </div>
          </div>
          <div class="col-12 col-md-8 py-2" style="min-width: 300px">
            <div class="card">
              <div class="card-body">
                <div v-if="!loading" class="row d-flex">
                  <div class="col-12 col-md px-4 d-flex flex-column justify-content-center align-items-center py-2">
                    <div class="row">
                      <weather-sunny-icon :size="60" fillColor="#ffd500" v-if="cloudCover < 25"/>
                      <weather-cloud-icon :size="60" fillColor="#b0b0b0" v-else-if="cloudCover > 70"/>
                      <weather-partial-icon :size="60" fillColor="#9df2f9" v-else/>
                    </div>
                    <div class="row fs-3">
                      {{cloudCover}} %
                    </div>
                  </div>
                  <div class="col-12 col-md px-4 d-flex flex-column justify-content-center align-items-center py-2">
                    <div class="row">
                      <temperature-icon :size="60" fillColor="#2a2927"/>
                    </div>
                    <div class="row fs-3">
                      {{temperature}} &deg;C
                    </div>
                  </div>
                  <div class="col-12 col-md px-4 d-flex flex-column justify-content-center align-items-center py-2">
                    <div class="row">
                      <rain-icon :size="60" fillColor="#00aaff" />
                    </div>
                    <div class="row fs-3">
                      {{rain}} mm
                    </div>
                  </div>
                </div>
                <div v-else-if="!loading" class="spinner-grow" role="status">
                  <span class="visually-hidden">Loading...</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="card mx-4 my-4">
      <div class="card-header">
        Predikce využití pro dnešní den
      </div>
      <div class="card-body">
        <PredictionGraph></PredictionGraph>
      </div>
    </div>
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
.custom-img {
  height: 100px;
  object-fit: cover;
  width: 100%;
}

.icon {
  height: 300px;
}


</style>