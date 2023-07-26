<template> 

  <div class="nav_container">

    <nav class="navbar">
      <router-link to="/subscriber" class="nav-link">
        <div class="inline">
          <img :src="imagePath2" alt="home-logo" class="home">
          <span class="brand-name"> <strong> DIABOT </strong></span>
        </div>
      </router-link>

      <div class="collapse">

        <ul class="navbar_nav">
          <li class="nav-item" @click="toggleDropdown">
            <span class="nav-link nav-link-hamburger"> &#9776; </span>
            <ul class="dropdown-menu" v-if="showDropdown">
              <li class="nav-item" @mouseenter="showDropdown =true" @mouseleave="showDropdown = false">
                <router-link to="/profile" class="nav-link"> <strong> Profile</strong></router-link>
              </li>

              <li class="nav-item" @mouseenter="showDropdown =true" @mouseleave="showDropdown = false">
                <router-link to="/login" class="nav-link" v-on:click="logoutPatient"> <strong> Logout </strong></router-link>
              </li>
            </ul>
          </li>
          
        </ul>
      </div> 
      
    </nav> 

  </div>
  
</template>
  
<script>
  import ImagePath2 from '@/assets/img/home.png'
  
  export default {
    name: 'SubscriberNavbar',
    data() {
      return {
        imagePath2: ImagePath2,
        showDropdown: false,
        showLogoutDropdown: false,
      };
    },
    methods: {
      toggleDropdown(){
        this.showDropdown = !this.showDropdown;
      },
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
  }

  .nav-link-hamburger{
    font-size:40px;
    cursor: pointer;
  }

  .nav-link-hamburger:hover{
    background-color: #6fabb9;
    border-radius:4px;
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
    text-decoration: none;
  }

  .nav-item{
    position: relative;
  }

  .nav-item:hover{
    background-color: #6fabb9;
  }

  .dropdown-menu{
    position: absolute;
    top: 100%;
    left: 0;
    display: none;
    list-style: none;
    padding: 10px;
    white-space: nowrap;
    background-color: #4e7780;
    border-radius:4px;
  }


  .nav-item:hover .dropdown-menu{
    display: block;
  }

  .home{ 
    height: 70px;
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
