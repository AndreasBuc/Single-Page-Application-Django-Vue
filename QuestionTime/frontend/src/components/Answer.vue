<template>
  <div>
    <p class="muted mb-1"><small> <span class="author">{{ answer.author }}</span> &#8901; {{ answer.created_at }}</small></p>
    <p class="mb-4">{{ answer.body }}</p>

    <div v-if="isAnswerAuthor">
      <router-link
        :to="{ name: 'answer-editor', params: { id: answer.id } }"
        class="btn btn-sm btn-outline-secondary mr-1"
        >Edit
      </router-link>

        <button
        @click="triggerDeleteAnswer"
        class="btn btn-sm ml-1 btn-outline-danger">
        Delete</button>

    </div>

  </div>

</template>

<script>
  export default {
    name: "AnswerComponent",
    props: {
      answer: {
        type: Object,
        required: true,
      },
      requestUser: {
        type: String,
        required: true,
      }
    },
    computed: {
      isAnswerAuthor() {
        return this.answer.author === this.requestUser;
      }
    },
    methods: {
      triggerDeleteAnswer() {
      // emit an event to delete an answer instance
      this.$emit("delete-answer", this.answer)
    }
    }
  }
</script>

<style scoped>
.author{
  color: #005b96;
}
</style>
