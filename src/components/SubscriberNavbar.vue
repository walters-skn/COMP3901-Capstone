<template> 

  <div class="nav_container">

    <nav class="navbar">
      <router-link to="/">
          <img :src="imagePath2" alt="home-logo" class="home">
      </router-link>

      <div class="collapse">
        <ul class="navbar_nav">

          <li class="nav-item">
            <router-link to="/" class="nav-link"> <strong> Home </strong></router-link>
          </li>

          <li class="nav-item">
            <router-link to="/login" class="nav-link"> <strong> Logout </strong></router-link>
          </li>

          <SignOut/>
        </ul>
      </div> 

    </nav> 

  </div>
  
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
.nav_container{
  width: 100%;
}

/* navigation */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 50px;
    background-color: #5CA2B1;
  }

  .navbar_nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    list-style: none;
    gap: 8px;
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
    /* width: 100%; */
  }

</style>
