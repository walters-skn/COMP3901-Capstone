<template>

  <SubscriberNavbar/>

  <div class="notification">
    <div class="option-section">
      <input type="checkbox" v-model="medication" class="options"> 
      <label for="medication" class="checkbox-label"> Medication</label>

      <div v-if="medication" class="meds">
        <label>Medication Type:</label>
        <input type="text" v-model="medicationType" class="input">

        <label>Frequency:</label>
        <select v-model="frequency" class="input">
          <option value="daily">Daily</option>
          <option value="3_times_daily">Everyday (3 times daily)</option>
        </select>

        <label>Date:</label>
        <input type="date" v-model="medicationDate" class="input">

        <label>Time:</label>
        <input type="time" v-model="medicationTime" class="input">
      </div>
    </div>

    <div class="option-section">
      <input type="checkbox" v-model="appointment" class="options">
      <label for="appointment" class="checkbox-label"> Appointment</label>

      <div v-if="appointment" class="apt">
        <label>Location (Doctor's Office):</label>
        <input type="text" v-model="location" class="input">

        <label> Name of Doctor(s):</label>
        <input type="text" v-model="location" class="input">

        <label>Date:</label>
        <input type="date" v-model="appointmentDate" class="input">

        <label>Time:</label>
        <input type="time" v-model="appointmentTime" class="input">
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
    padding-top: 50px;
  }

  .options{
    font-family: 'Times New Roman', Times, serif;
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
    font-size: 16px;
  }

  .checkbox-label{
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 10px;
  }

</style>