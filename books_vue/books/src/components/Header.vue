<!--
 * @Author: dofospider
 * @since: 2020-12-16 17:38:00
 * @lastTime: 2020-12-16 17:41:22
 * @LastAuthor: Do not edit
-->
 <template>
  <!-- <b-container fluid> -->
  <b-container>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">嗨小说</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Link0</b-nav-item>
          <b-nav-item href="#">Link1</b-nav-item>
          <b-nav-item href="#">Link2</b-nav-item>
          <b-nav-item href="#">Link3</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input
              size="sm"
              class="mr-sm-2"
              placeholder="输入图书名字或作者名字"
            ></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit"
              >开始查询</b-button
            >
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </b-container>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
</style>