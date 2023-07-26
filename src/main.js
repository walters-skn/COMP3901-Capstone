
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import Vue from 'vue'

// import axios from 'axios'

// import AppRouter from './App.vue'

const app = createApp(App);
app.use(router);
app.config.productionTip = false;
// Vue.config.productionTip = false;
app.mount('#app');

// new Vue({
//     render: h => h(App),
// }).$mount('#app')

// Vue.prototype.$axios =axios