<template> 
  <div class="page-container">
          <nav class="navbar navbar-expand navbar-light fixed-top">
            <div class="container">
              <router-link to="/">
                  <img :src="imagePath2" alt="home-logo" class="home">
              </router-link>

              <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">

                  <li class="nav-item">
                    <router-link to="/" class="nav-link"> <strong> Home ||</strong></router-link>
                  </li>

                  <li class="nav-item">
                    <router-link to='/login' class="nav-link"><strong> Login </strong></router-link>
                  </li>
                </ul>
              </div>  

            </div>
          </nav> 
      <router-view></router-view>

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

<style scoped>

/* navigation */
  .navbar {
    padding: 10px;
    background-color: #5CA2B1;
  }

  .nav-link{
    color: white;
  }

  .home{ 
    height: 65px;
    width: 100px;
    margin: -1%;
  }

  .page-container{
    /* background-color:#5CA2B1; */
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
