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
