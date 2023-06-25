<template> 
<!-- This page will get the other navigation pane -->

    <form @submit.prevent="handleSubmit">
        <h3> New User</h3>
        <h3> Sign Up To Get Started</h3>
    
        <div class="form-group">
            <label> First Name </label>
            <input type="text" class="form-control" placeholder="Jane" />
        </div>
    
        <div class="form-group">
            <label> Last Name </label>
            <input type="text" class="form-control" placeholder="Doe" />
        </div>
    
    </form>
    </template>
    
<script>
    export default {
        name: 'ProfilePage',
    }
</script>

<style scoped> 
</style>