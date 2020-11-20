import requests
import time
from urllib import parse


utl = 'https://vip.dmohe.com/index.php'

cookies = {
    'PHPSESSID': 'mrlhiu6iub9subsf7v6g5lc896',
    'Hm_lvt_1f4615ff33183230f77694fcb34175ad': '1605679229',
    'openid': 'p516056794757577491',
    # 'fanchang': '6',
    'Hm_lpvt_1f4615ff33183230f77694fcb34175ad': '1605679560'
}

c_file = open('./cookie.json', 'r', encoding='utf-8')
for line in c_file.readlines():
    dic = dict(line)
    if dic.get('name') == 'gushiyu':
        cookies = dic


data = {
    'step': '65434'
}

get = requests.post(url=utl, data=data, cookies=cookies)
print(get.status_code)
