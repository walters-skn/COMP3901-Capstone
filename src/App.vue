
<template>
  <NavBar/>

  <br> <br> <br> <br>  

  <FooterView/>
</template>

<script>

import ImagePath2 from '@/assets/img/logo.png'
import NavBar from '@/components/NavBar.vue';
import FooterView from '@/components/FooterView.vue';


export default {
    name:"myApp",
    components:{
        NavBar,
        FooterView
    },
  data(){
    return{
      imagePath2: ImagePath2,
    };
  }
}; 
</script>
