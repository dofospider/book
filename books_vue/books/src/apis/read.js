/*
 * @Author: dofospider
 * @since: 2020-12-16 23:45:17
 * @lastTime: 2021-02-03 00:24:40
 * @LastAuthor: Do not edit
 */
import service from "../utils/request.js";
import { rsaEncrypt } from "../utils/rsa";

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
            secretKey:rsaEncrypt(new Date().getTime()+':'+"book.dofospider.com"+':'+"other_infos"),
            
        }
    })
    
}