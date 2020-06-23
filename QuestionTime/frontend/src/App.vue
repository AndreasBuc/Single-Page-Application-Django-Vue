<template>
  <div id="app">
    <div id="nav">
      <NavbarComponent />
    </div>
    <router-view />
  </div>
</template>


<script>
import NavbarComponent from "@/components/Navbar.vue";
export default {
  name: "App",
  components: {
    NavbarComponent
  }
};
</script>

<style>

</style>
