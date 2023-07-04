
import {createRouter,createWebHistory} from 'vue-router';

import LoginPage from '@/components/LoginPage.vue'
import HomePage from '@/components/HomePage.vue'
import RegisterPage from '@/components/RegisterPage.vue'
import DiaBot from '@/components/DiaBot.vue'
import NavBar from '@/components/NavBar.vue';
import SubscriberPage from '@/components/SubscriberPage.vue';
import NutritionalScanner from '@/components/NutritionalScanner.vue';
import SubscriberNavbar from '@/components/SubscriberNavbar.vue';
import SignOut from '@/components/SignOut.vue';

const routes = [
    { path: '/', component: HomePage },
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterPage },
    { path: '/diabot', component: DiaBot},
    {path: '/navbar', component: NavBar},
    {path: '/home', component: HomePage},
    {path: '/signout', component: SignOut},
    {path: '/subscriber', component: SubscriberPage},
    {path: '/scanner', component: NutritionalScanner},
    {path: '/snavbar', component: SubscriberNavbar}

]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
 
 