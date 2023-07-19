<template>

  <NavBar/>

  <div class="container">

    <div class="label">
      <h1 class="diabot"> <strong> WELCOME TO DIABOT </strong> </h1>
      <p class="diabot-content">
        Diabot is an innovative solution to address the complexities of diabetes management. While Diabetes is a
        chronic disorder affecting millions of people worldwide, characterized by high blood glucose levels and
        insufficient insulin production, Diabot takes a personalized approach to diabetes care, considering individual
        patient data and medical history to tailor its recommendations and advice.
      </p>
    </div>
  
  
    <div class="guidelines_container">
      <h3 class="guidelines"> <strong> <b>Guidelines For Using Diabot  </b> </strong></h3>
      <p class="points"> <strong> It's vital to follow the instructions before using Diabot.</strong>  <br> <strong>These consist of:</strong>
        <ul class="points">
          <li> 1. To maintain accuracy, regularly update your profile and data.</li>
          <li> 2. Utilize the numerous features and resources Diabot has to offer.</li>
          <li> 3. Consistently evaluate and track your development.</li>
        </ul>
      </p>

      <p class="points"> <strong> Ready to take control of your diabetes management? </strong></p>

      <div class="button-container">
        <p class="points">
          <strong> Click the button below to get started. </strong> 
        </p>
        <router-link to="/diabot" class="btn"> Diabot</router-link>
      </div>

    </div>
  </div>

</template>

<script>

import NavBar from './NavBar.vue'

export default {
  components:{
    NavBar,
  },
    name:"homePage",
}; 

</script>

<style scoped>

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
    padding: 50px 0;
    text-align: center;

    /* text-align: center; */
    /* margin: 30px 50px;
    padding: 20px; */
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
    font-size: 50px;
    color: white;
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