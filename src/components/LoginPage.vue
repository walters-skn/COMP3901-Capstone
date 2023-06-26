<template>
  <!-- <NavBar/> -->

  <div class="page-container">
    <div class="side-menu">
      <h1 class="diabot">WELCOME TO DIABOT</h1>
    </div>

    <div class="content-container">
      <h1 class="title">LOGIN</h1>

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
          <a class="link" @click="forgotPassword">Forget Password?</a>
        </div>

        <div class="submit-group">
          <button class="btn btn-primary btn-block">Sign In</button>
        </div>
      </form>
    </div>
  </div>
  <!-- <FooterView/> -->
</template>

<script>

// import FooterView from '@/components/FooterView.vue';
// import NavBar from '@/components/NavBar.vue';


export default {
  name: 'LoginPage',
  //   components:{
  //       FooterView,
  //       NavBar
  //   },
  methods: {
    forgotPassword() {
      //Handle create account click
      console.log('Forgot password clicked');
    },
  },
};

</script>

<style>

.footer-bottom {
    text-align: center;
    background-color: #d8d8d8;
    padding: 10px 0;
    color: #777777;
  }

.page-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  /* background-color: #5CA2B1; */
}
  
.side-menu {
  position: absolute;
  left: 0;
  margin-top: 11%;
  bottom: 0;
  width: 200px;
  height: 100%;
  padding: 20px;
  background-color: #4C8F9E;
  color: white;
  font-family: 'Times New Roman', Times, serif;
}
  
.content-container {
  flex: 1;
  padding: 20px;
  background-color: white;
  margin-left: 200px;
  position: relative;
}
  
.title {
  text-align: center;
  margin-bottom: 20px;
  background-color: white;
}
  
.form-group {
  margin-bottom: 10px;
}
  
.btn {
  display: block;
  margin-bottom: 10px;
}

.btn.btn-primary {
      background-color: #4C8F9E;
      border: 2px solid #FAE9E9;
      color: white;
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
