import pandas as pd

with open('python-open.txt', 'a', encoding='utf-8') as f:
    f.write('谷世宇\n')
    print(f.tell())

d = {'b': 1, 'a': 0, 'c': 2}

s = pd.Series(d)
print(s)
d = {'one': [1., 2., 3., 4.], 'two': [4., 3., 2., 1.]}
frame = pd.DataFrame(d)
print(frame.index)
print(pd.DataFrame(d))

excel = pd.read_excel('area.xlsx', index_col=[0, 1, 2])
to_list = excel.index.to_numpy()
x = []
y = []
z = []
for l in to_list:
    x.append(l[0])
    y.append(l[1])
    z.append(l[2])

print(excel.index.to_numpy()[1][2])
print(excel.columns)
print(x, y, z)
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.scatter(x, y, z)
plt.show()
