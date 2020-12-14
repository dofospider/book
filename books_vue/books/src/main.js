/*
 * @Author: dofospider
 * @since: 2020-12-14 10:09:27
 * @lastTime: 2020-12-15 00:53:56
 * @LastAuthor: Do not edit
 */
import { createApp } from "vue";
// import Vue from 'vue';
import App from "./App.vue";

import router from "./router";
import store from "./store";
import vueCompositionAPI from "@vue/composition-api";
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);


Vue.use(vueCompositionAPI);

Vue.config.productionTip=false;


createApp(App)
  .use(store)
  .use(router)
  .mount("#app");
