<template> 

  <div class="nav_container">

    <nav class="navbar">
      <router-link to="/subscriber">
          <img :src="imagePath2" alt="home-logo" class="home">
      </router-link>

      <div class="collapse">
        <ul class="navbar_nav">

          <li class="nav-item">
            <router-link to="/subscriber" class="nav-link"> <strong> Home || </strong></router-link>
          </li>

          <li class="nav-item">
            <router-link to="/login" class="nav-link" v-on:click="logoutPatient"> <strong> Logout </strong></router-link>
          </li>


        </ul>
      </div> 

    </nav> 

  </div>
  
</template>
  
  <script>
  import ImagePath2 from '@/assets/img/logo.png'
  
  export default {
    name: 'SubscriberNavbar',
    data() {
      return {
        imagePath2: ImagePath2,
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
  };

  </script>
  
<style scoped>

.nav_container{
  width: 100%;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 50px;
    background-color: #5CA2B1;
  }

  .navbar_nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    list-style: none;
  }

  .nav-link{
    color: white;
  }

  .home{ 
    height: 65px;
    width: 100px;
    margin: -1%;
  }
        
  .collapse{
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 20px;
    display: flex;
    justify-content: flex-end;
  }

</style>
