
<template>
  <NavBar/>
</template>

<script>

import ImagePath2 from '@/assets/img/logo.png'
import NavBar from '@/components/NavBar.vue';


export default {
    name:"myApp",
    components:{
        NavBar
    },
  data(){
    return{
      imagePath2: ImagePath2,
    };
  }
}; 
</script>
