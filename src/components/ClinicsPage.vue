
<template>

    <div class="main-container">
        <NavBar/>
    </div>
    
    <div class="content-container">
        <SideMenu/>

        <div class="clinic">
            <div class="filter">
                <h1 class="heading"> <strong> <b> List of Health Care Facilities</b></strong></h1>
                <label for="address-input" class="address">  Enter Health Care Facilities You Wish To Locate By Parish </label>
                <input id="address-input" v-model="selectedParish" v-on:input="filterClinic" class="address-input" placeholder="Enter your Parish">
            </div>

            <br>

            <div class="hospital-list-container">
                <div class="hospital-list">
                    <div v-if="filteredClinics.length === 0" class="no-results-message">No results found.</div>
                    <div v-else v-for="clinic in filteredClinics" :key="clinic.name" class="hospital">
                        <div class="details">
                            <h3 class="name" >{{ clinic.name }}</h3>
                            <p><strong>Type:</strong> {{ clinic.type }}</p>
                            <p><strong>Address:</strong> {{ clinic.address }}</p>
                            <p><strong>Parish:</strong> {{ clinic.parish }}</p>
                        </div>
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

                selectedParish: '',
                clinics: []
            };
        },
        methods: {
            getAllClinics() {
                axios.get('http://localhost:5000/clinic')
                    .then((response) => {
                        this.clinics = response.data.clinics;
                        this.filteredClinics = this.clinics;
                    }).catch((error) => {
                        console.log('getAllClinics Error: ', error);
                    })
            },
            filterClinic() {
                this.filteredClinics = this.clinics.filter(clinic => clinic.parish.toLowerCase().includes(this.selectedParish.toLowerCase()));
            },
        },
        computed: {
            filteredClinics() {
                return this.clinics.filter((clinic) => {
                    return clinic.parish.toLowerCase().includes(this.selectedParish.toLowerCase());
                });
            }
        },
        mounted() {
            this.getAllClinics();
        },
        created() {
            isAuthenticated();
            if(!isAuthenticated){
                this.$router.push('/login')
            } else {
                this.token = localStorage.getItem('token');
                setAuthorizationHeader(this.token);
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

    .clinic {
        width: 80vw;
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
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        /* width: 80%;
        max-width: 800px; */
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

    /* .hospital {
        margin: 10px;
        border: 1px solid #ccc;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 10px;
        box-sizing: border-box;
    } */
    
    h3 {
        font-size: 20px;
    }
    
    p {
        margin: 5px 0;
    }

</style>
