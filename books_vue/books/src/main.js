/*
 * @Author: dofospider
 * @since: 2020-12-14 10:09:27
 * @lastTime: 2020-12-14 16:39:54
 * @LastAuthor: Do not edit
 */
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vueCompositionAPI from "@vue/composition-api"

Vue.use(vueCompositionAPI);

Vue.config.productionTip=false;


createApp(App)
  .use(store)
  .use(router)
  .mount("#app");
