<template>
  <div class="page-container">
    
    <div class="side-menu">
      <h1 class="diabot">WELCOME TO DIABOT</h1>
    </div>

    <div class="content-container">
      <h1 class="title"> <strong>LOGIN </strong></h1>

      <form>
        <div class="form-group">
          <label>Email</label>
          <input type="email" class="form-control" placeholder="Email" />
        </div>

        <div class="loginform-group">
          <label>Password</label>
          <input type="password" class="form-control" placeholder="Password" />
        </div>

        <div class="link-group">
          <a class="link" @click="forgotPassword"> Forgot Password?</a>
        </div>

        <div class="submit-group">
          <button class="btn btn-primary btn-block">Sign In</button>
        </div>

        <router-link to="/register" class="link" > Don't Have An Account? Click Here To Register </router-link>

      </form>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LoginPage',
  methods: {
    forgotPassword() {
      //Handle create account click
      console.log('Forgot password clicked');
    },
  },
};

</script>

<style>

  .form-control{
      border-radius: 1px solid #000000;
  }

  .side-menu {
    position: absolute;
    left: 0;
    width: 20%;
    height: 100vh;
    padding: 50px;
    background-color: #4C8F9E;
    color: white;
    font-family: 'Times New Roman', Times, serif;
    display: flex;
    align-items: center;
  }

  .link{
    color: rgb(163, 41, 41);
  }

  .link :hover{
    color:#d8d8d8;
  }

  .page-container {
    display: flex;
    /* justify-content: center; */
    /* align-items: center; */
    min-height: 100vh;
  }
  
  .content-container {
    flex: 1;
    padding: 90px;
    background-color: white;
    margin-left: 200px;
    position: relative;
  }
  
  .title {
    text-align: center;
    margin-bottom: 20px;
    color: #4C8F9E;
    font-family: Georgia, 'Times New Roman', Times, serif;
  }
  
  .form-group {
    margin-bottom: 10px;
  }
  
  .btn {
  display: block;
  margin-bottom: 10px;
  }

  .btn.btn-primary {
    background-color: white;
    border: 2px solid #2f2c2c;
    color: black;
    font-size: 15px;
    font-family: 'Times New Roman', Times, serif;
  }

  .btn:hover{
  background-color: #21616f;
}

  .link-group {
    text-align: center;
  }
    
  .link {
    margin: 5px;
    color: rgb(168, 29, 29);
    cursor: pointer;
    text-align: left;
  }
    
  .loginform-group {
    margin-bottom: 5px;
  }
    
  .submit-group {
    display: flex;
    justify-content: center;
    align-items: center;
  }
    
  .diabot {
    text-align: center;
    margin: 50px auto 0;
  }

  </style>
