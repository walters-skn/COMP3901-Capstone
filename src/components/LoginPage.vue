
<template>

  <div class="page-container">

    <div class="side-menu">
      <h1> <b><strong> WELCOME <br> TO <br> DIABOT </strong></b></h1>
    </div>

    <div class="content-container">
      <h1 class="title"> <strong>LOGIN </strong></h1>
      
      <form>
        <div class="form-group">
          <label> <b>Email Address</b></label>
          <input type="email" class="form-control" placeholder="Email Address" v-model="email" required/>
        </div>
        <br>
        <div class="loginform-group">
          <label> <b>Password</b></label>
          <input type="password" class="form-control" placeholder="Password" v-model="password" required />
        </div>

        <div class="link-group">
          <a class="link" @click="forgotPassword"> Forgot Password?</a>
        </div>

        <div class="submit-group">
          <button class="btn btn-primary btn-block" @click="login" > <strong> <b>SIGN IN </b></strong></button>
        </div>

      </form>

    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import axios from axios;

export default {
  name: 'LoginPage',
  created(){
    this.$router = useRouter();
  },
  data(){
    return {
      email: '',
      password: '',
      token: ''
    };
  },
  methods: {
    async login(){
      const path ='http://localhost5000/login'
      
      const response = await axios.post(path,{ 
        email: this.email,
        password: this.password

      })
      this.token = response.data.access_token
      console.log(this.token)
      /* 1. store token in local storage */
      /* 2. redirect to subscriber page */

    },
    //   if (this.email === 'user@example.com' && this.password === 'password'){
    //   this.$router.push('/subscriber');
    //   }else {
    //     console.log('Invalid credentials')
    //   }
    // },
    // forgotPassword() {
    //   //Handle create account click
    //   console.log('Forgot password clicked');
    // }
  }
}

</script>

<style>

  .form-control{
      border-radius: 1px solid #000000;
  }

  .side-menu {
    width: 20%;
    padding: 2px;
    background-color: #4C8F9E;
    color: white;
    flex: 0 0 25%;
    position: fixed;
    top: 0; bottom: 0; left: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .page-container {
    display: flex;
    width: 100%;
    margin-top: 6%;
    margin-bottom: 1%;
    margin-left: 0;
    height: 80vh;

  }

  .content-container {
    flex:1;
    width: 50%;
  }
  
  .title {
    text-align: center;
    margin-bottom: 20px;
    color: #4C8F9E;
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 35px;
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
    color: #528995;
    font-size: 15px;
    font-family: 'Times New Roman', Times, serif;
    display: inline-block;
  }

  .btn:hover{
  background-color: #528995;
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
