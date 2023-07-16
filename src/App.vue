<template>
  <NavBar/>
  <!-- <SubscriberNavBar v-if="$route.path === '/subscriber'" /> -->

</template>

<script>

import NavBar from '@/components/NavBar.vue';
// import SubscriberNavBar from '@/components/SubscriberNav'

export default {
    name:"myApp",
    components:{
        NavBar
        // SubscriberNavBar
    },
}; 
</script>

<style>
  body {
    margin: 0;
    /* max-height: 100vh; */
  }
</style>