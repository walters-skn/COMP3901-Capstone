<template> 
    <div class="page-container">
        <div>
            <nav class="navbar navbar-expand navbar-light fixed-top">

                <div class="collapse navbar-collapse" id="navbarNav">
                  <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                      <router-link to="/" class="nav-link"><strong>Home ||</strong></router-link>
                    </li>
                    <li class="nav-item">
                      <router-link to='/signout' class="nav-link"><strong>Sign Out </strong></router-link>
                    </li>
                  </ul>
                </div>  
            </nav> 
            <router-view></router-view>
        </div>
    </div>
    <div class="header">
        <img :src="imagePath" alt="profile" class="img">
        <h2 class="name"> <strong> WELCOME JANE DOE</strong>  </h2>
    </div>
    <div class="page-layout">

<div class="layout">
    <div class="container" >
        <img :src="imagePath" alt="profile" class="img">
        <div class="title"> <strong> Profile Information </strong></div>
    </div>
</div>

<div class="layout">
    <div class="container" >
        <img :src="imagePath2" alt="profile" class="img">
        <div class="title"><strong>  Notifications </strong></div>
    </div>
</div>

<div class="layout">
    <div class="container" >
        <img :src="imagePath3" alt="profile" class="img">
        <div class="title"> <strong> Diabot Chat </strong></div>
    </div>
</div>

</div> 
<FooterView/>

</template>

<script>

    import FooterView from '@/components/FooterView.vue';

    import ImagePath from '@/assets/img/profile.png'
    import ImagePath2 from '@/assets/img/notify.png'
    import ImagePath3 from '@/assets/img/chat.png'
    
    export default {
        name: 'profile',
        components: {
            FooterView
        },
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
  
  /* navigation */
    .navbar {
      padding: 5px;
      background-color: #5ca2b1;
    }
  
    .nav-link{
      color: white;
    }
  
    .header{
        margin: 50px;
        padding: 15px;

    }
  
    .page-container{
      background-color:#5CA2B1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
          
    .collapse{
      font-family: Georgia, 'Times New Roman', Times, serif;
      font-size: 20px;
      display: flex;
      justify-content: flex-end;
    }

    .name{
        font-family: 'Times New Roman', Times, serif;
        font-size: 35px;
        padding-top:5px;
    }
    
    .img{ 
        height: 100px;
        width: 100px;
    }

    .title{
        font-size:18px;
        font-family: 'Times New Roman', Times, serif;
    }

    .container{
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: center;
        text-align: center;
        padding: 40px;
    }

    .layout{
        padding: 30px;
        display: flex;
        color: white;
    }

    .page-layout{
        display: flex;
        align-items: flex-end;
        justify-content: center;
        background-color: #5ca2b1;
        flex-grow: 1;
      } 

  </style>
  
  