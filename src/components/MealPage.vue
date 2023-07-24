

<template> 

    <SubscriberNavbar/>

    <form v-on:submit.prevent="saveData" class="meals-container">

        <h2 class="details"> Enter your meal details below:</h2>
        
        <div class="form-group">
            <label>Meal Type: </label>
            <input type="text" v-model="mealType" class="input">
        </div>

        <div class="form-group"> 
            <label>Meal Content: </label>
            <input type="text" v-model="mealCont" class="input">
        </div>

        <div class="form-group">        
            <label>Nutritional Level: </label>
            <input type="text" v-model="nutriLvl" class="input">
        </div>

        <button class="submit"> Submit </button>

    </form>
</template>

<script>

import SubscriberNavbar from './SubscriberNavbar.vue'
import axios from 'axios'
import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';


export default {
    components: {
        SubscriberNavbar,
    },
    data() {
        return {
            token: null,
            isAuthenticated: false,

            mealType: '',
            mealCont: '',
            nutriLvl: ''
        }
    },
    methods: {
        saveData() {
            axios.post('http://localhost:5000/meal', {
                mealType: this.mealType,
                mealCont: this.mealCont,
                nutriLvl: this.nutriLvl
            })
            .then((response) => {
                console.log('saveData response: ', response)
            })
            .catch((error) => {
                console.log('saveData Error: ', error)
            });
        },
    },
    created() {
        this.isAuthenticated = isAuthenticated();
        if(!this.isAuthenticated){
            this.$router.push('/login')
        } else {
            this.token = localStorage.getItem('token');
            setAuthorizationHeader(this.token);
        }
    }
};

</script>

<style scoped>

.meals-container{
    font-family: 'Times New Roman', Times, serif;
    margin: 0 auto;
    padding: 20px;
}

.details{
    font-size: 24px;
    margin-bottom: 20px;
}
.submit{
    background-color: #33717f;
    color: white;
    border: none;
    margin-top: 10px ;
    padding: 8px 16px;
    font-size: 16px;
    width: 10%;
    cursor: pointer;
  }

  .submit:hover{
    background-color: #ccc;
  }

  .input{
    padding: 8px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 50%;
    margin-bottom: 10px;
  }

</style>