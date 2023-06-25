
import {createRouter,createWebHashHistory} from 'vue-router';

// import LoginPage from './components/LoginPage.vue'
// // import HomePage from './components/HomePage.vue'
// import RegisterPage from './components/RegisterPage.vue'
// import ProfilePage from './components/ProfilePage.vue'
// import FooterView from './components/FooterView.vue'
// import DiaBot from './components/DiaBot.vue'
// import NavBar from './components/NavBar.vue';
// import NavBar2 from './components/NavBar.vue';

//define route components so that it can be imported from other files
const LoginPage ={template: '<div>LoginPage</div>'}
const RegisterPage ={template: '<div>RegisterPage</div>'}
const FooterView ={template: '<div>FooterView</div>'}
const DiaBot ={template: '<div>DiaBot</div>'}
const NavBar ={template: '<div>NavBar</div>'}
const NavBar2 ={template: '<div>NavBar2</div>'}
const ProfilePage ={template: '<div>ProfilePage</div>'}
const SignOut ={template: '<div>SignOut</div>'}

const routes = [
    // { path: '/', component: HomePage },
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterPage },
    { path: '/profile', component: ProfilePage },
    { path: '/footer', component: FooterView},
    { path: '/diabot', component: DiaBot},
    {path: '/navbar', component: NavBar},
    {path: '/navbar2', component: NavBar2},
    {path: '/signout', component: SignOut}

]
const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router;
 
 