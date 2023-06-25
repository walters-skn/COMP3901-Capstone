
<template>
  <NavBar/>
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
  <FooterView/>

  </template>

<script>

import FooterView from '@/components/FooterView.vue';
import NavBar from '@/components/NavBar.vue';

  export default {
    name: 'DiaBot',
      components:{
          FooterView,
          NavBar
      },
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
