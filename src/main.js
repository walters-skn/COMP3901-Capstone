
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
// import AppRouter from './App.vue'

const app = createApp(App);
app.use(router);
app.config.productionTip = false;
app.mount('#app');
