import {createRouter,createWebHashHistory} from 'vue-router';
import LoginPage from './components/LoginPage.vue'
// import HomePage from './components/HomePage.vue'
import RegisterPage from './components/RegisterPage.vue'
import ProfilePage from './components/ProfilePage.vue'
import FooterView from './components/FooterView.vue'


const routes = [
    // { path: '/', component: HomePage },
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterPage },
    { path: '/profile', component: ProfilePage },
    { path: '/footer', component: FooterView}
]
const router = createRouter({history: createWebHashHistory(),routes})

export default router;
 
 