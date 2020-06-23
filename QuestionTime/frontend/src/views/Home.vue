<template>
  <div class="home">
    <div class="container">
      <div v-for="question in questions" :key="question.pk">
        <p class="mb-0">Posted by:
          <span class = "question-author">{{question.author}}</span>
        </p>
        <h2>
          <router-link
            :to="{ name: 'question', params: {slug: question.slug} }"
            class="question-link"
          >{{question.content}}
          </router-link>
        </h2>
        <p>Answers: {{question.answers_count}}</p>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "home",
  data() {
    return {
      questions: [],
      next: null,
      loadingQuestions: false
    }
  },
  methods: {
    getQuestions() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/api/questions/";
      apiService(endpoint)
      .then(data => {
        this.questions.push(...data.results)
      })
    }
  },
  created() {
    this.getQuestions()
    document.title = "Question Time"
  }
};
</script>

<style media="screen" scoped>
  .question-author{
    color: #005b96;
  }
  .question-link{
    color: #011f4b;
  }
  .question-link:hover{
    color: #b3cde0;
    text-decoration: none;
  }

</style>
