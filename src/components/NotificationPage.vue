<template>

  <SubscriberNavbar/>

  <div class="notification">

      <label class="reminder_label"><strong>Select Reminder</strong></label>
      <select v-model="selectedReminder" class="reminder">
        <option disabled value=""> Please select one</option>
        <!-- <option value="none">None</option> -->
        <option value="medication">Medication</option>
        <option value="appointment">Appointment</option>
      </select>

    <div class="option-section">

        <div v-if="selectedReminder === 'medication'">
          <label for="medication" class="label"> <strong> Medication Reminder</strong></label>

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
            
            <button @click="addMedication" class="btn"> + </button>
            <button @click="saveData" class="submit"> Submit </button>

        </div>
      </div>
    </div>
      
      <div class="option-section">

        <div v-if="selectedReminder === 'appointment'">
          <label for="appointment" class="label"><strong> Appointment Reminder</strong></label>

          <div class="apt">
            <div v-for="(apt,index) in appointments" :key="index" class="appointment-container">  
              <label>Location:</label>
              <input type="text" v-model="apt.location" class="input">

              <label>Date:</label>
              <input type="date" v-model="apt.appointmentDate" class="input">

              <label>Time:</label>
              <input type="time" v-model="apt.appointmentTime" class="input">
            </div>

            <button @click="addAppointment" class="btn">+</button>
            <button @click="saveData" class="submit"> Submit </button>

          </div>
        </div>
      </div>

  </div>

  <!-- Users can see the information they just entered -->
  <div class="entries">
    <h2> Entries </h2>

    <ul>
      <li v-for="(med,index) in userResponses.medications" :key="index" > 
        <strong> Medication Name</strong> {{ med.medicationName }}
        <strong> Commencement Date</strong> {{ med.comDate }}
        <strong> Termination Date</strong> {{ med.termDate }}
        <strong> Frequency </strong> {{ med.frequency }}
        <strong> Quantity</strong> {{ med.quantityMeds }}
        <button @click="removeMedication(index)">Delete</button>
      </li>

      <li v-for="(apt,index) in userResponses.appointments" :key="index">
        <strong>Location</strong> {{ apt.location }}
        <strong> Appointment Date</strong> {{ apt.appointmentDate }}
        <strong> Appointment Time</strong> {{ apt.appointmentTime }}
        <button @click="removeAppointment(index)">Delete</button>
      </li>
    </ul>
  </div>

</template>

<script>

import SubscriberNavbar from './SubscriberNavbar.vue'
import axios from 'axios';

export default {
  components:{
    SubscriberNavbar,
  },
  data(){
    return{
      selectedReminder: '',
      medications: [],
      appointments: [],
      userResponses: [],
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
    addReminder(){
      if(!this.selectedReminder) return;
      if (this.selectedReminder === 'medication') {
        this.medications.push({
          medicationName: '',
          comDate: '',
          termDate: '',
          frequency: '',
          quantityMeds:'',
        });
      } else if(this.selectedReminder === 'appointment'){
          this.appointments.push({
            location: '',
            appointmentDate: '',
            appointmentTime: '',
          });
      }
    },
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
    removeMedication(index){
      this.userResponses.medications.splice(index,1);
    },
    removeAppointment(index){
      this.userResponses.appointments.splice(index,1);
    },
    saveData(){
      console.log('userResponses:', this.userResponses)
      axios.post('http://localhost:5000/reminders',{
        responses: this.userResponses
      })
      .then((response) => {
        console.log('Data successfully stored', response);
        this.medicationName = response.data.medicationName;
        this.comDate = response.data.comDate;
        this.termDate = response.data.termDate;
        this.frequency = response.data.frequency;
        this.quantityMeds = response.data.quantityMeds;
        this.location = response.data.location;
        this.appointmentDate = response.data.appointmentDate;
        this.appointmentTime = response.data.appointmentTime;

        this.userResponses.medications = this.medications.slice();
        this.userResponses.appointments = this.appointments.slice();
      })
      .catch((error) => {
        console.log('Error', error);
      });
      this.userResponses={
        medications: this.medications.slice(),
        appointments: this.appointments.slice()
      };
      // Clears form after submission
      this.selectedReminder = '';
      // this.medications = [];
      // this.appointments =[];
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
    width: 20%;
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
    font-size: 16px;
    width: 10%;
  }

  .btn:hover{
    background-color: #ccc;
  }

</style>