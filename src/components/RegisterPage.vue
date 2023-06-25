
<template> 
    <div class="page-container">
        <div>
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
        </div>

        <div class="body">
            <h2 class = "title"> New User? <br> SIGN UP TO GET STARTED </h2> 
        </div>
        
        <form @submit.prevent="handleSubmit">
            <div class = "form-container">
                <div class="form">
                    <div class="box">
                        <div class="form-group">
                            <label> First Name: </label>
                            <input type="text" class="form-control" />
                        </div>
                        
                        <div class="form-group">
                            <label> Last Name: </label>
                            <input type="text" class="form-control" />
                        </div>
                        
                        <div class="form-group">
                            <label> Email Address: </label>
                            <input type="email" class="form-control" />
                        </div>
        
                        <div class="form-group">
                            <label> Telephone Number: </label>
                            <input type="tel" class="form-control" />
                        </div>
            
                        <div class="form-group form-inline">
                            <label> Password: </label>
                            <input type="password" />
                            
                            <div class="form-group">
                                <label> Re-Enter Password: </label>
                                <input type="password" />
                            </div>
                        </div>
                        
                        <div class="submit-group">
                            <button class="btn btn-primary btn-block" @click="signUp" >Sign In</button>
                        </div> 
    
                    </div>
                </div>
            </div>
        </form>
    </div>  
    <div class="footer-bottom">
        <p>&copy; 2023 Your Website. All rights reserved.</p>
    </div>
</template>
    
<script>
  
    import ImagePath2 from '@/assets/img/logo.png'
    
    export default {
        name: 'RegisterPage',
        methods:{
            handleSubmit(){
                console.log('submitted')
            }
        },
        data(){
            return{
                imagePath2: ImagePath2,
            };
        }
    };

</script>

<style scoped >

    .footer-bottom {
        text-align: center;
        background-color: #d8d8d8;
        padding: 10px 0;
        color: #777777;
    }

  /* navigation */
    .navbar {
      padding: 5px;
      background-color: #5ca2b1;
    }
  
    .nav-link{
      color: white;
    }
  
    .home{ 
      height: 10%;
      width: 100px;
      margin: -1%;
    }
  
    .body{ 
      padding: 10px;
      margin-bottom: 20px;
    }
  
    .page-container{
      background-color:#5CA2B1;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
          
    .collapse{
      font-family: Georgia, 'Times New Roman', Times, serif;
      font-size: 20px;
      display: flex;
      justify-content: flex-end;
    }

    /* form */
    .form-container{
      background-color: #ACC5CB;
      margin: auto;
      margin-right: auto;
    }
  
    .form{
      padding: 10px;
      border: 5px solid #ccc;
      border-radius: 5px;
      width: 100%;
    }
    
    .form-group{
      margin-bottom: 10px;
      align-items: center;
    }
  
    .form-inline{
      display: flex;
      align-items: center;
    }
    
    .title {
        background-color: #5CA2B1;
        color: white;
        font-family: 'Times New Roman', Times, serif;
        text-align: center;
        padding-top: 50px;
        margin-top: 50px;
    }
    
    .box{
        width: 100%;
        background-color: #ACC5CB;
    }
    
    .submit-group {
        display: flex;
        justify-content: center;
        align-items: center;
    }
  
    .btn.btn-primary {
        background-color: #4C8F9E;
        border: 2px solid #FAE9E9;
        color: white;
        font-size: 15px;
        font-family: 'Times New Roman', Times, serif;
    }
  
    </style>