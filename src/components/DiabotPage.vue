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
          this.risk_score = response.data.total_risk_score;
          this.risk_category = response.data.risk_category;
          this.chance_of_diabetes = response.data.chance_of_diabetes;
          this.screening_recommendation = response.data.screening_recommendation;
        })
        .catch((error) => {
          console.log('submitResponses error:', error);
        });
      this.assessmentComplete = true;
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