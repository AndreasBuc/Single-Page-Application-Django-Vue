<template>
  <div>
    <p class="muted mb-1"><small> <span class="author">{{answer.author}}</span> &#8901; {{ answer.created_at }}</small></p>
    <p class="mb-4">{{ answer.body }}</p>
  </div>
</template>

<script>
  export default {
    name: "AnswerComponent",
    props: {
      answer: {
        type: Object,
        required: true,
      }
    }
  }
</script>

<style scoped>
.author{
  color: #005b96;
}
</style>
