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
      <p> <strong> It's vital to follow the instructions before using Diabot.</strong>  <br> <strong>These consist of:</strong>
        <ul>
          <li> 1. To maintain accuracy, regularly update your profile and data.</li>
          <li> 2. Utilize the numerous features and resources Diabot has to offer.</li>
          <li> 3. Consistently evaluate and track your development.</li>
        </ul>
      </p>

      <br>

      <p class="end"> Ready to take control of your diabetes management? </p>

      <div class="button-container">
        <p class="end">
          <strong> Click the button below to get started. </strong> 
        </p>
        <router-link to="/diabot" class="btn"> Diabot</router-link>
      </div>

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
    padding-left: 5px;
    padding-right: 5px;
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
    padding-bottom: 90px;
    text-align: center;
    font-size: 20px;
    font-family: 'Times New Roman', Times, serif;
  }

  .guidelines_container ul li{
    display: flex;
    margin-right: 10px;
    justify-content: center;
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
    align-content: center;
    justify-content: center;
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