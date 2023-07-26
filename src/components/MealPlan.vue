
<template> 

    <div class="main-container">
        <SubscriberNavbar/>
    </div>

    <div class="content-container">
        <SideMenu/>

        <div class="filter">
            <h1 class="heading"> <strong> Diabetes Management Diet</strong></h1>

            <label class="risk" ><strong>Select Risk Category</strong></label>
            <select v-model="selectedReminder" class="risk-category">
            <option disabled value=""> Please select one</option>
            <option value="medication"> Low to Moderate </option>
            <option value="appointment"> High Risk </option>
            <option value="appointment"> Very High Risk </option>
            </select>

            
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

                <!-- <div class="form-group">        
                    <label>Nutritional Level: </label>
                    <input type="text" v-model="nutriLvl" class="input">
                </div> -->

                <button class="submit"> Submit </button>
            </form>
    </div>

    </div>
</template>

<script>

import SubscriberNavbar from './SubscriberNavbar.vue'
import SideMenu from './SideMenu.vue'
import axios from 'axios'
// import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';


export default {
    components: {
        SubscriberNavbar,
        SideMenu,
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
    }
    // ,
    // created() {
    //     this.isAuthenticated = isAuthenticated();
    //     if(!this.isAuthenticated){
    //         this.$router.push('/login')
    //     } else {
    //         this.token = localStorage.getItem('token');
    //         setAuthorizationHeader(this.token);
    //     }
    // }
};

</script>

<style scoped>

    .risk-category {
        padding: 8px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
        width: 50%;
        margin-bottom: 5%;
    }

    .risk{
        color: #33717f;
        font-family: 'Times New Roman', Times, serif;
        font-size: 25px;
    }

    .main-container{
        display: flex;
    }

    .content-container{
        display: inline-flex;
    }

    .meals-container{
        font-family: 'Times New Roman', Times, serif;
        margin: 0 auto;
        margin-top: 10%;
        padding-left: 50px;
        align-content: center;
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
        font-size: 14px;
        width: 15%;
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

    .filter{
        padding: 5px;
        margin-left: 60px;
        font-family: 'Times New Roman', Times, serif;
        text-align: center;
    }

    .heading{
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: #4890a0;
        text-align: center;
        font-size: 40px;
    }

</style>