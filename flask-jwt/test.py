import requests

url1 = 'http://127.0.0.1:5000/auth'
url2 = 'http://127.0.0.1:5000/protected'


data = {
    'username': 'user1',
    'password': 'abcxyz'
}

response = requests.post(url1, json=data)
json_get = response.json().get('access_token')
print(json_get)

auth = 'jwt ' + json_get
print(auth)

header = {
    'Authorization': auth
}
print(header)
res = requests.post(url2, headers=header)
print(res.text)
