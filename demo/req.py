import requests


res = requests.get('http://www.baidu.com')

print(res.content.decode(encoding='utf-8'))
print(res.status_code)
print(res.encoding)
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)


from PIL import Image
from io import BytesIO

r = requests.get('http://img.sccnn.com/bimg/326/203.jpg')
print(r.content)
bi = BytesIO(r.content)
print(bi)
i = Image.open(bi)
print(i)

import requests
from requests.auth import HTTPBasicAuth

#请将username和password替换成自己在该网站的登录用户名和密码
res = requests.get('http://127.0.0.1:5000/login/', auth=HTTPBasicAuth('lily', '123'))
print(res.text)

import re


r = re.match(r'1\d+', '123')
print(r.group())

regex = '\s'
test = '021- 1101101 10'
sub = re.sub(regex, '', test)
re.sub(r'\s', '', test)
print(sub)


def num(match):
    value = int(match.group('num'))
    return str(value + 100)


test = 'abc12defg980'
rr = re.findall(r'\d+', test)
result = re.sub(r'(?P<num>\d+)', num, test)
print(result)
print(rr)

