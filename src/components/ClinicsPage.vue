
<template>
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
            },
            {
                name: 'Andrews Memorial Seventh-Day Adventist Hospital',
                type: 'Private',
                address: '27 Hope Rd, Kingston',
            },
            {
                name: 'Cornwall Regional Hospital',
                type: 'Public',
                address: 'Montego Bay, St James',
            },
            {
                name: 'Angels Health Care AMDG',
                type: 'Private',
                address: 'Shop 16 Angles Plaza Ang1 Spanish Town St. Catherine',
            },
            {
                name: 'St Jago Park Health Center (SERHA)',
                type: 'Public',
                address: 'Burke Road, Spanish Town St. Catherine',
            },
            {
                name: 'Amadeo Medical Group',
                type: 'Private',
                address: '11A Young St, Spanish Town St. Catherine',
            },
            {
                name: 'Trinity Mall Medical Centre',
                type: 'Private',
                address: '3 Barnett St, Montego Bay',
            },
            {
                name: 'Sekhmet Medical Center',
                type: 'Private',
                address: 'Shop 14, Bogue City Center, Bogue Rd, Montego Bay',
            },
            {
                name: 'Medical Associates',
                type: 'Private',
                address: '18, 10 Tangerine Pl, Kingston',
            },
        ],
      };
    },
  };
  </script>
  
  <style scoped>

  .heading{
    color: #4C8F9E;
    /* justify-items: center; */
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
    width: 60%;
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
  