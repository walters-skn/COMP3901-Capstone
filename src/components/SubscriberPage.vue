<template> 
  <div class="header"> 
    <SubscriberNavbar/>
    <h2 class="name"> <strong> WELCOME TO DIABOT</strong>  </h2>
  </div>

  <div class="page-layout">
    
    <div class="links">
      <div class="container" >
        <img :src="imagePath" alt="profile" class="img">
        <router-link link to="/diabot">
          <div class="title">
            <strong> Profile </strong>
          </div>
        </router-link>
        <p class="detail"> View Profile Information </p>
      </div>
    </div>

    <div class="links">
      <div class="container" >
        <img :src="imagePath2" alt="profile" class="img">
        <router-link link to="/diabot">
          <div class="title">
            <strong> Medical Data </strong>
          </div>
        </router-link>
        <p class="detail"> Update Your Medical Data </p>
      </div>
    </div>

    <div class="links">
      <div class="container" >
        <img :src="imagePath7" alt="profile" class="img">
        <router-link link to="/diabot">
        <div class="title">
          <strong> <b> Diabot Chat </b> </strong> 
        </div>
        </router-link>
        <p class="detail"> Chat With Diabot </p>
      </div>
    </div>

    <div class="links">
      <div class="container" >
        <img :src="imagePath6" alt="profile" class="img">
        <router-link link to="/diabot">
        <div class="title">
          <strong> <b> View History </b> </strong> 
        </div>
        </router-link>
        <p class="detail"> View Your Chat History</p>
      </div>
    </div>
    
  </div>

  <div class="layout">

    <div class="links">
      <div class="container" >
        <img :src="imagePath3" alt="profile" class="img">
        <router-link link to="/clinics">
          <div class="title">
            <strong> Nearby Clinics </strong>
          </div>
        </router-link>
        <p class="detail">View Nearby Clinics</p>
      </div>
    </div>

    <div class="links">
      <div class="container" >
        <img :src="imagePath5" alt="profile" class="img">
        <router-link link to="/diabot">
          <div class="title">
            <strong> Mean Plan </strong>
          </div>
        </router-link>
        <p class="detail">Suggested Meal Plans</p>
      </div>
    </div>

    <div class="links">
      <div class="container" >
        <img :src="imagePath7" alt="profile" class="img">
        <router-link link to="/scanner">
          <div class="title">
            <strong> Nutritional Scanner </strong>
          </div>
        </router-link>
        <p class="detail">Check Your Meal's Nutritional Value</p>
      </div>
    </div>    

    <div class="links">
      <div class="container" >
        <img :src="imagePath4" alt="profile" class="img">
        <router-link link to="/diabot">
          <div class="title">
            <strong> Create Notifications </strong>
          </div>
        </router-link>
        <p class="detail">Create or View Notifications</p>
      </div>
    </div>

  </div> 
</template>

<script>
  import SubscriberNavbar from './SubscriberNavbar.vue'
  
  import ImagePath from '@/assets/img/profile.png'
  import ImagePath2 from '@/assets/img/profile.png'
  import ImagePath3 from '@/assets/img/location.png'
  import ImagePath4 from '@/assets/img/notify.png'
  import ImagePath5 from '@/assets/img/meal.png'
  import ImagePath6 from '@/assets/img/scan.png'
  import ImagePath7 from '@/assets/img/chat.png'
  
  export default {
    data(){
      return{
        imagePath: ImagePath,
        imagePath2: ImagePath2,
        imagePath3: ImagePath3,
        imagePath4 : ImagePath4,
        imagePath5 : ImagePath5,
        imagePath6 : ImagePath6,
        imagePath7 : ImagePath7
      }
    },
    name:"subscriberPage",
    components:{
      SubscriberNavbar,
    },
  }

</script>
  
<style scoped >

.header{
  margin: 0;
  padding: 5px;
  width: 100%;
  display: inline-block;
  text-align: center;
  justify-content: center;
}

.name{
  font-family: Georgia, 'Times New Roman', Times, serif;
  color: BLACK;
  font-size: 50px;
  margin-top: 20px;
  padding-top: 100px;
}

.img{ 
  height: 85px;
  width: 85px;
}

.container{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  background-color: #5ca2b1;
  padding: 10px;

}

.title{
  font-size:20px;
  font-family: 'Times New Roman', Times, serif;
  color: white;
  text-align: center;
  display: inline-block;
  margin-top: 10px;
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
  padding: 15px;
  display: flex;
  color: white;
}

.page-layout ,
.layout{
  margin-top: 1%;
  /* padding: 25px; */
  display: flex;
  align-items: center;
  justify-content: center;
} 

  </style>