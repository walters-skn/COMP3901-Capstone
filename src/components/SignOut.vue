<template>
    <button @click="signOut">Sign Out</button>
  </template>
  
  <script>
  export default {
    methods: {
      signOut() {
        // Implement your sign-out logic here
        // For example, you can clear local storage or session data
        // and redirect the user to the login page
        localStorage.clear();
        // Redirect to the login page
        this.$router.push('/login');
      }, //correction
    },
  };
  //correction//correction//correction//correction//correction
  </script>
  