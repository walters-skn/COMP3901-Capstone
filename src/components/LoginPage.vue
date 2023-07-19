
<template>
  <NavBar/>

  <div class="page-container">
    <div class="body">
      <h1 class="title"> <strong>LOGIN </strong></h1>
    </div>
      
        <form v-on:submit.prevent="handleLogin">
          <div class = "form-container">

            <div class = "box">

              <div class="form-group">
                <label for="email"> Email Address:</label>
                <input type="email" class="form-control" placeholder="Email Address" v-model="email" required/>
              </div>

              <br>

              <div class="form-group">
                <label for="password"> Password: </label>
                <input type="password" class="form-control" placeholder="Password" v-model="password" required />
              </div>

              <br>

              <div v-if="errorMessage" class="error-message">
                {{ errorMessage }}
              </div>

              <div class="submit-group">
                <button class="btn btn-primary btn-block"> <strong> <b>SIGN IN </b></strong></button>
            </div>
          
          </div>
          </div>
        </form>
    </div>

</template>

<script>

import { useRouter } from 'vue-router';
import axios from 'axios';
import NavBar from './NavBar.vue'


export default {
  components:{
    NavBar,
  },
  name: 'LoginPage',
  created(){
    this.$router = useRouter();
  },
  data(){
    return {
      email: '',
      password: '',
      token: '',
      errorMessage: ''
    };
  },
  methods: {
    handleLogin(){
      axios.post('http://localhost:5000/login', { 
        email: this.email,
        password: this.password
      }).then(response => {
        console.log(response.data)
        this.token = response.data.access_token
        localStorage.setItem('token', this.token)
        this.$router.push('/subscriber')
      }).catch(error => {
        console.log(error)
        this.errorMessage = 'You have entered an incorrect email address or password'
      })
    },
  }
}

</script>

<style scoped >
    
    .page-container {
        background-color: #5ca2b1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        /* width: 50%; */
        height: 83vh;
        margin-top: 20px;
      }
        
    .form-container{
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 90px;
        display: flex;
    }
        
    .form-group{
        display: flex;
        flex-direction: column;
        margin-bottom: 5px;
    }

    .form-group label{
        margin-bottom: 5px;
    }
  
    .box{
        display: flex;
        flex-direction:column ;
        margin-bottom: 10px;
        max-width: 400px;
        width: 400px;
        font-size: 20px;
    }
        
    .title {
        color: white;
        font-family: 'Times New Roman', Times, serif;
        padding: 10px px;
        width: 100%;
        text-align: center;
        font-size: 45px;
        margin-bottom: 10px;
    }

        
    .submit-group {
        display: flex;
        justify-content: center;
        align-items: center;
    }
      
    .btn.btn-primary {
        background-color: #4C8F9E;
        border-radius: 5px;
        padding: 12px 10px;
        color: white;
        font-size: 20px;
        font-family: 'Times New Roman', Times, serif;
        cursor: pointer;
        width: 50%;
    }

    .form-control{
        padding: 10px;
        width: 100%;
        font-size: 20px;
        font-family: 'Times New Roman', Times, serif;
        border: 1px solid #ccc;
        border-radius: 5px;
        margin-bottom: 10px;
    }

    .error-message{
      color:red;
      font-size: 15px;
      text-align: center;
      margin-top:10px
    }

</style>