/*
 * @Author: dofospider
 * @since: 2020-12-16 23:45:17
 * @lastTime: 2020-12-25 00:36:39
 * @LastAuthor: Do not edit
 */
import service from "../utils/request.js";

export function GetCates() {
    return service.request({
        method: "get",
        url: "/books_cates"
    })
}

export function GetInfoPost(postParams) {
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            key: postParams.key,
            secretKey:'',
            
        }
    })
    
}