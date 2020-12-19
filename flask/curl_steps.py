import requests
import random
import math

steps = math.ceil(random.random()*10000)+50000
username = '13523511140'
password = '123456'
url = 'https://www.gushiyu.cn/changeSteps?username=' + username + '&password=' + password + '&steps=' + str(steps)

request = requests.request(method='GET', url=url)

print(request.text)

print(steps)
