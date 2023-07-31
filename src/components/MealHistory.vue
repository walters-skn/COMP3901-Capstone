
<template>

    <div class="main-container">
        <NavBar/>
    </div>
    
    <div class="content-container">
        <SideMenu/>

        <div class="filter">
            <h1 class="heading"> <strong> <b> User Medical Records</b></strong></h1>

            <div class="table-container"> 
                <table> 
                    <thead>
                        <tr>
                            <th> Patient ID</th>
                            <th> Meal Type</th>
                            <th> Meal Content</th>
                            <th> Nutritional Level</th>
                            <th> Meal Date</th>
                            <th> Meal Time</th>
                            
                        </tr>
                    </thead>
        
                    <tbody>
                        <tr v-for="meal in meals" :key="meal">
                            <td> {{ meal.patient_id}}</td>
                            <td> {{ meal.meal_type }}</td>
                            <td> {{ meal.meal_cont }}</td>
                            <td> {{ meal.nutri_lvl}}</td>
                            <td> {{ meal.meal_date }}</td>
                            <td> {{ meal.meal_time  }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
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
            patient_id: '',
            meal_type: '',
            meal_cont: '',
            nutri_lvl: '',
            meal_date: '',
            meal_time: '',
        };
    },
    methods: {
        getMeal() {
            axios.get('http://localhost:5000/history')
                .then((response) => {
                    this.meals = response.data.meals;
                    console.log('getMeal response:', response);
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

        this.getMeal();
    }
}
</script>

<style scoped>

    .main-container{
        display: flex;
    }

    .content-container{
        display: inline-flex;
    }
  
    .heading{
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: #4890a0;
        font-size: 40px;
    }

    .filter{
        padding: 5px;
        margin-left: 60px;
        font-family: 'Times New Roman', Times, serif;
        text-align: center;
        display:flex;
        flex-direction: column;
        align-items: center;
    }
    
    .table-container{
        overflow-x: auto;
    }

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

</style>
