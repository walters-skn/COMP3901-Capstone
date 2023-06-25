
<template>

    <div id="app">
    <nav class="navbar navbar-expand navbar-light fixed-top">
      <div class="container">
        <a href="#" class="navbar-brand">Logo</a>

        <div class="collapse navbar-collapse">
          <ul class="navbar-nav ml-auto">

            <li class="nav-item">
              <a href="#" class="nav-link">Home ||</a>
            </li>

            <li class="nav-item">
              <a href="#" class="nav-link">About Us ||</a>
            </li>

          </ul>
        </div>
      </div>
    </nav>
    
    <div class="container">
      <div class="label">
        <img :src="imagePath" alt="logo" class="logo">

        <h1>WELCOME TO DIABOT</h1>
        <p>
          Diabot is an innovative solution to address the complexities of diabetes management. While Diabetes is a
          chronic disorder affecting millions of people worldwide, characterized by high blood glucose levels and
          insufficient insulin production, Diabot takes a personalized approach to diabetes care, considering individual
          patient data and medical history to tailor its recommendations and advice.
        </p>

      </div>
      
      <div class="content">
        <h3>Guidelines For Using Diabot</h3>
        <p>Before getting started with Diabot, it's important to follow the guidelines. These include:</p>

        <ul>
          <li>Follow the recommended guidelines and suggestions provided by Diabot</li>
          <li>Regularly update your profile and data to ensure accuracy</li>
          <li>Utilize the various features and resources offered by Diabot</li>
          <li>Regularly review and monitor your progress</li>
        </ul>

        <p>Ready to take control of your diabetes management? Click the button below to get started.</p>
      </div>

      <button class="btn btn-primary btn-block">DIBAOT</button>
    </div>

    <footer></footer>
</div>
</template>

<script>
    export default {
        name: 'HomePage',
        // components:{
        //     NavBar
        // },
        data(){
            return{
                imagePath:ImagePath
            };
        }
    }; 

</script>

<style scoped>
.app {
  padding: 50%;
}

.label {
  text-align: center;
  margin-top: 80px;
}

.h3 {
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}

.p {
  color: black;
}

.btn {
  display: block;
  width: 100%;
  max-width: 200px;
  margin: 20px auto;
  padding: 20px;
  background-color: black;
  color: #5ca2b1;
  border: none;
  cursor: pointer;
}

.tools {
  float: right;
  width: 50%;
  margin: 20px;
}
</style>