<template> 
  <div class="page-container">
      <div>
          <nav class="navbar navbar-expand navbar-light fixed-top">
            <div class="container">
                      
              <img :src="imagePath2" alt="home-logo" class="home">

              <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                  <li class="nav-item">
                    <router-link to="/" class="nav-link"><strong>Home ||</strong></router-link>
                    <!-- <a href="./src/components/HomePage.vue" class="nav-link"> <strong> Home || </strong></a> -->
                  </li>
                  <li class="nav-item">
                    <router-link to='/login' class="nav-link"><strong>Login </strong></router-link>
                  </li>
                  <!-- <li class="nav-item">
                    <a href="#" class="nav-link"><strong> Login </strong></a>
                  </li> -->
                </ul>
              </div>  

            </div>
          </nav> 
          <router-view></router-view>
      </div>
    </div>

</template>

<script>
  import ImagePath2 from '@/assets/img/logo.png'

  export default {
      data(){
          return{
              imagePath2: ImagePath2,
          };
      }
  };
</script>

<style scoped >

/* navigation */
  .navbar {
    padding: 5px;
    background-color: #5ca2b1;
  }

  .nav-link{
    color: white;
  }

  .home{ 
    height: 10%;
    width: 100px;
    margin: -1%;
  }

  .body{ 
    padding: 10px;
    margin-bottom: 20px;
  }

  .page-container{
    background-color:#5CA2B1;
    min-height: 5vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
        
  .collapse{
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 20px;
    display: flex;
    justify-content: flex-end;
  }
</style>

