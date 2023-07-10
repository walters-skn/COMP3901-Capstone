<template>
  <div class="chat-container">
    <div class="chat-sidebar">
      <h1> <b><strong>DIABOT <br> CHAT</strong></b></h1>
    </div>    
    <div class="chat-content">
      <div class="chat-messages" ref='chatMessages'>
        <div v-for="message in messages" :key="message.id" class="message" :class="{ 'user-message': message.from === 'user', 'bot-message': message.from === 'bot' }">
          <div class="message-content">
            {{ message.text }}
          </div>
        </div>
      </div>
      <div class="chat-input">
        <input v-model="inputText" @keydown.enter="sendMessage" placeholder="Type your message..." />
        <button @click="sendMessage" style="margin-right: 25px;"> <strong>SEND </strong></button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ChatBox',
  data() {
    return {
      message: '',
      messages: []
    };
  },
  methods: {
  sendMessage() {
    const message = this.inputText.trim();
    if (message) {
      this.messages.push({ id: Date.now(), text: message, from: 'user' });
      this.inputText = '';

      axios.get(`https://www.cleverbot.com/getreply?key=CC8uqcCcSO3VsRFvp5-uW5Nxvow&input=${message}`)
        .then(res => {
          this.messages.push({
            id: Date.now(),
            text: res.data.output,
            from: 'bot'
          });

          this.$nextTick(() => {
            const chatMessages = this.$refs.chatMessages;
            chatMessages.scrollTop = chatMessages.scrollHeight;
          });
        })
        .catch(error => {
          console.log('An error occurred:', error);
        });
    }
  }
}
};
</script>

<style scoped>

  .chat-container {
    display: flex;
    width: 100%;
  }

  .chat-content {
    display: flex;
    flex-direction: column;
    flex: 1;
  }

  .chat-messages {
    flex: 1;
    font-size: 10px;
    overflow-y: auto; /* Enable vertical scrolling */
    }
  .message {
    font-size: 20px;
  }

  .client {
    /* Add the styles for client messages here */
    span {
      background: #0070C8;
      padding: 8px;
      color: white;
      border-radius: 4px;
    }
    p {
      float: left;
    }
  }

  .server {
    /* Add the styles for server messages here */
    span {
      background: #99cc00;
      padding: 8px;
      color: white;
      border-radius: 4px;
    }
    p {
      float: right;
    }
  }

  .user-message {
    background-color: #c8d1d1;
    border-radius: 5px;
    align-self: flex-end;
  }

  .bot-message {
    background-color: #e2e2e2;
    border-radius: 5px;
    align-self: flex-start;
  }

  .chat-input {
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
    background-color: #4C8F9E;
    color: #fff;
    border: none;
    cursor: pointer;
  }

  .chat-sidebar {
    width: 22%;
    min-height: 84.5vh;
    padding: 2px;
    border-left: 1px solid #ccc;
    background-color: #4C8F9E;
    z-index: -1;
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
