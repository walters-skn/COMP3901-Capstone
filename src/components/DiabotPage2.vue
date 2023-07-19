<!-- <template>

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
</style> -->
<template>

  <NavBar/>

  <div class="chat-container">
    <div class="chat-sidebar">
      <h1>DIABOT <br>CHAT</h1>
    </div>
    <div class="chat-content">
      <div v-if="!greeted">
        <h2>Welcome! How can I assist you?</h2>
        <button v-on:click="startAssessment">Start Assessment</button>
      </div>
      
      <div v-else>
        <section v-if="!assessmentComplete" class="chat-messages">
          <div class="message">
            <h2 class="message-content">
              {{ question.question }}
            </h2>
          </div>
          <div class="chat-input">
            <input type="text" ref="answer" v-model="response">
            <button v-on:click="answerQuestion">Submit Answer</button>
          </div>
        </section>

        <section v-else>
          <h2>Assessment Complete!</h2>
          <h2>Your Risk</h2>
          <p>Risk Score: {{ risk_score }}</p>
          <p>Risk Category: {{ risk_category }}</p>
          <p>Chance of Developing Diabetes: {{ chance_of_diabetes }}</p>
          <p>Screening Recommendation: {{ screening_recommendation }}</p>
          <br>
          <h3>To Subscribe To Diabot, Click the Button Below </h3>
          <button v-on:click="redirectToRegister"> Register </button>
        </section>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';
import NavBar from './NavBar.vue'

export default {
  components:{
    NavBar,
  },
  name: 'ChatBox',
  data() {
    return {
      greeted: false,
      assessmentComplete: false,
      questions: [], // Array to store questions
      currentQuestionIndex: 0,
      userResponses: [],
      risk_score: 0,
      risk_category: '',
      chance_of_diabetes: '',
      screening_recommendation: '',
      question: {} // Current question object
    };
  },
  methods: {
    startAssessment() {
      this.greeted = true;
      this.getQuestions();
    },
    getQuestions() {
      axios.get(`http://localhost:5000/questions`)
        .then((response) => {
          console.log('getQuestions response:', response);
          this.questions = response.data.questions;
          this.getNextQuestion();
        })
        .catch((error) => {
          console.log('getQuestions error:', error);
        });
    },
    getNextQuestion() {
      console.log('getNextQuestion called. currentQuestionIndex:', this.currentQuestionIndex);
      if (this.currentQuestionIndex < this.questions.length) {
        this.question = this.questions[this.currentQuestionIndex];
        console.log('Displaying question:', this.question);
      } else {
        this.submitResponses();
      }
    },
    answerQuestion() {
      this.userResponses.push(this.response);
      this.currentQuestionIndex++;
      if (this.currentQuestionIndex < this.questions.length) {
        this.getNextQuestion();
      } else {
        this.submitResponses();
      }
      this.response = ''; // Clear the response input
    },
    submitResponses() {
      console.log('submitResponses called. userResponses:', this.userResponses);
      axios.post('http://localhost:5000/answers', {
        responses: this.userResponses
      })
        .then((response) => {
          console.log('submitResponses response:', response);
          this.risk_score = response.data.risk_score;
          this.risk_category = response.data.risk_category;
          this.chance_of_diabetes = response.data.chance_of_diabetes;
          this.screening_recommendation = response.data.screening_recommendation;
        })
        .catch((error) => {
          console.log('submitResponses error:', error);
        });
      this.assessmentComplete = true;
    },
    redirectToRegister(){
      this.$router.push('/register')
    }
  }
};
</script>

<style scoped>

  .chat-container {
    display: flex;
    width: 60%;
    height: 88vh;
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