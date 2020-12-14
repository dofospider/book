<!--
 * @Author: dofospider
 * @since: 2020-12-14 10:09:27
 * @lastTime: 2020-12-14 10:57:31
 * @LastAuthor: Do not edit
-->
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App123" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {
    HelloWorld
  }
};
</script>
