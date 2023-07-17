<template>

  <SubscriberNavbar/>

  <div class="notification">

    <input type="checkbox" v-model="medication" class="options"> 
    <label for="medication" class="checkbox-label"> Medication</label>

    <input type="checkbox" v-model="appointment" class="options">
    <label for="appointment" class="checkbox-label"> Appointment</label>
 

    <div v-if="medication" class="meds">
      <label>Medication Type:</label>
      <input type="text" v-model="medicationType" class="input">

      <label>Frequency:</label>
      <select v-model="frequency">
        <option value="daily" class="input">Daily</option>
        <option value="3_times_daily" class="input">Everyday (3 times daily)</option>
      </select>

      <label>Date:</label>
      <input type="date" v-model="medicationDate" class="input">

      <label>Time:</label>
      <input type="time" v-model="medicationTime" class="input">
    </div>

    <div v-if="appointment" class="apt">
      <label>Location (Doctor's Office):</label>
      <input type="text" v-model="location" class="input">

      <label>Date:</label>
      <input type="date" v-model="appointmentDate" class="input">

      <label>Time:</label>
      <input type="time" v-model="appointmentTime" class="input">
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
      medication: false,
      appointment: false,
      showMedicationOptions: false,
      medicationType: '',
      frequency: '',
      medicationDate: '',
      medicationTime: '',
      location: '',
      appointmentDate: '',
      appointmentTime: '',
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
};
</script>
      
<style scoped>

  .notification{
    font-family: 'Times New Roman', Times, serif;
    font-size: 25px;
    /* margin-left: 20px; */
    padding-top: 50px;
  }

  .options{
    font-family: 'Times New Roman', Times, serif;
    /* font-size: 70px;
    margin-left: 20px;
    padding: 50px; */
    margin-left: 20px;
    transform: scale(1.5);

  }

  .meds, .apt{
    padding:30px;
  }

  .checkbox-label{
    font-size: 25px;
  }

  .input{
    padding: 8px;
  }

</style>