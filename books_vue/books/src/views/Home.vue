<!--
 * @Author: dofospider
 * @since: 2020-12-16 14:49:16
 * @lastTime: 2021-01-08 23:42:11
 * @LastAuthor: Do not edit
-->
<template>
  <div class="home">
    <Header />

    <b-container>
      <div style="height: 1000px; background-color: red">body part</div>
    </b-container>

    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";

export default {
  name: "Home",
  components: {
    Header,
    Footer,
  },
  setup(props,context){
    document.title="蜘蛛大人的小说";
    document.querySelector("meta[name='keywords']").setAttribute("content","蜘蛛大人的keywords");
    document.querySelector("meta[name='description']").setAttribute('content',"蜘蛛大人的descrption");

  }
};
</script>
