/*
 * @Author: dofospider
 * @since: 2020-12-16 14:49:16
 * @lastTime: 2020-12-23 16:51:18
 * @LastAuthor: Do not edit
 */
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import HomeCate from "../views/HomeCate.vue";
import BookIndex from "../views/BookIndex.vue";


Vue.use(VueRouter);

const routes = [{ // 网站首页
    path: "/",
    name: "Home",
    component: Home
  },

  //网站分类页面
  {
    path: "/:cate_id",
    name: "HomeCate:",
    component: HomeCate
  },

  // 图书首页
{
  path:"/book/:book_id",
  name:"BookIndex",
  component:BookIndex, 
}


  // 图书详情页






  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue")
  // }
];

const router = new VueRouter({
  mode:"history",
  base:process.env.base_URL,
  routes
});

export default router;