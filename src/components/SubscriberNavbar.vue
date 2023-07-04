<template>
    <nav class="navbar navbar-expand navbar-light fixed-top">
      <div class="container">
        <router-link to="/subscriber">
          <img :src="imagePath2" alt="home-logo" class="home">
        </router-link>
  
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <router-link to="/subscriber" class="nav-link"> <strong>Home ||</strong></router-link>
            </li>
            <!-- <li class="nav-item">
              <router-link to='/signout' class="nav-link"><strong>Sign Out </strong></router-link>
            </li> -->
            <SignOut/>
          </ul>
        </div>  
      </div>
    </nav> 
  </template>
  
  <script>
  import ImagePath2 from '@/assets/img/logo.png'
  import SignOut from './SignOut.vue'
  
  export default {
    components:{
        SignOut,
    },
    data() {
      return {
        imagePath2: ImagePath2,
      };
    },
  };
  </script>
  
  <style scoped>
  /* navigation */
  .navbar {
    padding: 10px;
    background-color: #5CA2B1;
  }
  
  .nav-link {
    color: white;
  }
  
  .home {
    height: 65px;
    width: 100px;
    margin: -1%;
  }
  
  .collapse {
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 20px;
    display: flex;
    justify-content: flex-end;
  }
  </style>
  