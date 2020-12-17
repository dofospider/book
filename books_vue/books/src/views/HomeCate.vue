<!--
 * @Author: dofospider
 * @since: 2020-12-17 16:19:21
 * @lastTime: 2020-12-17 17:58:56
 * @LastAuthor: Do not edit
-->
<template>
<div id="HomeCate">
    <Header />
    <b-container>

    </b-container>
    <Footer />
</div>  
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import {ref,reactive,onMounted} from "@vue/composition-api";
import {GetInfoPost, GetInfoPosts} from"../apis/read";



export default {
    name:"HomeCate",
    comments:{
        Header,
        Footer,

    },

    setup(props, context){
        const now_url=ref(context.root.$route.path);
        const postParams=reactive({
            url:now_url.value,
            key:'newest'

        })

        GetInfoPost(postParams).then(resp=>{
            console.log(resp);
        });
        

        onMounted(()=>{
            console.log("In HomeCate context=",now_url);
            console.log("In HomeCate context.value=",now_url.value);
            
        });
        return{

        }
    }
}
</script>

<style lang="scss" scoped>

</style>