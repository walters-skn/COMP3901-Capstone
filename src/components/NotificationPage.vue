<template>

  <SubscriberNavbar/>

  <div class="notification">

    <div class="option-section">
      <label for="medication" class="label"> <strong> Set Medication Reminder</strong></label>
      <button @click="addMedication" class="btn"> +</button>

      <div class="meds">
        <div v-for="(med,index) in medications" :key="index" class="medication-container"> 
          <label>Medication Name:</label>
          <input type="text" v-model="med.medicationName" class="input">

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

          <label> Quantity(eg.500mg):</label>
          <input type="text" v-model="med.quantityMeds" class="input">

        </div>

        <!-- <button @click="addMedication" class="add-button"> + </button> -->
        <button @click="saveData" class="submit"> Submit </button>

      </div>

      </div>
      

      <div class="option-section">
        <label for="appointment" class="label"><strong> Set Appointment Reminder</strong></label>
        <button @click="addAppointment" class="btn"> +</button>

        <div class="apt">
          <div v-for="(apt,index) in appointments" :key="index" class="appointment-container"> 

            <label>Location:</label>
            <input type="text" v-model="apt.location" class="input">

            <label>Date:</label>
            <input type="date" v-model="apt.appointmentDate" class="input">

            <label>Time:</label>
            <input type="time" v-model="apt.appointmentTime" class="input">
          </div>

          <!-- <button @click="addAppointment" class="add-button"> + </button> -->
          <button @click="saveData" class="submit"> Submit </button>

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
      activeMedicationIndex: -1,
      activeAppointmentIndex: -1,
      showMedicationOptions: false,
      medicationName: '',
      comDate: '',
      termDate: '',
      frequency: '',
      // medicationDate: '',
      // medicationTime: '',
      location: '',
      appointmentDate: '',
      appointmentTime: '',
      quantityMeds:'',
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
        name: '',
        appointmentDate: '',
        appointmentTime: '',
      });
    },
  },

};

</script>
      
<style scoped>

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
    gap: 10px;
  
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
    width: 100%;
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
    border: none;
    color: white;
    margin-top: 10px ;
    padding: 8px 16px;
    font-size: 16px;
  }

  .btn{
    background-color: #33717f ;
    color: #fff;
    border: none;
    border-radius: 2px;
    cursor: pointer;
    margin-top: 10px ;
    padding: 8px 16px;
    font-size: 16px;
  }

  .btn:hover{
    background-color: #ccc;
  }

</style>