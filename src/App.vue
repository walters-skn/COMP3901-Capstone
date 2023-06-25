
<template>

    <div id="app">
      <nav class="navbar navbar-expand navbar-light fixed-top">
        <div class="container">
          <img :src="imagePath2" alt="home-logo" class="home">
  
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item">
                <a href="./src/components/HomePage.vue" class="nav-link"> <strong> Home || </strong></a>
              </li>
              <li class="nav-item">
                <a href="#" class="nav-link"><strong> About Us </strong></a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    
      <div class="container mt-4">
          <div class="label">
          <h1 class="diabot"> <strong> WELCOME TO DIABOT </strong> </h1>
          <p class="diabot-content">
            Diabot is an innovative solution to address the complexities of diabetes management. While Diabetes is a
            chronic disorder affecting millions of people worldwide, characterized by high blood glucose levels and
            insufficient insulin production, Diabot takes a personalized approach to diabetes care, considering individual
            patient data and medical history to tailor its recommendations and advice.
          </p>
        </div>
        <!-- <img :src="imagePath" alt="tools" class="tools"> -->
      </div>
  
    <div class="guidelines-container">
          <h3 class="guidelines"> <b>Guidelines For Using Diabot </b></h3>
          <p>Before getting started with Diabot, it's important to follow the guidelines. These include:</p>
          <p> Follow the recommended guidelines and suggestions provided by Diabot</p>
          <ul>
            <li>Regularly update your profile and data to ensure accuracy</li>
            <li>Utilize the various features and resources offered by Diabot</li>
            <li>Regularly review and monitor your progress</li>
          </ul>
  
          <p class="end"> Ready to take control of your diabetes management? </p>
          <p class="end"> <strong> Click the button below to get started. </strong> </p>
          
          <button class="btn btn-primary btn-block" @click="goToDiabotPage" >DIABOT</button>
  
        </div>
      </div>
    <div class="footer-bottom">
      <p>&copy; 2023 Your Website. All rights reserved.</p>
    </div>
  
  </template>
  
  <script>
  
    // import { useRouter } from 'vue-router';
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
  
    .footer-bottom {
        text-align: center;
        background-color: #d8d8d8;
        padding: 10px 0;
        color: #777777;
      }
  
    /* logo */
    .home{ 
      height: 10%;
      width: 100px;
      margin: -1%;
    }
  
  /* navigation bar */
    .navbar {
      padding: 5px;
      background-color: #5ca2b1;
    }
  
    /* navigation link */
    .nav-link{
      color: white;
    }
  
      /* position to the right */
    .collapse{
      font-family: Georgia, 'Times New Roman', Times, serif;
      font-size: 20px;
      display: flex;
      justify-content: flex-end;
    }
  
    .end{
      text-align: center;
    }
  
    .label{
      text-align: center;
      margin-top: 80px;
      flex:1;
    }
  
    .diabot-content{
      text-align: justify;
      font-size: 23px;
      font-family: 'Times New Roman', Times, serif;
    }
  
    .diabot {
      font-family: fantasy;
      margin-top: 80px;
      padding: 50px;
      font-size: 50px;
    }
  
    .guidelines-container{
      flex: 1;
      background-color: #8ec5d0;
      padding: 50px;
      display: flex;
      flex-direction: column;
      align-items: center;
      font-size: 20px;
      font-family: 'Times New Roman', Times, serif;
    }
  
    .guidelines{
      font-family: fantasy;
      font-size: 45px;
      margin-bottom: 0px;
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