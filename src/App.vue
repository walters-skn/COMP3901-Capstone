<template>

  <div id="app">
    <nav class="navbar navbar-expand navbar-light fixed-top">
      <div class="container">
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a href="./src/components/HomePage.vue" class="nav-link"> <strong> Home || </strong></a>
            </li>
            <li class="nav-item">
              <a href="#" class="nav-link"><strong> About Us </strong></a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
<div class="chatbox-container"> 
  <div class="chatbox">
    <div class="chatbox-header">
      <h2 class="head"> DIABOT CHAT </h2>
    </div>
    <div class="chatbox-body">
      <div v-for="(message, index) in messages" :key="index" class="message" :class="{ 'user-message': message.isUserMessage }">
        <div class="message-content">
          {{ message.content }}
        </div>
      </div>
    </div>
    <div class="chatbox-footer">
      <input type="text" v-model="newMessage" placeholder="Type a message..." @keydown.enter="sendMessage">
      <button class="btn" @click="sendMessage">Send</button>
    </div>
  </div>
</div>
</template>

<script>


export default {
  data() {
    return {
      messages: [],
      newMessage: ''
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.push({ content: this.newMessage, isUserMessage: true });
        this.newMessage = '';
      }
    }
  }
};
</script>

<style scoped>

.home{
    height: 10%;
    width: 100px;
    margin: -1%;
  }

/* navigation bar */
.navbar {
    padding: 0px;
    background-color: #5ca2b1;
  }

  /* navigation link */
  .nav-link{
    color: #000000;
  }

  .collapse{
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 20px;
    display: flex;
    justify-content: flex-end;
  }

  .chatbox-container{
    height:100vh;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
  }
  
  .head{
  font-family: fantasy;
  color: white;  
  text-align: center;
  margin: 0;
  font-size:45px;
}
.chatbox {
  width: 100%;
  max-width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row; /*this allows the "Diabot Chat" to go on the left side of the page*/
}


.chatbox-header {
  padding: 50px;
  background-color: #5ca2b1;
  display: flex;
  align-items: center;
}

.chatbox-body {
  flex: 1;
  /* padding: 1px; */
  overflow-y: auto;
}

.chatbox-footer {
  display: flex;
  align-items: flex-end;
  padding: 10px;
  width: 100%;
  font-size: 14px;
}

.chatbox-footer input[type="text"] {
  flex: 1;
  margin-right: 10px;
  padding: 7px;
  font-size: 14px;
  text-align: left;
}

.chatbox-footer button {
  padding: 5px 10px;
  background-color: #5599ab;
  color: white;
  font-family: 'Times New Roman', Times, serif;
  font-size: 14px;
}

.message {
  padding: 5px;
font-size: 15px;
}

.message-content {
  padding: 5px;
  font-size: 16px;
}


</style>
