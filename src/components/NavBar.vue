<template> 

  <div class="nav_container">

    <nav class="navbar">
      <router-link to="/" class="nav-link" v-if="!loggedIn">
        <div class="inline">
          <img :src="imagePath" alt="home-logo" class="home">
          <span class="brand-name"> <strong> DIABOT </strong></span>
        </div>
      </router-link>

      <router-link to="/subscriber" class="nav-link" v-if="loggedIn">
        <div class="inline">
          <img :src="imagePath" alt="home-logo" class="home">
          <span class="brand-name"> <strong> DIABOT </strong></span>
        </div>
      </router-link>

      <div class="collapse">
        <ul class="navbar_nav">

          <li class="nav-item" v-if="!loggedIn">
            <router-link to="/register" class="nav-link"> <strong> Sign Up </strong></router-link>
          </li>
          <li class="nav-item" v-if="!loggedIn">
            <router-link to="/login" class="nav-link"> <strong> Login </strong></router-link>
          </li>

          <li class="nav-item" v-if="loggedIn">
            <a class="nav-link" v-on:click="logoutPatient"> <strong> Logout </strong></a>
          </li>

        </ul>
      </div> 

    </nav> 
  </div>
  
</template>
  
<script>
  import ImagePath from '@/assets/img/logo.png'
  import { isAuthenticated } from '@/authUtils';
  
  export default {
    name: 'NavBar',
    data() {
      return {
        loggedIn: false,
        imagePath: ImagePath,
      };
    },
    methods: {
      logoutPatient() {
        // remove token from local storage
        localStorage.removeItem('token');
        // redirect to login page
        this.$router.push('/login');
      },
    },
    created() {
      this.loggedIn = isAuthenticated();
    },
  };

  </script>
  
  <style scoped>

  .brand-name{
    font-size:24px;
    color: white;
    margin-left: 10px;
    font-family: Georgia, 'Times New Roman', Times, serif;
    text-decoration: none;
  }

  .inline{
    display: inline-flex;
    align-items: center;
  }

  .nav_container{
    width: 100%;
    height: 30%;
  }

  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 30px;
    background-color: #5CA2B1;
    height: auto;
  }

  .navbar_nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    list-style: none;
  }

  .nav-link{
    color: white;
    text-decoration: none;
    padding: 0 10px;
  }

  .nav-link:hover{
    background-color:#4a7e8a;
  }

  .home{ 
    height: 50px;
    width: 70px;
  }
        
  .collapse{
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 20px;
    display: flex;
    justify-content: flex-end;
  }

</style>
