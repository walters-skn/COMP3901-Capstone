
import {createRouter,createWebHistory} from 'vue-router';

import LoginPage from '@/components/LoginPage.vue'
import HomePage from '@/components/HomePage.vue'
import RegisterPage from '@/components/RegisterPage.vue'
import DiabotPage from '@/components/DiabotPage.vue'
import NavBar from '@/components/NavBar.vue';
import SubscriberPage from '@/components/SubscriberPage.vue';
import NutritionalScanner from '@/components/NutritionalScanner.vue';
import SubscriberNavbar from '@/components/SubscriberNavbar.vue';
import ClinicsPage from '@/components/ClinicsPage.vue';
import NotificationPage from '@/components/NotificationPage.vue';
import MealPage from '@/components/MealPage.vue';

const routes = [
    { path: '/', component: HomePage },
    { path: '/home', component: HomePage},
    { path: '/register', component: RegisterPage },
    { path: '/login', component: LoginPage },
    { path: '/diabot', component: DiabotPage},
    { path: '/navbar', component: NavBar},
    { path: '/subscriber', component: SubscriberPage},
    { path: '/scanner', component: NutritionalScanner},
    { path: '/snavbar', component: SubscriberNavbar},
    { path: '/clinics', component: ClinicsPage},
    { path: '/notifications', component: NotificationPage},
    { path: '/meal', component: MealPage},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
 
 