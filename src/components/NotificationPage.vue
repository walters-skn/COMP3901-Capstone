
<template>

  <div class="main-container">
      <NavBar/>
  </div>
    
  <div class="content-container">
    <SideMenu/> 

    <div class="notification">

      <label class="reminder_label"><strong> Reminders</strong></label>
      <select v-model="selectedReminder" class="reminder">
        <option disabled value=""> Please select one</option>
        <option value="medication">Medication</option>
        <option value="appointment">Appointment</option>
      </select>

      <div class="option-section">

        <div v-if="selectedReminder === 'medication'">
          <label for="medication" class="label"> <strong> Medication Reminder</strong></label>

          <form v-on:submit.prevent="submitForm1" class="meds">
            <div class="medication-container"> 
              <label>Medication Name:</label>
              <input type="text" v-model="medicationName" class="input" >

              <label>Commencement Date:</label>
              <input type="date" v-model="comDate" class="input" >

              <label>Termination Date:</label>
              <input type="date" v-model="termDate" class="input">

              <label>Frequency:</label>
              <select v-model="frequency" class="input">
                <option value="daily">Daily</option>
                <option value="once_a_day"> Once(1) A Day</option>
                <option value="twice_a_day"> Twice(2) A Day</option>
                <option value="before_every_meals"> Before Every Meal</option>
                <option value="after_every_meal">After Every Meal</option>
                <option value="every_other_day"> Every Other Day</option>
              </select>

              <label> Quantity(eg.500mg):</label>
              <input type="number" v-model="quantityMeds" class="input">
            </div>
            
            <button v-on:click="addMedication" class="btn"> + </button>
            <button class="submit"> Submit </button>

          </form>

        </div>
      </div>
      
      <div class="option-section">

        <div v-if="selectedReminder === 'appointment'">
          <label for="appointment" class="label"><strong> Appointment Reminder</strong></label>
          <form v-on:submit.prevent="submitForm2"  class="apt">
            <div class="appointment-container">  
              <label>Location:</label>
              <input type="text" v-model="location" class="input">

              <label>Date:</label>
              <input type="date" v-model="appointmentDate" class="input">

              <label>Time:</label>
              <input type="time" v-model="appointmentTime" class="input">

              <label>Description</label>
              <textarea rows="4" cols="50" class="input" v-model="reminderDesc"></textarea>
            </div>

            <button v-on:click="addAppointment" class="btn">+</button>
            <button class="submit"> Submit </button>
          </form>

        </div>
      </div>

    </div>

  </div>

</template>

<script>

import NavBar from './NavBar.vue'
import SideMenu from './SideMenu.vue';
import axios from 'axios';
import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';

export default {
  name: 'ReminderForm',
  components:{
    NavBar,
    SideMenu,
  },
  data(){
    return{
      token: null,
      isAuthenticated: false,

      selectedReminder: '',
      medications: [],
      appointments: [],
      medicationName: '',
      comDate: '',
      termDate: '',
      frequency: '',
      quantityMeds: '',
      location: '',
      appointmentDate: '',
      appointmentTime: '',
      reminderDesc: '',
    }
  },
  methods:{
    addMedication() {
      this.medications = {
        medicationName: '',
        comDate: '',
        termDate: '',
        frequency: '',
        quantityMeds: '',
      }
    },
    addAppointment() {
      this.appointments = {
        location: '',
        appointmentDate: '',
        appointmentTime: '',
        reminderDesc: '',
      }
    },
    submitForm1() {
      if (this.selectedReminder === 'medication') {
        axios.post('http://localhost:5000/medication', {
          medicationName: this.medicationName,
          comDate: this.comDate,
          termDate: this.termDate,
          frequency: this.frequency,
          quantityMeds: this.quantityMeds,
        }).then((response) => {
          console.log("addMwdication response: ", response);
        }).catch((error) => {
          console.log("addMedication error: ", error);
        }) 
      } 
    },
    submitForm2() {
      if (this.selectedReminder === 'appointment') {
        
        axios.post('http://localhost:5000/reminder', {
          location: this.location,
          appointmentDate: this.appointmentDate,
          appointmentTime: this.appointmentTime,
          selectedReminder: this.selectedReminder,
          reminderDesc: this.reminderDesc,
        }).then((response)  => {
          console.log("addAppointment response: ", response);
        }).catch((error) => {
          console.log("addAppointment error: ", error);
        })
      }
    }
  },
  created() {
    isAuthenticated();
    if(!isAuthenticated){
        this.$router.push('/login')
    } else {
        this.token = localStorage.getItem('token');
        setAuthorizationHeader(this.token);
    }
  }
};

</script>

    
<style scoped>

  .main-container{
    display: flex;
  }


  .content-container{
    display: inline-flex;
  }

  .label{
    font-family: 'Times New Roman', Times, serif;
    display: block;
    font-size: 20px;
    flex: 1;
  }

  .option-section{
    margin-bottom: 50px 20px;
  }

  .meds, .apt{
    display: flex;
    flex-wrap: wrap;
    gap: 2px;
    flex-direction: column;
    width: 50%;

  }

  .reminder{
    padding: 8px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 90%;
    margin-bottom: 5%;

  }

  .reminder_label{
    color: #33717f;
    font-family: 'Times New Roman', Times, serif;
    font-size: 25px;
  }

  .notification{
    max-width: 800px;
    margin: 0 auto;
    padding: 50px 20px;
  }

  .input{
    padding: 8px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 90%;
    margin-bottom: 10px;
  }

  .medication-container,.appointment-container{
    flex: 1 1 45%;
    padding: 15px;
    border: 2px solid #ccc;
    border-radius: 10px;
  }

  .submit{
    background-color: #33717f;
    color: white;
    border: none;
    margin-top: 10px ;
    padding: 8px 16px;
    font-size: 16px;
    width: 50%;
    cursor: pointer;
  }

  .submit:hover{
    background-color: #ccc;
  }

  .btn{
    background-color: #33717f ;
    color: #fff;
    border: none;
    cursor: pointer;
    margin-top: 10px ;
    padding: 8px 16px;
    font-size: 14px;
    width: 20%;
  }

  .btn:hover{
    background-color: #ccc;
  }

</style>