
import {createRouter,createWebHistory} from 'vue-router';

import LoginPage from '@/components/LoginPage.vue'
import HomePage from '@/components/HomePage.vue'
import RegisterPage from '@/components/RegisterPage.vue'
import DiabotPage from '@/components/DiabotPage.vue'
import SubDiabotPage2 from '@/components/SubDiabotPage.vue'
import NavigationBar from '@/components/NavigationBar.vue';
import SubscriberPage from '@/components/SubscriberPage.vue';
import NutritionalScanner from '@/components/NutritionalScanner.vue';
import SubscriberNavbar from '@/components/SubscriberNavbar.vue';
import SignOut from '@/components/SignOut.vue';

const routes = [
    { path: '/', component: HomePage },
    {path: '/home', component: HomePage},
    { path: '/register', component: RegisterPage },
    { path: '/login', component: LoginPage },
    { path: '/diabot', component: DiabotPage},
    { path: '/diabot2', component: SubDiabotPage2},
    {path: '/navbar', component: NavigationBar},
    {path: '/subscriber', component: SubscriberPage},
    {path: '/scanner', component: NutritionalScanner},
    {path: '/snavbar', component: SubscriberNavbar},
    {path: '/signout', component: SignOut}

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
 
 