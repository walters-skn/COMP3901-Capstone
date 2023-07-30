
import {createRouter,createWebHistory} from 'vue-router';

import LoginPage from '@/components/LoginPage.vue'
import HomePage from '@/components/HomePage.vue'
import RegisterPage from '@/components/RegisterPage.vue'
import DiabotPage from '@/components/DiabotPage.vue'
import NavBar from '@/components/NavBar.vue';
import SubscriberPage from '@/components/SubscriberPage.vue';
import NutritionalScanner from '@/components/NutritionalScanner.vue';
import ClinicsPage from '@/components/ClinicsPage.vue';
import NotificationPage from '@/components/NotificationPage.vue';
import MealPlan from '@/components/MealPlan.vue';
import MedicalData from './components/MedicalData.vue';
import SideMenu from './components/SideMenu.vue';
import MealHisory from './components/MealHistory.vue';
import AdminPage from './components/AdminPage.vue';

const routes = [
    { path: '/', component: HomePage },
    { path: '/home', component: HomePage},
    { path: '/register', component: RegisterPage },
    { path: '/login', component: LoginPage },
    { path: '/diabot', component: DiabotPage},
    { path: '/navbar', component: NavBar},
    { path: '/subscriber', component: SubscriberPage},
    { path: '/scanner', component: NutritionalScanner},
    { path: '/clinics', component: ClinicsPage},
    { path: '/notifications', component: NotificationPage},
    { path: '/meal', component: MealPlan},
    { path: '/medical', component: MedicalData},
    { path: '/menu', component: SideMenu},
    { path: '/history', component: MealHisory},
    { path: '/admin', component: AdminPage},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
 
 