
<template> 

    <div class="main-container">
        <NavBar/>
    </div>

    <div class="content-container">
        <SideMenu/>

        <div class="filter">
            <h1 class="heading"> <strong> Diabetes Management Diet</strong></h1>

            <label class="risk" ><strong>Select Risk Category</strong></label>
            <select v-model="selectedRiskCategory" v-on:change="showRiskMeals" class="risk-category">
                <option value="">Select a category</option>
                <option v-for="riskCategory in riskCategories" :key="riskCategory" :value="riskCategory">
                    {{ riskCategory }}
                </option>
            </select>

            <div v-if="selectedRiskCategory">
                <h2>Risk Meals</h2>
                <ul class="risk-meals">
                    <li v-for="riskMeal in displayRiskMeals" :key="riskMeal">{{ riskMeal }}</li>
                </ul>
            </div>

            
            <form v-on:submit.prevent="saveMeal" class="meals-container">
                <h2 class="details">Enter your meal details below: </h2>

                <div class="form-group">
                    <label>Meal Type</label>
                    <select v-model="selectType" class="risk-category">
                        <option value="">Select a type</option>
                        <option v-for="(value, key) in mealTypes" :key="key" :value="key">
                            {{ value }}
                        </option>
                    </select>
                </div>

                <div class="form-group"> 
                    <label>Meal Content: </label>
                    <input type="text" v-model="mealCont" class="input">
                </div>

                <div class="form-group"> 
                    <label>Upload Image Photo: </label>
                    <input type="file" ref="selectedFile" v-on:change="handleFileChange" enctype="multipart/form-data" class="input">
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

import NavBar from './NavBar.vue'
import SideMenu from './SideMenu.vue'
import axios from 'axios'
import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';


export default {
    components: {
        NavBar,
        SideMenu,
    },
    data() {
        return {

            token: null,
            
            riskCategories: [],
            riskMealsByCategory:{},
            selectedRiskCategory: '',
            displayRiskMeals: [],

            mealTypes: {
                breakfast: 'Breakfast',
                lunch: 'Lunch',
                dinner: 'Dinner'
            },
            selectType: '',

            mealCont: '',
            // nutriLvl: '',

            selectedFile: null
        }
    },
    methods: {
        saveMeal() {
            axios.post('http://localhost:5000/meal', {
                meal_type: this.selectType,
                meal_content: this.mealCont,
                // nutritional_level: this.nutriLvl,
                
                headers: {
                    'Content-Type': 'application/json'
                }
                
            }).then((response) => {
                console.log('saveMeal response: ', response);
                this.selectType = '';
                this.mealCont = '';
                // this.nutriLvl = '';
            }).catch((error) => {
                console.log('saveMeal Error: ', error);
            })

            axios.post('http://localhost:5000/meal', {
                selectedFile: this.$refs.selectedFile.files[0],
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
                
            }).then((response) => {
                console.log('saveMeal response file: ', response);
                // this.nutriLvl = '';
            }).catch((error) => {
                console.log('saveMeal Error file: ', error);
            })

        },
        showRiskMeals() {
            this.displayRiskMeals = this.riskMealsByCategory[this.selectedRiskCategory] || [];
        },
        handleFileChange(event) {
            this.selectedFile = event.target.files[0]
        }
    }
    ,
    created() {
        isAuthenticated();
        if(!isAuthenticated){
            this.$router.push('/login')
        } else {
            this.token = localStorage.getItem('token');
            setAuthorizationHeader(this.token);
        }

        axios.get('http://localhost:5000/meal')
            .then((response) => {
                this.riskCategories = Array.from(new Set(response.data.categories.map((meal) => meal.risk_category)));
                this.riskMealsByCategory = response.data.categories.reduce((acc, meal) => {
                    if(!acc[meal.risk_category]) {
                        acc[meal.risk_category] = [];
                    }
                    acc[meal.risk_category].push(meal.risk_meal);
                    return acc;
                }, {});
            }).catch((error) => {
                console.log('getRiskMeals Error: ', error);
            });
    }
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

    .risk-meals{
        list-style-type: none;
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