<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit your Answer</h1>
    <form @submit.prevent="onSubmit">
      <textarea
                rows="3"
                class="form-control"
                v-model="answerBody"></textarea>
      <br>
      <button class="btn btn-outline-dark" type="submit">Publish</button>
    </form>
    <p  class="muted mt-2"
        v-if="error">{{error}}</p>
  </div>
</template>


<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "AnswerEditor",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      questionSlug: null,
      answerBody: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if (this.answerBody) {
        let endpoint = `/api/answers/${this.id}/`;
        apiService(endpoint, "PUT", { body: this.answerBody })
          .then(() => {
            this.$router.push({
              name: "question",
              params: { slug: this.questionSlug }
            })
          })
      } else {
        this.error = "You can't submit an empty answer!";
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // get the answer's data from the REST API and set two data properties for the component
    let endpoint = `/api/answers/${to.params.id}/`;
    let data = await apiService(endpoint);
    return next(vm => (
      vm.answerBody = data.body,
      vm.questionSlug = data.question_slug
    ));
  }
};
</script>

<style media="screen">

</style>
