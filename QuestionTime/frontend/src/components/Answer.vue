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
    <div v-else >
      <button
      class = "btn btn-sm"
      @click="toggleLike"
        :class="{
          'btn-info': userLikedAnswer,
          'btn-outline-info': !userLikedAnswer
        }">
        Like [{{likesCounter}}]
      </button>
    </div>

  </div>

</template>

<script>
  import { apiService } from "@/common/api.service.js";
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
    data() {
      return {
        userLikedAnswer: this.answer.user_has_voted,
        likesCounter: this.answer.likes_count,
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
      },
      toggleLike() {
        this.userLikedAnswer === false
          ? this.likeAnswer()
          : this.unlikeAnswer()
      },
      likeAnswer() {
        this.userLikedAnswer =  true;
        this.likesCounter += 1;
        let endpoint = `/api/answers/${this.answer.id}/like/`;
        apiService(endpoint, "POST")
      },
      unlikeAnswer() {
        this.userLikedAnswer =  false;
        this.likesCounter -= 1;
        let endpoint = `/api/answers/${this.answer.id}/like/`;
        apiService(endpoint, "DELETE")
      }
    }
  }
</script>

<style scoped>
.author{
  color: #005b96;
}
</style>
