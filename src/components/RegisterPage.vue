<template> 

    <h2> Sign Up To Get Started </h2> 

    <form @submit.prevent="handleSubmit">

    <div class="container">
        <div class="box">
            <div class="form-group">
        <label> First Name </label>
        <input type="text" class="form-control" placeholder="Jane" />
    </div>

    <div class="form-group">
        <label> Last Name </label>
        <input type="text" class="form-control" placeholder="Doe" />
    </div>

    <div class="form-group">
        <label> Email Address </label>
        <input type="email" class="form-control" placeholder="Janedoe12345@gmail.com" />
    </div>

    <div class="form-group">
        <label> Password </label>
        <input type="password" class="form-control" placeholder="***********" />
    </div>

    <div class="form-group">
        <label> Re-Enter Password </label>
        <input type="password" class="form-control" />
    </div>

    <button class="btn btn-primary btn-block"> SIGN UP </button>

    </div>
    </div>

</form>

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

<style >

    h2{
        background-color:#5CA2B1;
        color: white;
        font-family: 'Times New Roman', Times, serif;
        text-align: center;
        padding-top: 50px;
    }

    label{
        font-family: Georgia, 'Times New Roman', Times, serif;
        text-align: left;
    }

</style>