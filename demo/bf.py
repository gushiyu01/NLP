from bs4 import BeautifulSoup
import requests


url = 'http://127.0.0.1:5000/'
s = requests.Session()
index = s.get(url)


soup = BeautifulSoup(index.text, features='lxml')

print(soup)
print(soup.input)
print(soup.input['value'])
csrf_token = soup.input['value']
params = {
    'csrf_token': csrf_token,
    'username': 'lily',
    'password': '123'
}
response = s.post('http://127.0.0.1:5000/login/', params)
print(response.text)
response2 = s.get(url + 'index2')
print(response2.text)

from pyquery import PyQuery as pq

pp = pq(index.text)
print(pp)
print(pp('input')('#csrf_token').attr('value'))
