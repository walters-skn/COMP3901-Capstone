
<template>

    <div class="main-container">
        <NavBar/>
    </div>
    
    <div class="content-container">
        <SideMenu/>

        <div class="filter">
            <h1 class="heading"> <strong> <b> List of Health Care Facilities</b></strong></h1>
            <label for="address-input" class="address">  Enter Health Care Facilities You Wish To Locate By Parish </label>
            <input id="address-input" v-model="selectedParish" class="address-input" placeholder="Enter your Parish">
        </div>

        <br>

        <div class="hospital-list-container">
            <div class="hospital-list">
                <div v-if="filteredHospitals.length === 0" class="no-results-message">No results found.</div>
                <div v-else v-for="hospital in filteredHospitals" :key="hospital.name" class="hospital">
                    <div class="details">
                        <h3 class="name" >{{ hospital.name }}</h3>
                        <p><strong>Type:</strong> {{ hospital.type }}</p>
                        <p><strong>Address:</strong> {{ hospital.address }}</p>
                        <p><strong>Parish:</strong> {{ hospital.parish }}</p>
                    </div>
                </div>
            </div>
        </div>
                
    </div>
</template>
  
<script>
    import SideMenu from './SideMenu.vue'
    import NavBar from './NavBar.vue'
    import axios from 'axios'
    import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';

    export default {
        components:{
            NavBar,
            SideMenu,
        },
        data() {
            return {
                token: null,
                isAuthenticated: false,

                hospitals: [],
                parishes: [],
                selectedParish: '',
            };
        },
        methods: {
            getAllHospitals() {
                axios.get('http://localhost:5000/clinic')
                    .then((response) => {
                        this.hospitals = response.data.clinics;
                        this.filterByParish();
                    }).catch((error) => {
                        console.log('getAllHospitals Error: ', error);
                    })
            },
            filterByParish() {
                this.filteredHospitals = this.hospitals.filter((hospital) => {
                    if (!this.selectedParish) {
                        return true;
                    } else {
                        const selectedParishLower = this.selectedParish.toLowerCase();
                        const hospitalParishLower = hospital.parish.toLowerCase();
                        return hospitalParishLower.includes(selectedParishLower);
                    }
                })
            }
        },
        created() {
            this.isAuthenticated = isAuthenticated();
            if(!this.isAuthenticated){
                this.$router.push('/login')
            } else {
                this.token = localStorage.getItem('token');
                setAuthorizationHeader(this.token);
            }
        },
        computed: {
            filteredHospitals() {
                return this.hospitals.filter((hospital) => {
                    if (!this.selectedParish) {
                        return true;
                    } else {
                        return hospital.parish === this.selectedParish;
                    }
                })
            },
        },
        mounted() {
            this.getAllHospitals();
        },
        watch: {
            selectedParish() {
                this.filterByParish();
            }
        }
    }
</script>

<style scoped>

    .main-container{
        display: flex;
    }

    .content-container{
        display: inline-flex;
        /* padding-left: 50px;     */
    }

    .address{
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size: 20px;
    }
  
    .heading{
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: #4890a0;
        text-align: center;
        font-size: 40px;
    }

    .filter{
        padding: 5px;
        margin-left: 60px;
        font-family: 'Times New Roman', Times, serif;
        text-align: center;
    }

    .address-input{
        padding: 5px;
        width: 30%;
        height: 2vh;
        border: 3px solid #ccc;
        /* border-radius: 10px; */
    }

    .hospital-list-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    .hospital-list{
        width: 80%;
        max-width: 800px;
    }

    .details{
        padding: 10px;
        border: 5px solid #ccc;
        border-radius: 4px ;
        color: black;
        width: 50%;
    }
    
    .hospital {
        margin-bottom: 20px;
    }
    
    h3 {
        font-size: 20px;
    }
    
    p {
        margin: 5px 0;
    }

</style>
