<template> 
  <div class="header"> 
    <SubscriberNavbar/>
    <h2 class="name"> <strong> WELCOME TO DIABOT</strong>  </h2>
  </div>

  <div class="page-container">

    <div class="page-layout">
      
      <div class="links">
        <div class="container" >
          <img :src="imagePath" alt="profile" class="img">
          <router-link link to="/diabot" class="container-link">
          <div class="title">
            <strong> <b> Diabot Chat </b> </strong> 
          </div>
          </router-link>
          <p class="detail"> Chat With Diabot </p>
        </div>
      </div>

      <div class="links">
        <div class="container" >
          <img :src="imagePath1" alt="profile" class="img">
          <router-link link to="/medical" class="container-link">
            <div class="title">
              <strong> Medical Data </strong>
            </div>
          </router-link>
          <p class="detail"> Update Your Medical Data </p>
        </div>
      </div>

      <div class="links">
        <div class="container" >
          <img :src="imagePath2" alt="profile" class="img">
          <router-link link to="/clinics" class="container-link">
            <div class="title">
              <strong> Nearby Health Facilities </strong>
            </div>
          </router-link>
          <p class="detail">View Nearby Health Facilities</p>
        </div>
      </div>
      
    <!-- </div> -->

    <!-- <div class="layout"> -->

      <div class="links">
        <div class="container" >
          <img :src="imagePath3" alt="profile" class="img">
          <router-link link to="/meal" class="container-link">
            <div class="title">
              <strong> Meal Plan </strong>
            </div>
          </router-link>
          <p class="detail">Recommended Meal Plans</p>
        </div>
      </div>

      <div class="links">
        <div class="container" >
          <img :src="imagePath4" alt="profile" class="img">
          <router-link link to="/subscriber" class="container-link">
          <div class="title">
            <strong> <b> Meal History </b> </strong> 
          </div>
          </router-link>
          <p class="detail"> View Your Meal History</p>
        </div>
      </div>

      <!-- <div class="links">
        <div class="container" >
          <img :src="imagePath7" alt="profile" class="img">
          <router-link link to="/subscriber">
            <div class="title">
              <strong> Nutritional Scanner </strong>
            </div>
          </router-link>
          <p class="detail">Check Your Meal's Nutritional Value</p>
        </div>
      </div>     -->

      <div class="links">
        <div class="container" >
          <img :src="imagePath5" alt="profile" class="img">
          <router-link link to="/notifications" class="container-link">
            <div class="title">
              <strong> Create Notifications </strong>
            </div>
          </router-link>
          <p class="detail">Create or View Notifications</p>
        </div>
      </div>

    </div> 

  </div>
    
</template>

<script>
  import SubscriberNavbar from './SubscriberNavbar.vue'
  // import { isAuthenticated, setAuthorizationHeader } from '@/authUtils'

  import ImagePath from '@/assets/img/chat.png'
  import ImagePath1 from '@/assets/img/profile.png'
  import ImagePath2 from '@/assets/img/location.png'
  import ImagePath3 from '@/assets/img/meal.png'
  import ImagePath4 from '@/assets/img/scan.png'
  import ImagePath5 from '@/assets/img/notify.png'
  
  export default {
    data(){
      return{
        token: null,
        isAuthenticated: false,

        imagePath: ImagePath,
        imagePath1: ImagePath1,
        imagePath2: ImagePath2,
        imagePath3: ImagePath3,
        imagePath4: ImagePath4,
        imagePath5: ImagePath5,
      }
    },
    name:"subscriberPage",
    components:{
      SubscriberNavbar,
    }
    // ,
    // created() {
    //   this.isAuthenticated = isAuthenticated();
    //   if(!this.isAuthenticated){
    //     this.$router.push('/login')
    //   } else {
    //     this.token = localStorage.getItem('token');
    //     setAuthorizationHeader(this.token);
    //   }
    // }
  }

</script>
  
<style scoped >

  .container-link{
    text-decoration:none;
    color: inherit;
  }

  .header{
    width: 100%;
    display: inline-block;
    text-align: center;
  }

  .name{
    font-family: Georgia, 'Times New Roman', Times, serif;
    color: #5CA2B1;
    font-size: 50px;
    margin-top: 2px;
    padding-top: 8px ;
  }

  .img{ 
    height: 95px;
    width: 110px;
  }

  .page-container{
    padding: 20px;
    border-radius: 10px ;
    background-color: #5ca2b1;
    align-items: center;
  }

  .container{
    padding: 20px;
    border-radius: 10px ;
    background-color: #5ca2b1;
  }

  .title{
    font-size:20px;
    font-family: 'Times New Roman', Times, serif;
    color: white;
    margin-top: 5px;
    border-radius: 8px;
    padding: 8px 12px;
  }

  .title:hover{
    background-color: #1c606f ;
  }

  .detail{
    margin-top: 12px;
    font-size:20px;
    font-family: 'Times New Roman', Times, serif;
    color: #143e47;
  }

  .links{
    display: flex;
    flex: 1;
    flex-direction: column;
    align-items: center;
  }

  .page-layout ,
  .layout{
    display: flex;
    justify-content: center;
  } 

  </style>