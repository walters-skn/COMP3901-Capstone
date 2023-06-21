<template>
  <div id ="app">

    <!-- <NavBar/> -->
    <!-- <LoginPage/> -->
    <!-- <HomePage/> -->
    <RegisterPage/>

    <div class="auth-wrapper">
      <div class ="auth-inner">
        <router-view />
      </div>
    </div>

  </div>
</template>

<script>

// import NavBar from './components/NavBar.vue'
// import HomePage from './components/HomePage.vue'
// import LoginPage from './components/LoginPage.vue'
import RegisterPage from './components/RegisterPage.vue';

export default{
  name: 'App',
  components:{
    // NavBar
    // HomePage,
    // LoginPage
    RegisterPage
  }
}
</script>


<!-- <style>

  /* @import url("https://jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"); */
  
  *{
    box-sizing: border-box;
  }

  h1,h2,h3,h4,h5,h6, label,span{
    font-weight: 500;
    font-family: sans-serif;
  }

  body{
    background-color: #1c8ef9;
    min-height: 100vh;
    display: flex;
    font-weight: 400;
    font-family: sans-serif;
  }

  body,html,#app, #root, .auth.wrapper{
    width: 100%;
    height: 100%;
  }
  
  #app {
    font-family: Arial, Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color:#5CA2B1;
    margin-top: 60px;
  }

  .navbar-light{
    background-color: #ffffff;
    box-shadow: 0px 14px 80ox rgba(34, 35, 58, 092);
  }

  .auth-wrapper{
    display: flex;
    justify-content: center;
    flex-direction: column;
    text-align: left;
  }

  .auth-inner{
    width: 450px;
    margin:auto;
    background: #ffffff;
    box-shadow: 0px 14px 80ox tgba(34, 35, 58, 0.2);
    padding: 40px 55px 45px 55px;
    border-radius:15px;
    transition: all 0.3s;
  }

  .auth-wrapper .form-control:focus{
    border-color: #167bff;
    box-shadow: none;
  }

  .auth-wrapper h3{
    text-align: center;
    margin-top: 0;
    line-height: 1;
    padding-bottom: 20px;
  }

  .custom-control-label{
    font-weight: 400;
  }

  .forgot-password a{
    text-align: right;
    font-size: 13px;
    padding-top: 10px;  
    color: #7f7d7d;
    margin: 0;
  }

  .forgot-password a{
    color: #167bff;
  }

</style> -->
