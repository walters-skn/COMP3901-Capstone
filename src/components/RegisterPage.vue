
<template> 
    <NavBar/>
  
    <div class="page-container">
        <div class="body">
            <h2 class = "title"> SIGN UP TO GET STARTED </h2> 
        </div>
            
        <form v-on:submit.prevent="handleRegister">
            <div class = "form-container">
                <div class="box">
                    <div class="form-group">
                        <label> First Name: </label>
                        <input type="text" class="form-control" placeholder="First Name" v-model="fname" required/>
                    </div>
                    <div class="form-group">
                        <label> Last Name: </label>
                        <input type="text" class="form-control" placeholder="Last Name" v-model="lname" required/>
                    </div>
                        
                    <div class="form-group">
                        <label> Email Address: </label>
                        <input type="email" class="form-control" placeholder="Email Address" v-model="email" required/>
                    </div>

                    <div class="form-group">
                        <label> Password: </label>
                        <input type="password" class="form-control" placeholder="Password" v-model="password" required/>
                    </div>
        
                    <div class="form-group">
                        <label> Address 1: </label>
                        <input type="text" class="form-control" placeholder="Address 1"  v-model="address1" required/>
                    </div>

                    <div class="form-group">
                        <label> Address 2: </label>
                        <input type="text" class="form-control" placeholder="Address 2"  v-model="address2"/>
                    </div>
                </div>
            </div>

            <div class="submit-group">
                <button class="btn btn-primary btn-block">Sign Up</button>
            </div> 

        </form>
    </div>
</template>
        
<script>

    import { useRouter } from 'vue-router';
    import axios from 'axios';
    import NavBar from './NavBar.vue';

    export default {
    components:{
        NavBar,
    },
    
    name: 'registerPage',
    created() {
        this.$router = useRouter();
    },
    data() {
        return {
            fname: '',
            lname: '',
            email: '',
            password: '',
            address1: '',
            address2: ''
        };
    },
    methods: {
        handleRegister() {
            axios.post('http://localhost:5000/register', {
                lname: this.lname,
                fname: this.fname,
                email: this.email,
                password: this.password,
                address1: this.address1,
                address2: this.address2
            }).then(() => {
                this.$router.push('/login')
            }).catch((error) => {
                console.log(error)
            })
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
        /* width: 50%; */
        height: 85vh;
        margin-top: 10px;
    }
        
    .form-container{
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding:20px;
        width: 70vh;
        display: flex;
        height: 60vh;
        justify-content: center;
    }
        
    .form-group{
        display: flex;
        flex-direction: column;
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
        width: 20%;
    }

    .form-control{
        padding: 15px;
        width: 100%;
        font-size: 20px;
        font-family: 'Times New Roman', Times, serif;
        border: 1px solid #ccc;
        border-radius: 5px;
        margin-bottom: 10px;
    }

    .btn:hover{
        background-color: #6da6b3;
    }

</style>