
<template>

    <div class="main-container">
        <NavBar/>
    </div>
    
    <div class="content-container">
        <SideMenu/>

        <div class="filter">
            <h1 class="heading"> <strong> <b> User Medical Records</b></strong></h1>

            <div class="table-container"> 
                <table> 
                    <thead>
                        <tr>
                            <th> Symptom ID</th>
                            <th> Gender</th>
                            <th> Weight</th>
                            <th> Age</th>
                            <th> Waist Size</th>
                            <th> Waist Circumference</th>
                            <th> Physically Active</th>
                            <th> Fruit/Veggie Intake</th>
                            <th> Has High Bp Medication</th>
                            <th> History of Hyperglycemia </th>
                            <th> Family Medical History</th>
                        </tr>
                    </thead>
                    <tbody> 
                        <tr v-for="symptom in symptoms" :key="symptom">
                            <td> {{ symptom.symptom_id}}</td>
                            <td> {{ symptom.gender}}</td>
                            <td> {{ symptom.weight}}</td>
                            <td> {{ symptom.height}}</td>
                            <td> {{ symptom.age}}</td>
                            <td> {{ symptom.waist_circumference}}</td>
                            <td> {{ symptom.is_physically_active}}</td>
                            <td> {{ symptom.fruit_veggie_intake}}</td>
                            <td> {{ symptom.has_high_bp_medication}}</td>
                            <td> {{ symptom.has_hyperglycemia_history}}</td>
                            <td> {{ symptom.has_family_history}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
  
<script>
    import SideMenu from './SideMenu.vue'
    import NavBar from './NavBar.vue'
    import axios from 'axios';
    import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';

    export default {
        components:{
            NavBar,
            SideMenu,
        },
        data() {
            return {
                token: null,
                isAuthenticated: false,

                symptoms: [],
                symptom_id: '',
                gender: '',
                weight: '',
                height: '',
                age: '',
                waist_circumference: '',
                is_physically_active: '',
                fruit_veggie_intake: '',
                has_high_bp_medication: '',
                has_hyperglycemia_history: '',
                has_family_history: '',
            };
        },
        
        methods: {
            getSymptoms() {
                axios.get('http://localhost:5000/symptoms')
                .then((response) => {
                    this.symptoms = response.data.symptoms;
                    console.log('getSymptoms response:', this.symptoms);
                })
                .catch((error) => {
                    console.log('getSymptoms error:', error);
                });
            }
        },
        created() {
            this.isAuthenticated = isAuthenticated();
            if(!this.isAuthenticated){
                this.$router.push('/login')
            } else {
                this.token = localStorage.getItem('token');
                setAuthorizationHeader(this.token);
            }
            
            this.getSymptoms();
        }
    }
</script>

<style scoped>

    .main-container{
        display: flex;
    }

    .content-container{
        display: inline-flex;
    }
  
    .heading{
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: #4890a0;
        font-size: 40px;
    }

    .filter{
        padding: 5px;
        margin-left: 60px;
        font-family: 'Times New Roman', Times, serif;
        text-align: center;
        display:flex;
        flex-direction: column;
        align-items: center;
    }
    
    .table-container{
        overflow-x: auto;
    }

    table{
        width: 100%;
        border-collapse: collapse;
        border: 3px solid #ccc;
        margin-top: 10px;
    }

    th,
    td{
        padding: 8px 12px;
        text-align: center;
        border-bottom: 1px solid #ccc;
    }

    th{
        background-color: #5CA2B1;
    }

    tbody tr:nth-child(even){
        background-color: #f2f2f2;
    }

</style>
