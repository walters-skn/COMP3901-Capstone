<template>
  <NavBar/>
</template>

<script>

import NavBar from '@/components/NavigationBar.vue';

export default {
    name:"myApp",
    components:{
        NavBar
    },
}; 
</script>

<style>
  body {
    margin: 0;
    max-height: 100vh;
  }
</style>