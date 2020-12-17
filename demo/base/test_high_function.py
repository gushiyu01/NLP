import math


def high_func(f, arr):
    return [f(x) for x in arr]


def square(n):
    return n ** 2


# 使用python自带数学函数 阶乘
print(high_func(math.factorial, list(range(10))))
# print out: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# 使用自定义函数
print(high_func(square, list(range(10))))

# print(math.acos(60)) 弧度 弧长与半径之比 round(1.999，2) 1.999四舍五入 保留2位小数 2.00
print(round(math.sin(math.pi / 6), 1))

print(list(map(square, list(range(10)))))

print('*' * 40)

# 注意，现在 reduce() 函数已经放入到functools包中。
from functools import reduce

result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 5)

print(result)
# print out 15
print('*' * 40)
import os

print(os.path.join('/a' + '/b' + '/c'))

print('*' * 40)
print(" ".join('dddddddd'))
print('*' * 40)
# map(function,sequence)：把sequence中的值当参数逐个传给function，
# 返回一个包含函数执行结果的list。如果function有两个参数，即map(function,sequence1,sequence2)
print(list(map(lambda x: x * x, range(1, 21))))
# reduce(function,sequence)：function接收的参数个数只能为2，先把sequence中第一个值和第二个值当参数传给function，
# 再把function的返回值和第三个值当参数传给function，然后只返回一个结果
from functools import reduce

print(reduce(lambda x, y: x + y, range(1, 101)))
# filter(function,sequence)：对sequence中的item依次执行function(item)，
# 将执行结果为True的item组成一个List/String/Tuple(取决于sequence的类型)返回
print(list(filter(lambda x: x == 'g', 'abcdefghijk')))

l1 = [1, 9, 5, 7, 8, 6, 3, 4, 0]
l2 = ['abc', 'abd', 'aaa', 'aee']
print(sorted(l2, reverse=True))
print(sorted(l2, reverse=False))
