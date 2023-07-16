<template>

  <NavBar/>
  
  <div class="chat-container">
    <div class="chat-sidebar">
      <h1><b><strong>DIABOT <br> CHAT</strong></b></h1>
    </div>
    <div class="chat-content">
      <div class="chat-messages" ref="chatMessages">
        <div v-for="message in messages" :key="message.id" class="message" :class="message.from">
          <div class="message-content">
            {{ message.text }}
          </div>
        </div>
        <div v-if="!greeted && messages.length === 0" class="message bot">
          <div class="message-content">
            Welcome! How can I assist you?
          </div>
          <div class="message-content">
            <button @click="startAssessment">Start Assessment</button>
          </div>
        </div>
      </div>
      <div class="chat-input">
        <input v-model="inputText" @keydown.enter="sendMessage" placeholder="Type your message..." />
        <button @click="sendMessage"><strong>SEND</strong></button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from './NavBar.vue';

export default {
  name: 'ChatBox',
  components: {
    NavBar,
  },
  data() {
    return {
      inputText: '',
      messages: [],
      greeted: false,
    };
  },
  methods: {
    startAssessment() {
      this.greeted = true;
      this.messages.push({
        id: Date.now(),
        text: 'Start Assessment',
        from: 'user',
      });
    },
    sendMessage() {
      const message = this.inputText.trim();
      if (message) {
        this.messages.push({ id: Date.now(), text: message, from: 'user' });
        this.inputText = '';

        axios
          .get(`https://www.cleverbot.com/getreply?key=CC8uqcCcSO3VsRFvp5-uW5Nxvow&input=${message}`)
          .then((res) => {
            this.messages.push({
              id: Date.now(),
              text: res.data.output,
              from: 'bot',
            });

            this.$nextTick(() => {
              const chatMessages = this.$refs.chatMessages;
              chatMessages.scrollTop = chatMessages.scrollHeight;
            });
          })
          .catch((error) => {
            console.log('An error occurred:', error);
          });
      }
    },
  },
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
  overflow-y: auto;
}

.message {
  font-size: 20px;
  margin-bottom: 10px;
}

.user {
  align-self: flex-end;
  text-align: right;
}

.bot {
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
