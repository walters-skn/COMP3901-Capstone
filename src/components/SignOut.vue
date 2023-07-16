<template>
  <div class="signout" @click="signOut">
  </div>
  
</template>
  
<script>

  export default {
    methods: {
      signOut() {
        localStorage.clear();
        // Redirect to the login page
        this.$router.push('/login');
      },
    },
  };
</script>

