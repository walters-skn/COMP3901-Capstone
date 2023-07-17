
<template>
    <div>
        <SubscriberNavbar/>

        <h1 class="heading"> <strong> <b> List of Nearby Clinics and Hospitals</b></strong></h1>

        <div class="hospital-list">
            <div v-for="hospital in hospitals" :key="hospital.name" class="hospital">
                <div class="details">
                    <h3 class="name" >{{ hospital.name }}</h3>
                    <p><strong>Type:</strong> {{ hospital.type }}</p>
                    <p><strong>Address:</strong> {{ hospital.address }}</p>
                </div>
            </div>
        </div>
    </div>
  </template>
  
  <script>

    import SubscriberNavbar from './SubscriberNavbar.vue'
    import axios from 'axios'

    export default {
        components:{
            SubscriberNavbar,
        },
        data() {
            return {
                hospitals: []
            };
        },
        methods: {
            getAllHospitals() {
                axios.get('http://localhost:5000/clinic')
                    .then((response) => {
                        console.log('getAllHospitals- response:', response);
                        this.hospitals = response.data.clinics;
                    }).catch((error) => {
                        console.log('getAllHospitals- error:', error);
                    })
            }
        },
        created() {
            this.getAllHospitals();
        }
    };
     
  </script>
  
  <style scoped>
  .heading{
    color: #4C8F9E;
    text-align: center;
  }
  .hospital-list {
    padding-left: 30px;
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
    /* Add hospital item styles here */
    margin-bottom: 20px;
  }
  
  h3 {
    /* Add hospital name styles here */
    font-size: 20px;
  }
  
  p {
    /* Add hospital details styles here */
    margin: 5px 0;
  }
  </style>
  