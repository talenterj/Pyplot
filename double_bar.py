import matplotlib.pyplot as plt
import numpy as np

# # 这两行代码解决 plt 中文显示的问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
waters = ('cola', 'tea', 'pure water', 'juice', 'other')
buy_number_male = [6, 7, 6, 1, 2]
buy_number_female = [9, 4, 4, 5, 6]

bar_width = 0.3 # 条形宽度
index_male = np.arange(len(waters)) # 男生条形图的横坐标
index_female = index_male + bar_width # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_male, height=buy_number_male, width=bar_width, color='b', label='male',hatch = '/')
plt.bar(index_female, height=buy_number_female, width=bar_width, color='g', label='female',hatch = 'x')
#设置label的作用，在后面直接调用legend，就可以添加图例
#hatch是设置图的样式

plt.legend() # 显示图例
plt.xticks(index_male + bar_width/2, waters) # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('num') # 纵坐标轴标题
plt.title('investigate') # 图形标题

plt.show()