<!--
 * @Author: dofospider
 * @since: 2021-01-06 22:44:43
 * @lastTime: 2021-01-08 23:26:10
 * @LastAuthor: Do not edit
-->
<template>
  <div id="BookSearch">
    <Header />
    <b-container>
      <b-row
        ><b-col><h4>查询结果</h4></b-col></b-row
      >

      <b-row>
        <b-col v-if="searchResult.items.length>0">
          <table
            role="table"
            aria-busy="false"
            aria-colcount="3"
            class="table b-table table-striped table-hover"
            id="search table"
          >
            <thead role="row" class="">
              <tr role="row" class="">
                <th role="columnheader" scope="col" aria-colindex="1" class="">
                  <div>图书名字</div>
                </th>
                <th role="columnheader" scope="col" aria-colindex="2" class="">
                  <div>作者</div>
                </th>
                <th role="columnheader" scope="col" aria-colindex="3" class="">
                  <div>最新章节</div>
                </th>
              </tr>
            </thead>

            <tbody role="rowgroup">
              <tr role="row" v-for="item in searchResult.items" :key="item.id">
                <td aria-colindex="1" role="cell" class="">
                 <a :href="'/book/'+item.book_id">{{ item.book_name }}</a> 
                </td>
                <td aria-colindex="2" role="cell" class="">
                  <a :href="'/book/'+item.book_id">{{ item.book_author }}</a>
                </td>
                <td aria-colindex="3" role="cell" class="">
                  <a :href="'/book/'+item.book_id+'/'+item.book_newest_url">{{ item.book_newest_name }}</a>
                </td>
              </tr>
            </tbody>
          </table>
        </b-col>
        <b-col v-else>
          <h4>您要查询的图书不在，请您确认后，重新查询。</h4>
        </b-col>
      </b-row>
      <!-- <h2>it's a search page</h2>
      {{searchResult.items[0]}} -->
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { reactive } from "@vue/composition-api";
import { GetInfoPost } from "../apis/read";

export default {
  name: "BookSearch",
  components: {
    Header,
    Footer,
  },

  setup(props, context) {
    const searchParma = reactive({
      url: "/search",
      key: context.root.$route.query.q,
    });

    const searchResult = reactive({
      items: [],
    });

    GetInfoPost(searchParma).then(resp => {
      console.log('book Search',resp.data.data);
      searchResult.items = resp.data.data;
    });
    return {
      searchResult,
    };
  },
};
</script>

<style lang="scss" scoped>
</style>