import numpy as np

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

aa = np.array(a)
bb = np.array(b)
res = aa*bb
print(res)
print(res.dtype)
print(np.empty((3, 4)))
print(np.linspace(1, 10, 6))
print(np.arange(1, 10, 1))
arange = np.arange(12)
reshape = arange.reshape(2, 6)
print(reshape)
np_arange = np.arange(10)
print(np_arange)

x = np_arange.reshape(2, 5)
print(x)
print()
print(x[1, 3])
y = np.arange(35).reshape(5, 7)
print(y)
b = y > 20
print(b)
print(y[b])

# import matplotlib.pyplot as plt
# image = plt.imread('C:/Users/dell/Desktop/服务器.png')
# print(image.shape)
# image_crop = image[300:, ::, ::]
# plt.imshow(image_crop)
# plt.show()


# 连接两个字符串：
print(np.char.add(['hello'], [' world']))

# 连接多个字符串
print(np.char.add(['hello', 'hi'], [' world', ' Tracy']))

print(np.char.multiply('hello', 3))
print(np.char.multiply(['hello', 'hi'], 3))

print(np.char.center("gsy", 69, "*"))
print(np.char.capitalize('gsy shi hao ren'))
print(np.char.title(['gsy', 'shi', 'hao', 'ren']))

import numpy as np

print(np.char.center('msort() 函数', 20, '*'))
msa = np.array([[3, 7, 12, 45], [9, 1, 0, 34]])
print(np.msort(msa))
print(bin(13))
