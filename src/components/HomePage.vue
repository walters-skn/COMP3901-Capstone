<template>

  <NavBar/>

  <div class="container">

    <div class="label">
      <h1 class="diabot"> <strong> WELCOME TO DIABOT </strong> </h1>
      <p class="diabot-content">
        Diabot is an innovative solution to address the complexities of diabetes management. Diabetes is a chronic condition that affects millions of individuals worldwide and is characterised by elevated blood sugar levels and insufficient insulin synthesis.
        <br>
        <br>

        With a personalised approach to diabetes management, Diabot offers recommendations and guidance that are based on patient information, medical history, and preferences. By taking into account unique traits and needs, this personalised approach improves the efficiency of diabetes management.
      </p>
    </div>
    
    <div class="content-container">

      <div class="image-container">
        <img :src="imagePath" alt="risk" class="img">
      </div>

      <div class="guidelines_container">

        <div class="guidelines-content">
          <h3 class="guidelines"> <strong> <b>Guidelines For Using Diabot  </b> </strong></h3>
          <p class="points"> <strong> Before using Diabot, it is vital to follow these instructions carefully.</strong>  <br> <strong>These consist of:</strong>
            <ul class="points">
              <li> 1. Keep Your Profile and Data Updated: To maintain accuracy, regularly update your profile and data.</li>
              <li> 2. Leverage Diabot's Numerous Features: Make the most of the various features and resources Diabot has to offer.</li>
              <li> 3. Consistently Evaluate and Track Your Development: Monitor your development and progress regularly.</li>
            </ul>
          </p>
        </div>
        <br>

        <p class="points"> <strong> Ready to take control of your diabetes management? <br> Click the button below to get started. </strong></p>

        <div class="button-container">
          <router-link to="/diabot" class="btn"> Diabot</router-link>
        </div>
    </div>

    <div class="image-container">
        <img :src="imagePath" alt="risk" class="img">
      </div>

    </div>

  </div>
</template>

<script>

import NavBar from './NavBar.vue'
import ImagePath from '@/assets/img/risk.jpeg'


export default {
  components:{
    NavBar,
  },

  data(){
    return{
      imagePath: ImagePath,
    }
  },
    name:"homePage",
}; 

</script>

<style scoped>

  .img{ 
    height: 64vh;
    width: 100%;
  }

  .content-container{
    display: flex;
    align-items: center;
    justify-content:space-between;
    width: 100%;
  }

  .guidelines-content{
    flex-grow: 1;
  }

  .container{
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex-direction: column;
    width: 100%;
    /* padding: 20px; */
  }

  .label{
    text-align: center;
    background-color: white;
  }

  .diabot-content{
    text-align: justify;
    font-size: 25px;
    font-family: Georgia, 'Times New Roman', Times, serif;
    padding: 0 10% ;
  }

  .diabot {
    font-family: 'Times New Roman', Times, serif;
    font-size: 50px;
    color: #5CA2B1;
  }

  .guidelines_container{
    background-color: #5CA2B1;
    width: 100%;
    padding: 0;
    text-align: center;
  }

  .guidelines_container ul{
    list-style: none;
    padding: 0;
    /* display: flex;
    margin-right: 10px;
    justify-content: center; */
  }

  .guidelines_container ul li{
    margin: 10px 0;
  }

  .guidelines{
    font-family: 'Times New Roman', Times, serif;
    font-size: 30px;
    color: white;
    /* text-align: justify; */
  }

  .points{
    font-family: 'Times New Roman', Times, serif;
    font-size: 25px;
    color: white;
  }

  .btn {
    display: block;
    width: 100%;
    max-width: 150px;
    padding: 15px;
    color: white;
    background-color: #37717e;
    border: none;
    cursor: pointer;
    text-align: center;
    font-family: 'Times New Roman', Times, serif;
    font-size: 25px;
  }

  .btn:hover{
    background-color: #21616f;
  }

  .button-container {
    display: flex;
    flex-direction: column;
    align-items: center
  }

</style>