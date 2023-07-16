
<template> 
    <NavBar/>
  
    <div class="page-container">
        <div class="body">
            <h2 class = "title"> New User <br> SIGN UP TO GET STARTED </h2> 
        </div>
                
        <form @submit.prevent="handleSubmit">
            <div class = "form-container">
                <div class="box">
                    <div class="form-group">
                        <label> First Name: </label>
                        <input type="text" class="form-control" v-model="fname" required/>
                    </div>
                <br>
                <div class="form-group">
                    <label> Last Name: </label>
                        <input type="text" class="form-control" v-model="lname" required/>
                </div>
                <br>
                <div class="form-group">
                    <label> Email Address: </label>
                        <input type="email" class="form-control" v-model="email" required/>
                </div>
                <br>

                <div class="form-group">
                    <label> Password: </label>
                    <input type="password" class="form-control" v-model="password" required/>
                </div>
                <br>
                <div class="form-group">
                    <label> Address 1: </label>
                    <input type="text" class="form-control" v-model="addrees1" required/>
                </div>
                <br>
                <div class="form-group">
                    <label> Address 2: </label>
                    <input type="text" class="form-control" v-model="address2" required/>
                </div>
                <br>
                                
                <div class="submit-group">
                    <button class="btn btn-primary btn-block" @click="signUp"> <strong> Sign Up</strong></button>
                </div> 
            
                </div>
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
    created(){
        this.$router = useRouter();
    },

    data(){
        return {
            lname: '',
            fname: '',
            email: '',
            password: '',
            address1: '',
            address2: ''
        };
    },
    
    methods:{
        signUp(){
            axios.post('http://localhost:5000/register', {
                lname: this.lname,
                fname: this.fname,
                email: this.email,
                password: this.password,
                address1: this.address1,
                address2: this.address2
            }).then((response) => {
                console.log("signUp Information: ", response)
                this.$router.push('/login')
            }).catch((error) => {
                console.log(error)
            })
        },
        handleSubmit(){
            console.log(' Form submitted')
        }
    },
};
    
</script>
    
<style scoped >
    
    .page-container {
        background-color: #5ca2b1;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
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
        font-size: 25px;
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