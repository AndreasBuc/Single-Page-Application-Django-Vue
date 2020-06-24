<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand" href="#">
        <router-link
          :to="{ name: 'home' }"
          class="navbar-brand"
          >QuestionTime
        </router-link></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
        </ul>

        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link
              :to="{name: 'home'}"
              class = "nav-link">
              Home
            </router-link>
          </li>

          <li class="nav-item active">
            <router-link
              class = "nav-link"
              :to="{ name: 'question-editor' }"
              >Ask Question
            </router-link>
          </li>

          <li class="nav-item active">
            <a class="nav-link" href="/accounts/logout/"
              >Logout
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style>
  .navbar-brand:hover {
    color: #f6abb6 !important;
  }
  .nav-link:hover {
    color: #eec9d2 !important;
  }
</style>
