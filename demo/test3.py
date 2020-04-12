import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017','2018','2019']

# 定义2个列表分别作为两条折线的Y轴数据
y_data = [56000, 62200, 64000, 73000, 85600, 92500, 120000,135000,146000]
y_data2 = [51000, 53200, 54500,56300, 57500, 59800, 64700,68900,72900]

import matplotlib.font_manager as fm
# 使用Matplotlib的字体管理器加载中文字体
my_font=fm.FontProperties(fname="C:\Windows\Fonts\simkai.ttf")

# 指定折线的颜色、线宽和样式
plt.plot(x_data, y_data, color = 'red', linewidth = 2.0,
         linestyle = '--', label='Juna')
plt.plot(x_data, y_data2, color = 'blue', linewidth = 3.0,
         linestyle = '-.', label='July')

# 调用legend函数设置图例
plt.legend(loc='best')

# 设置数据图的标题
plt.title('Sale Amount in Juna or July')

# 设置两条坐标轴的标签
plt.xlabel("Year")
plt.ylabel("Sale")

# 设置Y轴上的刻度值：第一个参数是点的位置，第二个参数是点的文字提示
plt.yticks([60000, 85000, 120000],[r'Good', r'Wonderful', r'Hot'])

# 调用show()函数显示图形
plt.show()
