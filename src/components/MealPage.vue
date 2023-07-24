

<template> 

    <SubscriberNavbar/>

    <div class="meals-container">
        <h2> Enter your meal details below:</h2>

        <label>Meal Type:</label>
        <input type="text" class="input">

        <label>Meal Content:</label>
        <input type="text" class="input">

        <label>Nutritional Level:</label>
        <input type="text" class="input">

        <button @click="saveData" class="submit"> Submit </button>

    </div>

</template>

<script>

import SubscriberNavbar from './SubscriberNavbar.vue'
import axios from 'axios'

export default {
    components:{
        SubscriberNavbar,
    },
    methods:{
        saveDate(){
            axios.post('http://localhost:5000/meal',{
            })
            .then((response) => {
                console.log('Data successfully stored', response)

                // this.
            })
            .catch((error) => {
                console.log('Error', error)
            });
        },
    },
};

</script>

<style scoped>

.submit{
    background-color: #33717f;
    color: white;
    border: none;
    margin-top: 10px ;
    padding: 8px 16px;
    font-size: 16px;
    width: 20%;
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