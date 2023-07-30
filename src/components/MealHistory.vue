
<template>

    <div class="main-container">
        <NavBar/>
    </div>

    <h2> Meal History</h2>
    <router-link to="/login" v-on:click="logoutAdmin">Logout</router-link>
    <table>
        <thead>
            <tr>
                <th> Meal ID</th>
                <th> Patient ID</th>
                <th> Recommended ID</th>
                <th> Meal Type</th>
                <th> Meal Content</th>
                <th> Picture of Meal</th>
                <th> Nutritional LEvel</th>
                <th> Meal Date</th>
                <th> Meal Time</th>
                
            </tr>
        </thead>

        <tbody>
            <tr v-for="meal in meals" :key="meal">
                <td> {{ meal.meal_id }}</td>
                <td> {{ meal.patient_id}}</td>
                <td> {{ meal.recommend_id }}</td>
                <td> {{ meal.meal_type }}</td>
                <td> {{ meal.meal_cont }}</td>
                <td> {{ meal.meal_pic }}</td>
                <td> {{ meal.nutri_lvl}}</td>
                <td> {{ meal.meal_date }}</td>
                <td> {{ meal.meal_time  }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>

import axios from 'axios';
import SideMenu from './SideMenu.vue'
import NavBar from './NavBar.vue'

import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';

export default{
    components:{
        NavBar,
        SideMenu,
    },
    data(){
        return{
            token: null,
            isAuthenticated: false,

            meals: [],
            meal_id: '',
            patient_id: '',
            recommend_id: '',
            meal_type: '',
            meal_cont: '',
            meal_pic: '',
            nutri_lvl: '',
            meal_date: '',
            meal_time: '',
        };
    },
    methods: {
        getMeal(){
            axios.get('http://localhost:5000/meal', {
                headers: {
                    Authorization: `Bearer ${this.token}`,
                },
            })
            .then((response) => {
                this.meals = response.data.meals;
                // console.log('getMeal response:', this.meals);
            })
            .catch((error) => {
                if (error.response && error.response.status === 401) {
                // Unauthorized access, redirect to login page or show an error message
                this.$router.push('/login');
                } else {
                console.log('getProfile error:', error);
                }
            });
        },
        logoutAdmin() {
            // remove token from local storage
            localStorage.removeItem('token');
            // redirect to login page
            this.$router.push('/login');
        },
    },
    created(){
        this.isAuthenticated = isAuthenticated();
        if(!this.isAuthenticated){
            this.$router.push('/login')
        } else {
            this.token = localStorage.getItem('token');
            setAuthorizationHeader(this.token);
        }
        
        this.getProfile();
    }
}
</script>

<style scoped>

    table{
        width: 100%;
        border-collapse: collapse;
        border: 3px solid #ccc;
        margin-top: 10px;
    }

    th,
    td{
        padding: 8px 12px;
        text-align: center;
        border-bottom: 1px solid #ccc;
    }

    th{
        background-color: #5CA2B1;
    }

    tbody tr:nth-child(even){
        background-color: #f2f2f2;
    }

    h2{
        margin-bottom: 20px;
        text-align: center;
        padding: 10px;
    }

</style>
