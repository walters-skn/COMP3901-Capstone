
<template>

    <div class="main-container">
        <SubscriberNavbar/>
    </div>
    
    <div class="content-container">
        <SideMenu/>

        <div class="filter">
            <h1 class="heading"> <strong> <b> Medical Information</b></strong></h1>
            <p> **Show their medical information** </p>
            <p> ** Give them the option to update their medical information** </p>
            <!-- <input id="address-input" v-model="selectedAddress" class="address-input" placeholder="Enter your Parish"> -->
        </div>

    </div>
  </template>
  
<script>
    import SideMenu from './SideMenu.vue'
    import SubscriberNavbar from './SubscriberNavbar.vue'
    import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';

    export default {
        components:{
            SubscriberNavbar,
            SideMenu,
        },
        data() {
            return {
                token: null,
                isAuthenticated: false,
            };
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
        /* justify-content: center; */
    }
    
    h3 {
        font-size: 20px;
    }
    
    p {
        font-family: 'Times New Roman', Times, serif;
        font-weight: bold;
        color:red;
        margin: 5px 0;
    }
</style>
