from urllib import request, parse

getUrl = 'http://117.160.193.17:8103/yl/deviceHistoryLocation/findWithPage?currentPage=1&pageSize=9999&bindName='
postUrl = 'http://117.160.193.17:8102/ictbda_api/liedata/pageList'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# get请求
req = request.Request(url=getUrl, method='GET', headers=headers)
res = request.urlopen(req)

print(res.read().decode())

# post请求
data = {'start': 0, 'limit': 5}
data = bytes(parse.urlencode(data), encoding='utf-8')

req2 = request.Request(url=postUrl, method='POST', data=data, headers=headers)
res2 = request.urlopen(req2)

print(res2.read().decode())

l = [1, "2", {}, "abc"]
import random

choice = random.choice(l)
print(choice)



# 解析并输出 url 中每个字段的字符串
import urllib
url = 'http://www.baidu.com/urllib.parse.html;python?kw=urllib.parse#module-urllib'
result = urllib.parse.urlparse(url)
print(result)
print(result.scheme, result.netloc, result.path, result.params, result.query, result.fragment, sep = '\n')
# 解码经过 quote 函数处理后的 url，输出解码后的结果。
import urllib
url = 'http://www.baidu.com/爬虫'
result = urllib.parse.quote(url)
print(result)
result = urllib.parse.unquote(url)
print(result)

# 使用两种爬虫代理分别查看是否可以对 'http://www.baidu.com' 网站进行爬取
from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url("http://www.baidu.com/robots.txt")
rp.read()
print(rp)
print(rp.can_fetch('Baiduspider', 'http://www.baidu.com'))
print(rp.can_fetch('*', 'http://www.baidu.com'))
