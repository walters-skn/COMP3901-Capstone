<template> 
<div class="page-container">

    <!-- <title> Registration Page </title> -->
    <h2 class = "title"> SIGN UP TO GET STARTED </h2> 

        <form @submit.prevent="handleSubmit">

        <div class="container">
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

            <div class="form-group">
                <label> Password: </label>
                <input type="password" class="form-control" />
            </div>

            <div class="form-group">
                <label> Re-Enter Password: </label>
                <input type="password" class="form-control" />
            </div>

        <button class="btn btn-primary btn-block"> SIGN UP </button>

        </div>
        </div>
    </form>
</div>

</template>

<script>
    export default {
        name: 'RegisterPage',
        methods:{
            handleSubmit(){
                console.log('submitted')
            }
        }
    }
    
</script>

<style scoped >

    .page-container{
        background-color:#5CA2B1;
        min-height: 100vh;
        /* display: flex;
        justify-content: center;
        align-items: center; */
    }

    .container{
        width: 400px;   
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #5CA2B1;
        /* display: flex; */
        /* justify-content: center;
        align-items: center;
        height: 100vh; */
    }

    .title {
        background-color: #5CA2B1;
        color: white;
        font-family: 'Times New Roman', Times, serif;
        text-align: center;
        padding-top: 50px;
        margin-bottom: 10px;
    }

    .box{
        width: 400px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #ACC5CB;
    }

    h2{
        background-color:#5CA2B1;
        color: white;
        font-family:  monospace;
        text-align: center;
        padding-top: 50px;
    }

    label{
        font-family: Georgia, 'Times New Roman', Times, serif;
        text-align: left;
    }

    .btn{
        display: flex;
        justify-content:center;
        align-items:center;
        background-color: #4C8F9E;
        border: 2px solid #FAE9E9;
        color: white;
        text-align: center;
        font-size: 15px;
        border-radius: 5px;
        font-family: 'Times New Roman', Times, serif;
        width: 120px;
        height: 30px;
    }

    .button-wrapper{
        display: flex;
        justify-content: center;
    }

    .form-group{
        margin-bottom: 10px;
    }

    .submit-group{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

</style>