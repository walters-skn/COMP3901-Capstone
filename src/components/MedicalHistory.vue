
<template>

    <div class="main-container">
        <SubscriberNavbar/>
    </div>
    
    <div class="content-container">
        <SideMenu/>

        <div class="container">
            <h1 class="heading"> Medical History</h1>
            <p >  What is to go on this page? </p>
        </div>

    </div>
  </template>
  
<script>
    import SideMenu from './SideMenu.vue'
    import SubscriberNavbar from './SubscriberNavbar.vue'
    // import { isAuthenticated, setAuthorizationHeader } from '@/authUtils';

    export default {
        components:{
            SubscriberNavbar,
            SideMenu,
        },
        
        methods: {
        // created() {
        //     // this.getAllHospitals();
        //     // this.filterByParish();

        //     this.isAuthenticated = isAuthenticated();
        //     if(!this.isAuthenticated){
        //         this.$router.push('/login')
        //     } else {
        //         this.token = localStorage.getItem('token');
        //         setAuthorizationHeader(this.token);
        //     }

        //     this.getAllHospitals();
        // },
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

    .address{
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size: 20px;
    }
  
    .heading{
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: #4890a0;
        text-align: center;
        font-size: 40px;
    }


    .address-input{
        padding: 5px;
        width: 30%;
        height: 2vh;
        border: 3px solid #ccc;
        /* border-radius: 10px; */
    }
    
    h3 {
        font-size: 20px;
    }
    
    p {
        margin: 5px 0;
        color: red;
        font-weight: bold;
    }

</style>
