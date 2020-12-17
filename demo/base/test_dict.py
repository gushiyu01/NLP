# 与Java的map类似
dict1 = {'name': 'gushiyu', 'age': 18, 'gender': 'male'}

print(dict1['name'])
dict1['hobby'] = ['football', 'basketball', 'pingpang']
print(dict1)
# 函数
# 字典元素个数
print(len(dict1))
# tostring
print(str(dict1))
# 判断类型
print(type(1))
print(type('1'))
print(type(dict1))
# copy

# 浅拷贝: 引用对象  赋值
dict2 = dict1
# 深拷贝
dict3 = dict1.copy()

# get取值 如果值不存在 则返回 1
print(dict3.get('22', 1))

# 遍历字典
for key, values in dict1.items():
    print(key, '已经', values, '了')
# 取出全部的key value
print(dict1.keys())
print(list(dict1.keys()))
print(dict1.values())
print(list(dict1.values()))

# 判断是否存在
if 'name' in dict1:
    print(111)

# Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。

dict = {'Name': 'Mary', 'Age': 17}
dict2 = {'Sex': 'female', 'Age': 19}

# 将 dict2 中的结果添加到字典 dict 中　
dict.update(dict2)
print("更新字典 dict : ", dict)
print(dict.setdefault('a', 20))
print(dict)

print(dict.pop('Age', 25))
print(dict)
# 类似栈，先进后出
print(dict.popitem())
print(dict)
