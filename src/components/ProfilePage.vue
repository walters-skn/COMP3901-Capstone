<template>
    <div class="page-container">
    <div class="header">
        <img :src="imagePath" alt="profile" class="img">
        <h2 class="name"> <strong> WELCOME</strong>  </h2>
    </div>

    <div class="profile-layout">

        <div class="layout">

            <div class="container" >
                <img :src="imagePath" alt="profile" class="img">
                <router-link link to="/profile">
                <div class="title"> 
                    <strong> <b>View Profile Information </b></strong>
                </div>
                </router-link>
            </div>
        </div>

        <div class="layout">
            <div class="container" >
                <img :src="imagePath2" alt="profile" class="img">
                <router-link link to='/diabot'>
                <div class="title"> 
                    <strong> <b> Create Notifications</b></strong>
                </div>
                </router-link>
            </div>
        </div>

        <div class="layout">
            <div class="container" >
                <img :src="imagePath3" alt="profile" class="img">
                <router-link link to='/diabot'>
                <div class="title"> 
                    <strong> <b>Diabot Chat </b></strong>
                </div>
                </router-link>
            </div>
        </div>

    </div> 
</div>

</template>

<script>

    import ImagePath from '@/assets/img/profile.png'
    import ImagePath2 from '@/assets/img/notify.png'
    import ImagePath3 from '@/assets/img/chat.png'
    
    export default {
        name: 'profilePage',
        data(){
            return{
                imagePath: ImagePath,
                imagePath2: ImagePath2,
                imagePath3: ImagePath3
            };
        },
        methods:{
            handleSubmit(){
                console.log('submitted')
            }
        }
    };
    
    </script>
  
<style scoped>

    .page-container{
        margin-top: -20vh;
        padding-top: 0;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        display: flex;
        margin-top: -20vh;
    }

    .header{
        margin: 0;
        padding: 5px;
        width: 100%;
        background-color: #5ca2b1;
        display: inline-block;
        color: white;
    }

    .name{
        font-family: 'Times New Roman', Times, serif;
        font-size: 35px;
    }
    
    .img{ 
        height: 100px;
        width: 100px;
    }

    .title{
        font-size:20px;
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: white;
        display: inline-block;
    }

    .container{
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
        text-align: center;
        padding: 20px;
        background-color: #5ca2b1;
    }

    .btn.btn-primary {
        background-color: white;
        border: none;
        color: #5ca2b1;
        font-size: 15px;
        font-family: 'Times New Roman', Times, serif;
    }

    .layout{
        padding: 50px;
        color: white;
    }

    .profile-layout{
        margin-top: 20px;
        display: flex;
        align-items: flex-end;
    } 

  </style>