
<template> 
    <div class="page-container">
        <NavBar/>
            <div class="body">
                <h2 class = "title"> New User? <br> SIGN UP TO GET STARTED </h2> 
            </div>
            
        <FooterView/>
    </div>
    </template>
        
    <script>
      
        import ImagePath2 from '@/assets/img/logo.png'
        import FooterView from '@/components/FooterView.vue';
        import NavBar from '@/components/NavBar.vue';
    
        export default {
            name: 'register',
            components:{
                FooterView,
                NavBar
            },
            methods:{
                handleSubmit(){
                    console.log('submitted')
                }
            },
            data(){
                return{
                    imagePath2: ImagePath2,
                };
            }
        };
    
    </script>
    
    <style scoped >
    
        .page-container {
        background-color: #5ca2b1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        }
        
        /* form */
        .form-container{
          background-color: #ACC5CB;
          width: 100%;
          margin: 0 auto;
        }
      
        .form{
          padding: 5px;
          border: 5px solid #ccc;
          border-radius: 5px;
          width: 100%;
        }
        
        .form-group{
          margin-bottom: 10px;
          align-items: center;
        }
      
        .form-inline{
          display: flex;
          align-items: center;
        }
        
        .title {
            background-color: #5CA2B1;
            color: white;
            font-family: 'Times New Roman', Times, serif;
            text-align: center;
            padding-top: 50px;
            margin-top: 50px;
        }
        
        .box{
            width: 100%;
            background-color: #ACC5CB;
        }
        
        .submit-group {
            display: flex;
            justify-content: center;
            align-items: center;
        }
      
        .btn.btn-primary {
            background-color: #4C8F9E;
            border: 2px solid #FAE9E9;
            color: white;
            font-size: 15px;
            font-family: 'Times New Roman', Times, serif;
        }
      
        </style>