
<template>
  <div class="chatbox-container"> 

    <div class="chatbox-header">
      <h2 class="head"> DIABOT CHAT </h2>
    </div>

    <div class="chatbox">

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
    name: 'DiaBot',
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
  .chatbox-container{
    width: 80%;
    margin-left:0;
    /* height:90vh; */
    /* display: flex; */
    /* flex-direction: row; */
  }

  .chatbox-header {
    position: absolute;
    left: 0;
    width: 20%;
    height: 90vh;
    /* padding: 50px; */
    background-color: #4C8F9E;
    color: white;
    font-family: 'Times New Roman', Times, serif;
    display: flex;
    align-items: center;
}
  .head{
  font-family: fantasy;
  color: white;  
  text-align: center;
  font-size:45px;
  }

  .chatbox-body {
    padding: 90px;
  }

  .chatbox {
    display: flex;
    flex-direction: row; /*this allows the "Diabot Chat" to go on the left side of the page*/
  }

.chatbox-footer {
  display: flex;
  align-items: flex-end;
  height: 90vh;
  width: 100%;
  font-size: 14px;
  margin-left: 0;
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
  background-color: #92aeb5;
}

.message-content {
  font-size: 16px;
}

</style>
