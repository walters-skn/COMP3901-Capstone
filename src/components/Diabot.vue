
<template>
    <div class="chat-container">
        <div class="chat-sidebar">
            <h1> <b><strong>DIABOT <br> CHAT</strong></b></h1>
        </div>    
    <div class="chat-content">
        <div class="chat-messages">
            <div v-for="message in messages" :key="message.id" class="message" :class="{ 'user-message': message.from === 'user', 'bot-message': message.from === 'bot' }">
                <div class="message-content">
                    {{ message.text }}
                </div>
            </div>
        </div>
    <div class="chat-input">
        <input v-model="inputText" @keydown.enter="sendMessage" placeholder="Type your message..." />
        <button @click="sendMessage">Send</button>
    </div>
  </div>
    </div>
  </template>
  
  <script>
  import { reactive, ref } from 'vue';
  
  export default {
  name: 'diaBot',
  setup() {
    const messages = reactive([]);
    const inputText = ref('');
  
    const sendMessage = () => {
      const text = inputText.value.trim();
      if (text) {
        messages.push({ id: Date.now(), text, from: 'user' });
        inputText.value = '';
      }
    };
  
    return { messages, inputText, sendMessage };
  },
  };
  </script>
  
  <style scoped>
  
    .chat-container{
        display: flex;
        width: 100%;
        height: 100vh;
        margin: 0 auto;
    }
  
    .chat-content{
        display: flex;
        flex-direction: column;
        flex: 1;
    }
  
    .chat-messages{
        flex:1;
        font-size: 10px;
    }
  
    .message{
        font-size: 20px;
    }
  
    .user-message{
        background-color: #898a8a;
        border-radius: 5px;
        align-self: flex-end;
    }
  
    .bot-message{
        background-color: #e2e2e2;
        border-radius: 5px;
        align-self: flex-start;
    }
  
    .chat-input{
        display: flex;
        justify-content: flex-end;
    }
  
    .chat-input input {
        flex: 1;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
  
    .chat-input button {
         border-radius: 5px;
        background-color: #4caf50;
        color: #fff;
        border: none;
        cursor: pointer;
    }
  
    .chat-sidebar {
        width: 25%;
        padding: 5px;
        border-left: 1px solid #ccc;
        background-color: #4C8F9E;
    }
  
    .chat-sidebar h1 {
        color: white;
        font-family: Georgia, 'Times New Roman', Times, serif;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }
  </style>