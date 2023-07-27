
<template>
    <h2> User List Admin View</h2>
    <table>
        <thead>
            <tr>
                <th> Patient ID</th>
                <th> First Name</th>
                <th> Last Name</th>
                <th> Patient Contact Number</th>
                <th> Nutritional Level</th>
                <th> Medication Name</th>
                <th> Commencement Date</th>
                <th> Termindation Date</th>
                <th> Clinic Name</th>
                <th> Appointment Date</th>
                <th> Reminder Type</th>
                
            </tr>
        </thead>

        <tbody>
            <tr v-for="profile in profiles" :key="profile">
                
                <td> {{ profile.patient_id }}</td>
                <td> {{ profile.first_name}}</td>
                <td> {{ profile.last_name }}</td>
                <td> {{ profile.phone }}</td>
                <td> {{ profile.nutri_lvl }}</td>
                <td> {{ profile.medication_name}}</td>
                <td> {{ profile.commencement_date }}</td>
                <td> {{ profile.termination_date  }}</td>
                <td> {{ profile.cname }}</td>
                <td> {{ profile.appt_date }}</td>
                <td> {{ profile.remind_type }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>

import axios from 'axios';
import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';

export default{
    data(){
        return{
            token: null,
            isAuthenticated: false,

            profiles: [],
            patient_id: '',
            first_name: '',
            last_name: '',
            phone: '',
            nutri_lvl: '',
            medication_name: '',
            commencement_date: '',
            termination_date: '',
            cname: '',
            appt_date: '',
            remind_type: '',
        };
    },
    methods: {
        getProfile(){
            axios.get('http://localhost:5000/profile')
            .then((response) => {
                this.profiles = response.data.profiles;
                console.log('getProfile response:', this.profiles);
            })
            .catch((error) => {
                console.log('getProfile error:', error);
            });
        }
    },
    created(){
        this.isAuthenticated = isAuthenticated();
        if(!this.isAuthenticated){
            this.$router.push('/login')
        } else {
            this.token = localStorage.getItem('token');
            setAuthorizationHeader(this.token);
        }
        
        this.getProfile();
    }
}
</script>

<style scoped>

</style>
