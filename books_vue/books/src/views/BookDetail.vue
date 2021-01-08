<!--
 * @Author: dofospider
 * @since: 2020-12-30 23:52:48
 * @lastTime: 2021-01-08 22:11:46
 * @LastAuthor: Do not edit
-->
<template>
  <div id="BookDetail">
    <Header />
    <b-container v-if ='items.detailsItems.length==1'>
      <b-row>
        <b-col>
           当前路径：<a href='/'>首页</a><a :href='"/book/"+items.detailsItems[0].book_id'> {{items.detailsItems[0].book_name}}</a>--{{items.detailsItems[0].detail_title}}
        </b-col>
      </b-row>
      <b-row><b-col> 
       <h2> {{items.detailsItems[0].detail_title}}</h2>
      </b-col> </b-row>

      <b-row>
        <b-col v-if="items.detailsItems[0].pre_id==''">
       <a :href="'/book/'+items.detailsItems[0].book_id" >上一页</a>
        </b-col>
        <b-col v-else><a :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].pre_id" >上一页</a></b-col>
        <b-col><a :href='"/book/"+items.detailsItems[0].book_id'>目录</a> </b-col>

        <b-col v-if="items.detailsItems[0].next_id==''">
          <a :href="'/book/'+items.detailsItems[0].book_id" >下一页</a> </b-col>
        <b-col v-else>
          <a :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].next_id" >下一页</a> </b-col>  
          </b-row>
      <b-row> <b-col>
        <h2>{{items.detailsItems[0].detail_content}}</h2>
        </b-col></b-row>
      
      

      <b-row>
        <b-col v-if="items.detailsItems[0].pre_id==''">
       <a :href="'/book/'+items.detailsItems[0].book_id" >上一页</a>
        </b-col>
        <b-col v-else><a :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].pre_id" >上一页</a></b-col>
        <b-col><a :href='"/book/"+items.detailsItems[0].book_id'>目录</a> </b-col>

        <b-col v-if="items.detailsItems[0].next_id==''">
          <a :href="'/book/'+items.detailsItems[0].book_id" >下一页</a> </b-col>
        <b-col v-else>
          <a :href="'/book/'+items.detailsItems[0].book_id+'/'+items.detailsItems[0].next_id" >下一页</a> </b-col>  
          </b-row>

    </b-container>
    <b-container>
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { ref, reactive } from "@vue/composition-api";
import { GetInfoPost } from "../apis/read";
export default {
  name: "BookDetail",
  components: {
    Header,
    Footer,
  },

  setup(props, context) {
    const detailPrams = reactive({
      url: context.root.$route.path,
      key: "",
    });

    const items = reactive({
      detailsItems: [],
    });
    GetInfoPost(detailPrams).then(resp => {
      console.log('book detail',resp.data.data);
      items.detailsItems = resp.data.data;
    });

    return {
      items,
    };
  },
};
</script>

<style lang='scss' scoped>
</style>