
<template>
  <NavBar/>
  <FooterView/>

</template>

<script>

// import { useRouter } from 'vue-router';
import ImagePath2 from '@/assets/img/logo.png'
import FooterView from '@/components/FooterView.vue';
import NavBar from '@/components/NavBar.vue';

export default {
    name:"myApp",
    components:{
        FooterView,
        NavBar
    },
  data(){
    return{
      imagePath2: ImagePath2,
    };
  }
}; 
</script>

<style scoped></style>
