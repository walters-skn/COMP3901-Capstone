
<template>
    <!-- <NavBar/> -->
  
    <div class="container mt-4">

      <div class="label">
        <h1 class="diabot"> <strong> WELCOME TO <br> DIABOT </strong> </h1>
      <hr>
        <p class="diabot-content">
          Diabot is an innovative solution to address the complexities of diabetes management. While Diabetes is a
          chronic disorder affecting millions of people worldwide, characterized by high blood glucose levels and
          insufficient insulin production, Diabot takes a personalized approach to diabetes care, considering individual
          patient data and medical history to tailor its recommendations and advice.
        </p>
      </div>
      <img :src="imagePath" alt="tools" class="tools">
    </div>

  <div class="guidelines-container">
        <h3 class="guidelines"> <strong> <b>Guidelines For Using Diabot  </b> </strong></h3>
        <p>Before getting started with Diabot, it's important to follow the guidelines. These include:</p>
        <p> Follow the recommended guidelines and suggestions provided by Diabot</p>
        <ul>
          <li>Regularly update your profile and data to ensure accuracy</li>
          <li>Utilize the various features and resources offered by Diabot</li>
          <li>Regularly review and monitor your progress</li>
        </ul>

        <p class="end"> Ready to take control of your diabetes management? </p>
        <br>
        <p class="end"> <strong> Click the button below to get started. </strong> </p>
        
        <button class="btn btn-primary btn-block" @click="goToDiabotPage" >DIABOT</button>

    </div>
  <!-- <FooterView/> -->

</template>

<script>

  // import { useRouter } from 'vue-router';
  import ImagePath from '@/assets/img/tools.png'

  import ImagePath2 from '@/assets/img/logo.png'
  // import FooterView from '@/components/FooterView.vue';
  // import NavBar from '@/components/NavBar.vue';


  export default {
      name:"myApp",
      // components:{
      //     FooterView,
      //     NavBar
      // },
    data(){
      return{
        imagePath: ImagePath,
        imagePath2: ImagePath2,
      };
    }
  }; 
</script>

<style scoped>

  /* {margin: 0; padding: 0 } */
  .container{
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    margin-left: 30px;
  }

  .tools{
    width: 300px;
    height: 400px;
  }

  .end{
    text-align: center;
  }

  .label{
    text-align: center;
    flex-grow:1;
    background-color: white;
    margin: auto 0;
    padding: 5px;
    padding-right: 20px;


  }

  .diabot-content{
    text-align: justify;
    font-size: 23px;
    font-family: Georgia, 'Times New Roman', Times, serif;
  }

  .diabot {
    font-family: 'Times New Roman', Times, serif;
    /* margin-top: 50px;
    padding: 50px; */
    font-size: 55px;
    padding: 2px;
  }

  .guidelines-container{
    background-color: #8ec5d0;
    width: 100%;
    display: flex;
    padding: 30px;
    flex-direction: column;
    align-items: center;
    font-size: 20px;
    font-family: 'Times New Roman', Times, serif;
  }

  .guidelines{
    font-family: 'Times New Roman', Times, serif;
    font-size: 45px;
    color: white;
  }

  .btn {
    display: block;
    width: 100%;
    max-width: 150px;
    margin: 20px auto;
    padding:15px;
    color: white;
    background-color: #5ca2b1;
    border: none;
    cursor: pointer;
  }

  .btn:hover{
    background-color: #21616f;
  }

</style>