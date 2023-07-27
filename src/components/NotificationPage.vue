<template>

  <div class="main-container">
      <SubscriberNavbar/>
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

          <form v-on:submit.prevent="saveData" class="meds">
            <div v-for="(med,index) in medications" :key="index" class="medication-container"> 
              <label>Medication Name:</label>
              <input type="text" v-model="med.medicationName" class="input" >

              <label>Commencement Date:</label>
              <input type="date" v-model="med.comDate" class="input" >

              <label>Termination Date:</label>
              <input type="date" v-model="med.termDate" class="input">

              <label>Frequency:</label>
              <select v-model="med.frequency" class="input">
                <option value="daily">Daily</option>
                <option value="once_a_day"> Once(1) A Day</option>
                <option value="twice_a_day"> Twice(2) A Day</option>
                <option value="before_every_meals"> Before Every Meal</option>
                <option value="after_every_meal">After Every Meal</option>
                <option value="every_other_day"> Every Other Day</option>
              </select>

              <label> Quantity(eg.500mg):</label>
              <input type="text" v-model="med.quantityMeds" class="input">
            </div>
            
            <button @click="addMedication" class="btn"> + </button>
            <button class="submit"> Submit </button>
          </form>

        </div>
      </div>
      
      <div class="option-section">

        <div v-if="selectedReminder === 'appointment'">
          <label for="appointment" class="label"><strong> Appointment Reminder</strong></label>
          <form v-on:submit.prevent="saveData" class="apt">
            <div v-for="(apt,index) in appointments" :key="index" class="appointment-container">  
              <label>Location:</label>
              <input type="text" v-model="apt.location" class="input">

              <label>Date:</label>
              <input type="date" v-model="apt.appointmentDate" class="input">

              <label>Time:</label>
              <input type="time" v-model="apt.appointmentTime" class="input">
            </div>

            <button @click="addAppointment" class="btn">+</button>
            <button class="submit"> Submit </button>
          </form>

        </div>
      </div>

    </div>

  </div>

</template>

<script>

import SubscriberNavbar from './SubscriberNavbar.vue'
import SideMenu from './SideMenu.vue';
import axios from 'axios';
import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';

export default {
  components:{
    SubscriberNavbar,
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
    }
  },
  methods:{
    addMedication(){
      this.medications.push({
        medicationName: '',
        comDate: '',
        termDate: '',
        frequency: '',
        quantityMeds:'',
      });
    },
    addAppointment(){
      this.appointments.push({
        location: '',
        appointmentDate: '',
        appointmentTime: '',
      });
    },
    saveData(){
      axios.post('http://localhost:5000/notification', {
        remind_type: this.selectedReminder,
        medication_name: this.medicationName,
        commencement_date: this.comDate,
        termination_date: this.termDate,
        frequency: this.frequency,
        quantity: this.quantityMeds,
        cname: this.location,
        appt_date: this.appointmentDate,
        appt_time: this.appointmentTime,
      })
      .then((response) => {
        console.log('Data successfully stored', response);
      })
      .catch((error) => {
        console.log('Error', error);
      });
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
  },
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