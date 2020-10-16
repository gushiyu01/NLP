from urllib.request import urlopen
from urllib.parse import urlencode
import json
import urllib.error
# 设置超时时间为0.1s

try:
    response = urlopen("http://117.160.193.17:8103/yl/deviceHistoryLocation/findWithPage?currentPage=1&pageSize=9999&bindName=", timeout=0.01)
    decode = json.loads(response.read().decode())
    print(decode)
    print(decode['msg'])
    print(decode.get('code'))
except urllib.error.URLError as e:
    print(e.reason)

# 创建一个 HTTP POST 请求，输出响应上下文

data = {'start': 0, 'limit': 5}
data = bytes(urlencode(data), encoding='utf-8')
response = urlopen("http://117.160.193.17:8102/ictbda_api/liedata/pageList", data)
print(response.read().decode())
print(data)


