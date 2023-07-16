<template>
  <div class="signout" @click="signOut">
    <img class="logout" :src="imagePath" alt="logout">
  </div>
  
</template>
  
<script>

import ImagePath from '@/assets/img/logout.png'

  export default {
      data(){
        return{
            imagePath: ImagePath,
          };
      },
    methods: {
      signOut() {
        localStorage.clear();
        // Redirect to the login page
        this.$router.push('/login');
      },
    },
  };
</script>

<style scoped>
  .logout{ 
    height: 40px;
    width: 40px;
    margin: -1%;
    /* transition: transform 0.3s ease-in-out; */
    cursor: pointer;
  }

  .logout:hover{
    transform: scale(1.2)
  }

</style>
  