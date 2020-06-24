<template>
  <div class="container mt-2">
    <h1 class="mb-3">Ask a Question</h1>
    <form @submit.prevent="onSubmit">
      <textarea rows="3" class="form-control" placeholder="What would you like to ask" v-model="question_body"></textarea>
      <br>
      <button class="btn btn-outline-dark" type="submit">Publish</button>
    </form>
    <p class="muted mt-2" v-if="error">{{error}}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "QuestionEditor",
  data(){
    return {
      question_body: null,
      error: null
    }
  },
  methods: {
    onSubmit(){
      if(!this.question_body){
        this.error = "You cannot send an empty Question!";
      } else if (this.question_body.length > 240) {
        this.error = "Ensure this field has no more than 240 char ";
      } else {
        let endpoint = "/api/questions/";
        let method = "POST";
        apiService(endpoint, method, { content: this.question_body })
        .then(question_data => {
          this.$router.push({
            name: 'question',
            params: {
              slug: question_data.slug
            }
          })
        })
      }
    }
  },
  created() {
    document.title = "Editor - Question Time"
  }
}
</script>

<style>

</style>
