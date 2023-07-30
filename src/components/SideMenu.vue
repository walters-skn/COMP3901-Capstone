<template>
    <div class="side-menu-container">

        <span class="side"> <strong> <h2> <u> Services </u> </h2> </strong> </span>

        <!-- Diabot Chat -->
        <router-link @click="toggleDropdown('/diabot')" :class="{ 'links': true, 'active': selectedLink === '/diabot' }" to="/diabot">            
            <div class="container">
                <img :src="imagePath" alt="profile" class="img">
                <h3 class="title"> Diabot Chat</h3>
            </div>
        </router-link>

        <!-- Medical Data -->
        <router-link @click="toggleDropdown('/medical')" :class="{ 'links': true, 'active': selectedLink === '/medical' }" to="/medical">            
            <div class="container">
                <img :src="imagePath1" alt="profile" class="img">
                <h3 class="title"> Medical Data</h3>
            </div>
        </router-link>

        <!-- Nearby Clinics -->
        <router-link @click="toggleDropdown('/clinics')" :class="{ 'links': true, 'active': selectedLink === '/clinics' }" to="/clinics">
            <div class="container">
            <img :src="imagePath2" alt="profile" class="img">
            <h3 class="title"> Nearby Health Facilities</h3>
            </div>
        </router-link>

        <!-- Meal Plan -->
        <router-link @click="toggleDropdown('/meal')" :class="{ 'links': true, 'active': selectedLink === '/meal' }" to="/meal">
            <div class="container">
            <img :src="imagePath3" alt="profile" class="img">
            <h3 class="title"> Meal Plan </h3>
            </div>
        </router-link>

        <!-- View Meal History -->
        <router-link @click="toggleDropdown('/history')" :class="{ 'links': true, 'active': selectedLink === '/history' }" to="/history">
            <div class="container">
                <img :src="imagePath4" alt="profile" class="img">
                <h3 class="title"> Meal History </h3>
            </div>
        </router-link>

        <!-- Create Notifications -->
        <router-link @click="toggleDropdown('/notifications')" :class="{ 'links': true, 'active': selectedLink === '/notifications' }" to="/notifications">
            <div class="container">
            <img :src="imagePath5" alt="profile" class="img">
            <h3 class="title"> Create Notifications </h3>
            </div>
        </router-link>

    </div>

</template>

<script>
    import ImagePath from '@/assets/img/chat.png'
    import ImagePath1 from '@/assets/img/profile.png'
    import ImagePath2 from '@/assets/img/location.png'
    import ImagePath3 from '@/assets/img/meal.png'
    import ImagePath4 from '@/assets/img/chat.png'
    import ImagePath5 from '@/assets/img/notify.png'

    export default {
      name: 'SideMenu',
      data() {
        return {
            selectedLink: null,

            imagePath: ImagePath,
            imagePath1: ImagePath1,
            imagePath2: ImagePath2,
            imagePath3: ImagePath3,
            imagePath4: ImagePath4,
            imagePath5: ImagePath5,
    
            showDropdown: false,
            showLogoutDropdown: false,
        };
      },
    methods: {
      toggleDropdown(link){
        this.showDropdown = !this.showDropdown;
        this.selectedLink = link;
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

  .title{
    font-size:18px;
    margin: 0;
  }

  .img{
    width: 35px;
    height: 30px;
    padding-right: 12px;
  }

  .side-menu-container{
    margin-top: 2px;
    display: flex;
    flex-direction: column;
    width: 200px;
    background-color: #5CA2B1;
    height: 86vh;
    overflow-y: auto;
  }  

  .container{
    height: 40px;
    align-items: center;
    display: flex;
    margin-bottom: 10px;
    padding-left: 5px;
  }

  .side{
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 22px;
    color: white;
    margin-bottom: 15px;
    padding-top: 15px;
    align-self: center;
  }

  .links{
    height: 40px;
    color: black;
    text-decoration: none;
    display: flex;
    margin-bottom:15px;
    padding: 8px;
  }

  .links:hover{
    background-color:white;
  }

  .active{
    background-color:white;
  }

</style>
