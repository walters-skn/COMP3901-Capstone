<template> 
    <div class="header"> 
        <h2 class="name"> WELCOME TO DIABOT</h2>
    </div>

    <div class="page-layout">
      
      <div class="layout">
            <div class="container" >
                <img :src="imagePath" alt="profile" class="img">
                <div class="title"> <strong> Update Medical Data </strong></div>
            </div>
        </div>

        <div class="layout">
            <div class="container" >
                <img :src="imagePath2" alt="profile" class="img">
                <div class="title"><strong>  Nearest Clinics </strong></div>
            </div>
        </div>

        <div class="layout">
            <div class="container" >
                <img :src="imagePath3" alt="profile" class="img">
                <div class="title"> <strong> Create Notification</strong></div>
            </div>
        </div>

        <div class="layout">
            <div class="container" >
                <img :src="imagePath4" alt="profile" class="img">
                <div class="title"> <strong> Recommend Mean Plan </strong></div>
            </div>
        </div>

        <div class="layout">
            <div class="container" >
                <img :src="imagePath5" alt="profile" class="img">
                <div class="title"> <strong> Nutritional Scanner </strong></div>
            </div>
        </div>

        <div class="layout">
            <div class="container" >
                <img :src="imagePath6" alt="profile" class="img">
                <div class="title"> <strong> History </strong></div>
            </div>
        </div>
        
    </div> 
  </template>

  <script>
    import ImagePath from '@/assets/img/profile.png'
    import ImagePath2 from '@/assets/img/location.png'
    import ImagePath3 from '@/assets/img/notify.png'
    import ImagePath4 from '@/assets/img/meal.png'
    import ImagePath5 from '@/assets/img/scan.png'
    import ImagePath6 from '@/assets/img/history.png'
    
    export default {
      data(){
        return{
          imagePath: ImagePath,
          imagePath2: ImagePath2,
          imagePath3: ImagePath3,
          imagePath4 : ImagePath4,
          imagePath5 : ImagePath5,
          imagePath6 : ImagePath6
        }
      },
      name:"subscriberPage"
    }

  </script>
    
  <style scoped >

  .header{
    margin-top: 20px;
    align-content: center;
    text-align: center;
  }
    
  .img{ 
    height: 100px;
    width: 100px;
  }

  .container{
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  .title{
    font-size:18px;
    font-family: 'Times New Roman', Times, serif;
  }

  .layout{
    padding: 30px;
    display: flex;
    color: white;
  }

  .page-layout{
    margin-top: 20%;
    padding: 30px;
    display: flex;
    background-color: #5ca2b1;
    align-items: center;
    } 

    </style>