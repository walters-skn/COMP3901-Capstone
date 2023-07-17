
<template>
    <div>
        <SubscriberNavbar/>

        <h1 class="heading"> <strong> <b> List of Nearby Clinics and Hospitals</b></strong></h1>

        <div class="filter">
            <label for="parish-select"> Parishes:</label>
            <select id="parish-select" v-model="selectedParish">
                <option value=""> ALL</option>
                <option v-for="parish in parishes" :value="parish" :key="parish">{{ parish }}</option>
            </select>
        </div>

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

    export default {
        components:{
            SubscriberNavbar,
        },
        data() {
            return {
                hospitals: [
                    {
                        name: 'Kingston Public Hospital (K.P.H.)',
                        type: 'Public',
                        address: 'North St, Kingston',
                        parish: 'Kingston',

                    },
                    {
                        name: 'Andrews Memorial Seventh-Day Adventist Hospital',
                        type: 'Private',
                        address: '27 Hope Rd, Kingston',
                        parish: 'Kingston',

                    },
                    {
                        name: 'Cornwall Regional Hospital',
                        type: 'Public',
                        address: 'Montego Bay, St James',
                        parish: 'St James',

                    },
                    {
                        name: 'Angels Health Care AMDG',
                        type: 'Private',
                        address: 'Shop 16 Angles Plaza Ang1 Spanish Town St. Catherine',
                        parish: 'St. Catherine',

                    },
                    {
                        name: 'St Jago Park Health Center (SERHA)',
                        type: 'Public',
                        address: 'Burke Road, Spanish Town St. Catherine',
                        parish: 'St. Catherine',

                    },
                    {
                        name: 'Amadeo Medical Group',
                        type: 'Private',
                        address: '11A Young St, Spanish Town St. Catherine',
                        parish: 'St. Catherine',

                    },
                    {
                        name: 'Trinity Mall Medical Centre',
                        type: 'Private',
                        address: '3 Barnett St, Montego Bay',
                        parish: 'Montego Bay',

                    },
                    {
                        name: 'Sekhmet Medical Center',
                        type: 'Private',
                        address: 'Shop 14, Bogue City Center, Bogue Rd, Montego Bay',
                        parish: 'Montego Bay',

                    },
                    {
                        name: 'Medical Associates',
                        type: 'Private',
                        address: '18, 10 Tangerine Pl, Kingston',
                        parish: 'Kingston',
                    },
                ],
                selectedParish: '',
                parishes: [],
            };
        },
        computed: {
            filteredHospitals() {
            if (!this.selectedParish) {
                return this.hospitals;
            } else {
                return this.hospitals.filter((hospital) => hospital.parish === this.selectedParish);
            }
            },
        },
        mounted() {
            this.parishes = Array.from(new Set(this.hospitals.map((hospital) => hospital.parish)));
        },
        methods: {
            filterByParish() {
            this.filteredHospitals = this.selectedParish
                ? this.hospitals.filter((hospital) => hospital.parish === this.selectedParish)
                : this.hospitals;
            },
        },
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
    margin-bottom: 20px;
  }
  
  h3 {
    font-size: 20px;
  }
  
  p {
    margin: 5px 0;
  }
  </style>
  