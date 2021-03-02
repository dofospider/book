<!--
 * @Author: dofospider
 * @since: 2020-12-16 14:49:16
 * @lastTime: 2021-02-02 23:47:39
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
import { GetInfoPost  } from "../apis/read";
import { ref, reactive,onMounted} from "@vue/composition-api";

export default {
  name: "Home",
  components: {
    Header,
    Footer,
  },
  setup(props,context){
    
    const titlePramas=reactive({
      url:'/title',
      key:'index',

    });

    GetInfoPost(titlePramas).then(resp=>{
      console.log("In home title=",resp.data.data);
      document.title=resp.data.data[0];
      document.querySelector("meta[name='keywords']").setAttribute("context",resp.data.data[1]);
      document.querySelector("meta[name='description']").setAttribute("context",resp.data.data[2]);

    });


  }
};
</script>
