/*
 * @Author: dofospider
 * @since: 2020-12-16 23:45:17
 * @lastTime: 2020-12-17 00:02:38
 * @LastAuthor: Do not edit
 */
import service from "../utils/request.js";

export function GetCates() {
    return service.request({
        method: "get",
        url: "/books_cates"
    })
}