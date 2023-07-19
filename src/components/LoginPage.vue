
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
      token: ''
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
        /* justify-content: center;
        align-items: center; */
        width: 50%;
        height: 100vh;
        margin: 0 auto;
    }
        
    .form-container{
        background-color: #8eb9c4;
        padding: 80px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
        
    .form-group{
        align-items: center;
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
        background-color: #5CA2B1;
        color: white;
        font-family: 'Times New Roman', Times, serif;
        padding-top: 10px;
        text-align: center;
        font-size: 35px;
    }
        
    .submit-group {
        display: flex;
        justify-content: center;
        align-items: center;
    }
      
    .btn.btn-primary {
        background-color: #4C8F9E;
        border: 3px solid #f8f0f0;
        padding: 10px;
        color: white;
        font-size: 20px;
        font-family: 'Times New Roman', Times, serif;
        cursor: pointer;
    }

    .form-control{
        padding: 10px;
        width: 100%;
        font-size: 20px;
        font-family: 'Times New Roman', Times, serif;
    }

</style>