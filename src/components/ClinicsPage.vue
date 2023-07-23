
<template>
    <div>
        <SubscriberNavbar/>

        <h1 class="heading"> <strong> <b> List of Nearby Clinics and Hospitals</b></strong></h1>

        <div class="filter">
            <label for="address-input" class="address"> <strong> Enter Health Care Facilities By Parish</strong></label>
            <input id="address-input" v-model="selectedAddress" class="addressinput" placeholder="Enter your Parish">
        </div>

        <br>

        <div class="hospital-list-container">
            <div class="hospital-list">
                <div v-for="hospital in filteredHospitals" :key="hospital.name" class="hospital">
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

    import SubscriberNavbar from './SubscriberNavbar.vue'
    import axios from 'axios'
    import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';

    export default {
        components:{
            SubscriberNavbar,
        },
        data() {
            return {
                token: null,
                isAuthenticated: false,

                hospitals: [],
                parishes: [],
                selectedParish: '',
                selectedAddress: '',
            };
        },
        methods: {
            getAllHospitals() {
                axios.get('http://localhost:5000/clinic')
                    .then((response) => {
                        this.hospitals = response.data.clinics;
                    }).catch((error) => {
                        console.log('getAllHospitals- error:', error);
                    })
            },
            filterByParish() {
            this.filteredHospitals = this.selectedParish
                ? this.hospitals.filter((hospital) => hospital.parish === this.selectedParish)
                : this.hospitals;
            }
        },
        created() {
            this.getAllHospitals();
            this.filterByParish();

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
                if (!this.selectedAddress) {
                    return this.hospitals;
                } else {
                    const selectedAddressLower = this.selectedAddress.toLowerCase();
                    return this.hospitals.filter((hospital) =>
                        hospital.address.toLowerCase().includes(selectedAddressLower)
                    );
                }
            },
        },
        mounted() {
            this.parishes = Array.from(new Set(this.hospitals.map((hospital) => hospital.parish)));
        }
    }
</script>

<style scoped>

    .address{
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size: 24px;
    }
  
    .heading{
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: #4890a0;
        text-align: center;
        font-size: 40px;
    }

    .filter{
        padding: 5px;
        margin-left: 35px;
        font-family: 'Times New Roman', Times, serif;
        text-align: center;

    }

    .addressinput{
        padding: 5px;
        width: 10%;
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
        /* background-color: #6b7578; */
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
