print('{}:是世界上最好的语言，{}'.format('python', 'yes'))
print('{1}:是世界上最好的语言，{0}'.format('python', 'yes'))
# print(input('请输入你的名字'))

with open('../aaa.txt', 'r') as f:
    while True:
        a = f.readlines()
        for l in a:
            print(l, end='')

with open('./b.txt', 'a') as f:
    f.write('vvvcccxbbv')

import json

data = {'id': '1', 'name': 'jhon', 'age': 12}
d = [1, 2, 3, 4, 5]
with open('t.json', 'w') as f:
    json.dump('111', f)
with open("t.json", 'r') as f:
    d = json.load(f)
    print(d)
