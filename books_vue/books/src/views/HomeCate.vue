<!--
 * @Author: dofospider
 * @since: 2020-12-17 16:19:21
 * @lastTime: 2021-01-01 11:21:15
 * @LastAuthor: Do not edit
-->
<template>
  <div id="HomeCate">
    <Header />
    <b-container class="mt-4 mb-2">
      <b-row>
        <b-col cols="12" md="7">
          <h4>最新更新的小说</h4>
          <table
            role="table"
            aria-busy="false"
            aria-colcount="3"
            class="table b-table table-striped table-hover"
          >
            <thead role="rowgroup" class="">
              <tr role="row" class="">
                <th role="columnheader" scope="col" aria-colindex="1" class="">
                  <div>小说</div>
                </th>
                <th role="columnheader" scope="col" aria-colindex="2" class="">
                  <div>最新章节</div>
                </th>
                <th role="columnheader" scope="col" aria-colindex="3" class="">
                  <div>最新更新时间</div>
                </th>
              </tr>
            </thead>

            <tbody role="rowgroup">
              <tr role="row" v-for="item in items.newestItems" :key="item.id">
                <td aria-colindex="1" role="cell" class="">
                  <a :href="'/book/' + item.book_id">
                    {{ item.book_name }}
                  </a>
                </td>
                <td aria-colindex="2" role="cell" class="">
                  <a
                    :href="'/book/' + item.book_id + '/' + item.book_newest_url"
                  >
                    {{ item.book_newest_name }}
                  </a>
                </td>
                <td aria-colindex="3" role="cell" class="">
                  {{ dateFormat(item.book_last_update_time) }}
                </td>
              </tr>
            </tbody>
          </table>
        </b-col>
        <b-col cols="12" md="1"> </b-col>
        <b-col cols="12" md="4">
          <h4>最多阅读的小说</h4>
          <table
            role="table"
            aria-busy="false"
            aria-colcount="2"
            class="table b-table table-striped table-hover"
          >
            <thead role="rowgroup" class="">
              <tr role="row" class="">
                <th role="columnheader" scope="col" aria-colindex="1" class="">
                  <div>小说</div>
                </th>
                <th role="columnheader" scope="col" aria-colindex="2" class="">
                  <div>作者</div>
                </th>
              </tr>
            </thead>

            <tbody role="rowgroup">
              <tr role="row" v-for="item in items.mostItems" :key="item.id">
                <td aria-colindex="1" role="cell" class="">
                  <a :href="'/book/' + item.book_id">
                    {{ item.book_name }}
                  </a>
                </td>
                <td aria-colindex="2" role="cell" class="">
                  <a
                    :href="'/book/' + item.book_id + '/' + item.book_newest_url"
                  >
                    {{ item.book_author }}
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </b-col>
      </b-row>
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { GetInfoPost, GetInfoPosts } from "../apis/read";
import dateFormat from "../utils/data";

export default {
  name: "HomeCate",
  components: {
    Header,
    Footer,
  },

  setup(props, context) {
    const now_url = ref(context.root.$route.path);
    const newstParams = reactive({
      url: now_url.value,
      key: "newest",
    });

    const items = reactive({
      newestItems: [],
      mostItems:[],
    });
    const mostParams = reactive({
      url: now_url.value,
      key: "most",
    });

    GetInfoPost(newstParams).then((resp) => {
      console.log(resp);
      items.newestItems = resp.data.data;
    });

    GetInfoPost(mostParams).then((resp) => {
      console.log(resp);
      items.mostItems = resp.data.data;
    });

    onMounted(() => {
      console.log("In HomeCate context=", now_url);
      console.log("In HomeCate context.value=", now_url.value);
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