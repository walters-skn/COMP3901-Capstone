<template> 

  <div class="nav_container">

    <nav class="navbar">
      <router-link to="/">
          <img :src="imagePath2" alt="home-logo" class="home">
      </router-link>

      <div class="collapse">
        <ul class="navbar_nav">

          <li class="nav-item">
            <router-link to="/register" class="nav-link"> <strong> Sign Up ||</strong></router-link>
          </li>
          <li class="nav-item">
            <router-link to="/login" class="nav-link"> <strong> Login </strong></router-link>
          </li>

        </ul>
      </div> 

    </nav> 
  </div>
  
</template>
  
<script>
  import ImagePath2 from '@/assets/img/logo.png'
  
  export default {
    name: 'NavBar',
    data() {
      return {
        imagePath2: ImagePath2,
      };
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
    height: 75px;
    width: 90px;
    margin: -1%;
  }
        
  .collapse{
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 20px;
    display: flex;
    justify-content: flex-end;
  }

</style>
