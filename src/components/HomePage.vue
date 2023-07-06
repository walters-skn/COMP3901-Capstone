<template>

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

      <router-link to="/diabot" class="btn"> Diabot</router-link>
    </div>
  </div>

</template>

<script>

export default {
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
  }

  .end{
    text-align: center;
  }

  .label{
    text-align: center;
    flex-grow:1;
    background-color: white;
    margin: 0 50px;
    align-items: center;
  }

  .diabot-content{
    text-align: justify;
    font-size: 20px;
    font-family: Georgia, 'Times New Roman', Times, serif;
  }

  .diabot {
    font-family: 'Times New Roman', Times, serif;
    font-size: 50px;
  }

  .guidelines_container{
    background-color: #8ec5d0;
    width: 100%;
    text-align: center;
    font-size: 20px;
    font-family: 'Times New Roman', Times, serif;
  }

  .guidelines{
    font-family: 'Times New Roman', Times, serif;
    font-size: 50px;
    color: white;
  }

  .btn {
    display: block;
    width: 100%;
    max-width: 150px;
    padding: 15px;
    color: white;
    background-color: #5ca2b1;
    border: none;
    cursor: pointer;
  }

  .btn:hover{
    background-color: #21616f;
  }

</style>