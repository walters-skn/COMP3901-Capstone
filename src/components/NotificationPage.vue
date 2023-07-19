<template>

  <SubscriberNavbar/>

  <div class="notification">
    <div class="option-section">
      <!-- <input type="checkbox" v-model="medication" class="options">  -->
      <label for="medication" class="checkbox-label"> Medication</label>

      <div class="meds">
        <div v-for="(med,index) in medications" :key="index"> 
          <label>Medication Type:</label>
          <input type="text" v-model="med.medicationType" class="input">

          <label>Commencement Date:</label>
          <input type="date" v-model="med.comDate" class="input">

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

          <label> Custom Time:</label>
          <input type="date" v-model="med.medicationTime" class="input">
        </div>

          <!-- <label>Termination Time:</label>
          <input type="date" v-model="medicationDate" class="input"> -->

        <button @click="addMedication"> Add Medication </button>
      </div>
    </div>

      <div class="option-section">
        <label for="appointment" class="checkbox-label"> Appointment</label>

        <div class="apt">
          <div v-for="(apt,index) in medications" :key="index"> 
            <label>Location (Doctor's Office):</label>
            <input type="text" v-model="apt.location" class="input">

            <label> Name of Doctor(s):</label>
            <input type="text" v-model="apt.name" class="input">

            <label>Date:</label>
            <input type="date" v-model="apt.appointmentDate" class="input">

            <label>Time:</label>
            <input type="time" v-model="apt.appointmentTime" class="input">
          </div>
          <button @click="addAppointment"> Add Appointment </button>
        </div>
      </div>
  </div>

</template>
    
<script>    

import SubscriberNavbar from './SubscriberNavbar.vue'

export default {
  components:{
    SubscriberNavbar,
  },
  data() {
    return {
      medications: [],
      appointments: [],
      medication: false,
      appointment: false,
      showMedicationOptions: false,
      // medicationType: '',
      // comDate: '',
      // termDate: '',
      // frequency: '',
      // medicationDate: '',
      // medicationTime: '',
      // location: '',
      // appointmentDate: '',
      // appointmentTime: '',
    };
  },
  watch: {
    medication(value) {
      if (value) {
        this.showMedicationOptions = true;
      } else {
        this.showMedicationOptions = false;
      }
    },
  },
  methods:{
    addMedication(){
      this.medications.push({
        medicationType: '',
        comDate: '',
        termDate: '',
        frequency: '',
        medicationTime: '',
      });
    },
    addAppointment(){
      this.appointments.push({
        location: '',
        name: '',
        appointmentDate: '',
        appointmentTime: '',
      });
    },
  },

};

</script>
      
<style scoped>

  .notification{
    font-family: 'Times New Roman', Times, serif;
    font-size: 25px;
    padding-top: 50px;
  }

  .meds, .apt{
    padding:30px;
    display: flex;
    flex-direction: column;
  }

  .meds label, .apt label{
    margin-bottom:10px;
  }

  .checkbox-label{
    font-size: 25px;
  }

  .input{
    padding: 8px;
    font-size: 16px;
  }

  .checkbox-label{
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 10px;
  }

  button{
    margin-top: 10px ;
    padding: 8px 16px;
    font-size: 16px;
  }

</style>