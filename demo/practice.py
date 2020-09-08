import random
import logging

print(random.random())

print(random.randint(0, 10))
print(random.uniform(2, 5))
# sample(sequence, k)函数可以获取从总体序列或集合中选择的唯一元素的k长度列表。sample()函数不会修改原有序列，它主要用在无重复的随机抽样场景，实现从大量样本中快速进行抽样。例如：
lst = [1, 2, 3, 4, 5]
print(random.sample(lst, 4))

# choice(sequence)函数可以从非空序列 sequence 中随机返回一个数，参数 sequence 表示一个有序类型，可以包含 list、tuple 等。例如：
strlist = ['C++', 'C#', 'Java', 'Python']
strtemp = ('Do you love python')
print(random.choice(strlist))
print(random.choice(strtemp))

# shuffle(x[, random])函数可以将一个有序列表中的元素打乱，再重新排序。例如：
lst = ['A', 'B', 'C', 'D', 'E']
random.shuffle(lst)
print(lst)
# 指定日志打印级别
# logging.basicConfig(level=logging.DEBUG)


# 日志信息记录到文件
logging.basicConfig(filename='F:/example.log', level=logging.DEBUG)

logging.warning("aaaa")
logging.error("aaaa")
logging.debug("aaaa")


from pathlib import Path
currentPath = Path.cwd()
homePath = Path.home()
print("文件当前所在目录:%s\n用户主目录:%s" %(currentPath, homePath))


import calendar
print(calendar.monthrange(2019, 10))

print(calendar.weekday(2019,10,7))
print(calendar.month_abbr[9])


import math

# 向上取整
print(math.ceil(-1))
# 向下取整
print(math.floor(1.024))
# 开方
print(math.sqrt(4))
# 绝对值
print(math.fabs(-8))
# 阶乘
print(math.factorial(8))
# 取余数
print(math.fmod(8, 3))

print(math.frexp(1024))
print(2**11)
print(math.fsum([1,2,3,4,5,6]))

