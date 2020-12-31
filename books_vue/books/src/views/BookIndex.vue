<!--
 * @Author: dofospider
 * @since: 2020-12-23 16:50:41
 * @lastTime: 2021-01-01 00:08:22
 * @LastAuthor: Do not edit
-->
<template>
  <div id="BookIndex">
    <Header />

      <b-container v-if="items.indexItems.length != 0">
        <b-row>
          <b-col md="4">
            <b-img
              thumbnail
              fluid
              class='p-3'
              style="width:80%;margin-left:10%"
              :src="items.indexItems[0].image_urls"
              alt="Image 1"
            >
            </b-img>
          </b-col>

          <b-col md="8">
            <b-jumbotron header-level="0" style="padding:3rem 1rem">
              <template v-slot:header>{{
                items.indexItems[0].book_name
              }}</template>
              <div>作者:{{ items.indexItems[0].book_author }}</div>
              <div>最新章节:{{ items.indexItems[0].book_newest_name }}</div>
              <div>
                最新更新时间:{{
                  dateFormat(items.indexItems[0].book_last_update_time)
                }}
              </div>
              <div>本书状态:{{ items.indexItems[0].book_status }}</div>

              <hr class="my-4" />
              <p> 小说简介:{{ items.indexItems[0].book_desc }}</p>
              <b-button
                pill
                variant="primary"
                class="left"
                style="float: left; margin-left: 5px"
                :href="'/book/'+items.indexItems[0].book_id+'/'+items.allCapItems[0].sort_id"
                >开始阅读</b-button
              >
              <b-button
                pill
                variant="success"
                class="right"
                style="float: right; margin-right: 5px"
                href="#"
                >加入收藏</b-button
              >
            </b-jumbotron>
          </b-col>
        </b-row>
       

        <b-row>
          <b-col><h6>最近更新的20个章节</h6></b-col>
        </b-row>
        <b-row>
          <!-- <b-col clos='12' md='4' v-for="item in items.cap20Items" :key="items.id">{{item.detail_title}}</b-col> -->
          <b-col
            clos="12"
            md="4"
            v-for="item in items.cap20Items"
            :key="items.id"
            ><a :href="'/book/' + item.book_id + '/' + item.sort_id">{{
              item.detail_title
            }}</a></b-col
          >
        </b-row>

        <b-row>
          <b-col><h6>所有章节的内容</h6></b-col>
        </b-row>
        <b-row>
          <b-col
            clos="12"
            md="4"
            v-for="item in items.allCapItems"
            :key="items.id"
            ><a :href="'/book/' + item.book_id + '/' + item.sort_id">{{
              item.detail_title
            }}</a></b-col
          >
        </b-row>
      </b-container>
    
      <b-container v-else>图书不存在
    </b-container>
    <Footer />
  </div>
</template>

<script>
// import Header from "../components/Header";
import Footer from "../components/Footer";
import Header from "../components/Header";
import { GetInfoPost } from "../apis/read";
import { reactive, ref, onMounted } from "@vue/composition-api";
import dateFormat from "../utils/data";

export default {
  name: "BookIndex",
  components: {
    Header,
    Footer,
  },
  setup(props, context) {
    const now_url = ref(context.root.$route.path);

    const indexParams = reactive({
      url: now_url.value,
      key: "index",
    });

    const cap20Params = reactive({
      url: now_url.value,
      key: "cap20",
    });

    const capAllParams = reactive({
      url: now_url.value,
      key: "all",
    });

    const items = reactive({
      indexItems: [],
      allCapItems: [],
      cap20Items: [],
    });

    GetInfoPost(indexParams).then((resp) => {
      console.log("In bookindex resp.data=", resp.data);
      items.indexItems = resp.data.data;
    });

    GetInfoPost(capAllParams).then((resp) => {
      console.log("In all_bookindex resp.data=", resp.data);
      items.allCapItems = resp.data.data;
    });

    GetInfoPost(cap20Params).then((resp) => {
      console.log("In 20bookindex resp.data=", resp.data);
      items.cap20Items = resp.data.data;
    });

    onMounted(() => {
      console.log("context.root.$router.path= ", context.root.$route.path.root);
    });
    return {
      items,
      dateFormat,
    };
  },
};
</script>

<style lang="scss" scoped>
</style>