# 列表
list1 = [4, 7, 1, 2]
# 函数
# len 函数返回列表中的元素个数len(list1)
# max 函数返回列表元素最大值max(list1)
# min 函数返回列表元素最小值min(list1)
# 方法
# append 方法用于在列表的末尾追加新的内容list1.append('1')
# count 方法用于统计某个元素在列表中出现的次数list1.count(1)
# extend 方法表示追加内容，它可以在列表的末尾一次性追加另一个序列中的多个值，也就是用新列表扩展原有列表list1.extend(list1)
# index 方法用于从列表中找出某个元素第一次匹配的位置的索引位置 list1.index('1')
# insert 方法用于像列表中插入对象list1.insert(3,4) 在3坐标处插入4
# pop 方法会移除列表中的一个元素（默认是最后一个），并且返回该元素的值list1.pop() == 2
# remove 方法用于移除列表中第一个匹配的元素
# reverse 方法是将列表中的元素进行反转操作
# sort 方法用于在原位置排序，‘原位置排序’意味着改变原来的列表而让列表中的元素有顺序排列
# clear 方法用于清空列表
# copy 方法是复制列表
# 列表基本操作
# list1[2] 取值
# list1[2] = 1 赋值
# del list1[3] 删除第三个元素
# list(string) 将字符串转换为list
name = list('Pyther')
print('a' in name)
# 分片赋值
name[4:] = 'on'
name
['P', 'y', 't', 'h', 'o', 'n']


# 元组
tup = ('baidu', 'google', 1, 2)
# 通用函数 min max len


# 集合
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
# remove删除，不存在报错| discard删除，不存在不报错
s.remove(3)
s.discard(7)
print(s)
print(len(s))

# ‘-’：代表前者中包含后者中不包含的元素
#
# ‘|’：代表两者中全部元素聚在一起去重后的结果
#
# ‘&’：两者中都包含的元素
#
# ‘^’：不同时包含于两个集合中的元素
a = set('afqwbracadaagfgbrafg')
b = set('rfgfgfalacazamddg')
# 集合a中包含而集合b中不包含的元素
print(a - b)
c = a.difference(b)

# 集合a或b中包含的所有元素
print(a | b)
a.union(b)

# 集合a、b都有的
print(a & b)
a.intersection(b)

# 不同时包含的
print(a ^ b)

# isdisjoint() 方法用于判断两个集合是否包含相同的元素，==如果没有返回 True，否则返回 False。==
# issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
# issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。


# 返回两个集合组成的新集合，但会移除两个集合的重复元素： union不会移除相同的元素
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.symmetric_difference(y)
v = x.union(y)
print(z)
print(v)
