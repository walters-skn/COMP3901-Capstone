
<template> 
<div class="page-container">
        <div class="body">
            <h2 class = "title"> New User <br> SIGN UP TO GET STARTED </h2> 
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
                            <button class="btn btn-primary btn-block" @click="signUp" >Sign Up</button>
                        </div> 
    
                    </div>
                </div>
            </div>
        </form>
    <FooterView/>
</div>
</template>
    
<script>
    export default {
        name: 'registerPage',
        methods:{
            handleSubmit(){
                console.log('submitted')
            }
        },
    };

</script>

<style scoped >

    .page-container {
    background-color: #5ca2b1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    }
    
    /* form */
    .form-container{
      background-color: #8eb9c4;
      width: 100%;
      margin: 0 auto;
    }
  
    .form{
      padding: 5px;
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
    }
    
    .submit-group {
        display: flex;
        justify-content: center;
        align-items: center;
    }
  
    .btn{
        border-radius: 2px;
    }
    .btn.btn-primary {
        background-color: #4C8F9E;
        border: 2px solid #f8f0f0;
        color: white;
        font-size: 18px;
        font-family: 'Times New Roman', Times, serif;
    }
  
    </style>