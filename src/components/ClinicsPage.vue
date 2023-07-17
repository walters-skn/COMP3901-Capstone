
<template>
    <div>
        <SubscriberNavbar/>

        <h1 class="heading"> <strong> <b> List of Nearby Clinics and Hospitals</b></strong></h1>

        <!-- <div class="filter">
            <label for="parish-select" class="parish"> <strong> Parishes: </strong></label>
            <select id="parish-select" v-model="selectedParish" class="parishselect">
                <option value=""> ALL</option>
                <option v-for="parish in parishes" :value="parish" :key="parish">{{ parish }}</option>
            </select>
        </div> -->
        <div class="filter">
            <label for="address-input" class="address"> <strong> Filter Clinics/Hospitals by Parish </strong></label>
            <input id="address-input" v-model="selectedAddress" class="addressinput" placeholder="Enter your Parish">
        </div>


        <br>

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
                        console.log('getAllHospitals- response:', response);
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
        },
        computed: {
            // filteredHospitals() {
            //     if (!this.selectedParish) {
            //         return this.hospitals;
            //     } else {
            //         return this.hospitals.filter((hospital) => hospital.parish === this.selectedParish);
            //     }
            // },
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

  .parish{
    font-family: times, "Times New Roman";
    font-size: 20px;
  }

  .parishselect{
    padding: 5px;
  }
  
  .heading{
    color: #4C8F9E;
    text-align: center;
  }

  .filter{
    padding: 5px;
    margin-left: 35px;
    font-family: 'Times New Roman', Times, serif;
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
    margin-bottom: 20px;
  }
  
  h3 {
    font-size: 20px;
  }
  
  p {
    margin: 5px 0;
  }
  </style>
  