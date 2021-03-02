#!/usr/bin/env python
# coding=UTF-8
'''
Author: dofospider
since: 2020-12-13 00:07:39
lastTime: 2021-02-03 00:41:59
LastAuthor: Do not edit
'''
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'read_books'
MYSQL_PASSWORD = 'resetf1'
MYSQL_DATABASE = 'books'
MYSQL_CHARSET = 'utf8'

BOOK_LIST = [
    'xuanhuan',
    'xiuzhen',
    'dushi',
    'lishi',
    'wangyou',
    'kehuan',
    'yanqing',
    'qita',
    'quanben',
]

RSA_1024_PRIV_KEY = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQCz2Qt3zfz85BrPvNos1MsuUQ2I5qzjdzBxMJ1tcVTEO7oa6cL8HhaAeUoldDZhHiNhAqrN2sv2kX3qrInB7EKLFMhA3sGfweS/1/CEm10Lvd462rxD/8+wG69fS2uRY3ZiA2xA9tO23fL87VsNK1fPV6YzfObdslz1Eyi4gjEYEwIDAQABAoGAccqwYNsqaPACrtH00UzKScHq6GXbmgh91ABIe0irs4V+2SxyvIZlAmC7szr2dThWdjjzzU/UoWuo2eTVPKe56amZ0Lq1d7jZMWAnCej51nKE8nRNYS7rZ0/YC8QFooeRRdPMAha+UIQHIwVo/dHUAUNzhKy+sY8rZU8RUkMrL0ECQQDoO7iCOhWGy+ZiyZQlOapxY3RS8Lg7TH9dIC+zCrn8Vz1LX4cyCQNgcc9PcIFe8zBSjSW/Ot1H3+D6bY90TRrjAkEAxkDgsSU6DoqxErcumAVtvidy5LLOCN1J1s0l3XD9Dh9R7cMfhQCXDUsA3cPN83lPDHoRIoR85EDeivQflKqlEQJBANzIujeExSZr/1H31tI1Kqe2J8cad+xYY9XDXdXX4s3Wmr1nyn51NzKfwLoDedstVMmGy1YsvmcwnxE2y+WD0IUCQAiBqCJxsngFQ2vGKF2lffv2vVtKwMRomk55JvLFclY0ydMl2Chgyhpr6XGagS+9OMMUSb/tZ15z2hikOOasG8ECQQCBKCy69B/VRpHB33gYCvYvJiC/iM8VSFSh4k9hF0lu23Z+pnkBiKjch+u5KuKMAT0mbXiVu0egAVTsx2xqNC95\n-----END RSA PRIVATE KEY-----'

REQUEST_LISTS=[
    'book.dofospider.com'
]

TITLES={
    'book.dofospider.com':{
        "index":["dofospider's book","dofospider's keywords","dofospider's description"]
    }
}