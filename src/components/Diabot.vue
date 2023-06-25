<template>
    <div class="chatbox">
      <div class="chatbox-header">
        <h3>Chat</h3>
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
        <button @click="sendMessage">Send</button>
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
  .chatbox {
    width: 300px;
    height: 400px;
    border: 1px solid #ccc;
    border-radius: 4px;
    display: flex;
    flex-direction: column;
  }
  
  .chatbox-header {
    background-color: #f5f5f5;
    padding: 10px;
    text-align: center;
  }
  
  .chatbox-body {
    flex: 1;
    padding: 10px;
    overflow-y: auto;
  }
  
  .message {
    padding: 5px;
    margin-bottom: 5px;
  }
  
  .user-message {
    background-color: #f0f0f0;
  }
  
  .message-content {
    padding: 5px;
  }
  
  .chatbox-footer {
    display: flex;
    align-items: center;
    padding: 10px;
  }
  
  .chatbox-footer input[type="text"] {
    flex: 1;
    margin-right: 10px;
    padding: 5px;
  }
  
  .chatbox-footer button {
    padding: 5px 10px;
  }
  </style>
  