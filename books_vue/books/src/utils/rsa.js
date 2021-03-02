/*
 * @Author: dofospider
 * @since: 2021-01-09 17:57:27
 * @lastTime: 2021-01-09 23:46:55
 * @LastAuthor: Do not edit
 */
import { JSEncrypt  }  from "jsencrypt";

export function rsaEncrypt(data){
    
    console.log("in RSA data=",data);

    const publicKey="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCz2Qt3zfz85BrPvNos1MsuUQ2I5qzjdzBxMJ1tcVTEO7oa6cL8HhaAeUoldDZhHiNhAqrN2sv2kX3qrInB7EKLFMhA3sGfweS/1/CEm10Lvd462rxD/8+wG69fS2uRY3ZiA2xA9tO23fL87VsNK1fPV6YzfObdslz1Eyi4gjEYEwIDAQAB";
    const jse = new JSEncrypt;
    jse.setPublicKey(publicKey)
    const result = jse.encrypt(data)


    console.log("in RSA result=",result);
    return result
}