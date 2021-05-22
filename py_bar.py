# 导入相关的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 定义画布的大小
fig = plt.figure(figsize = (15,8))

# 添加主标题
plt.title("sales")

# 设置X周与Y周的标题
plt.xlabel("brand")
plt.ylabel("sales num")

# 显示网格线
plt.grid(True)

# 设置 x轴 数据
x = np.array(["BMW","BENC","AODI","MAZID"])

# 设置 y 数据,四季度
y1 = np.array([1000,800,600,400])
y2 = np.array([200,800,100,400])
y3 = np.array([300,800,600,400])
y4 = np.array([4000,800,600,400])


# 直接绘制简单的柱状图
# plt.bar(x,y)

# 绘制柱状图，并把每根柱子的颜色设置为洋红色
# plt.bar(x,y,color = "m")

# 绘制柱状图，并把每根柱子的颜色设置为洋红色，顺便设置每根柱子的宽度
# plt.bar(x,y,color = "m",width = 0.6)

# 绘制柱状图，并给每根柱子的颜色根据自己的喜好来自定义
plt.bar(x,y1)
plt.bar(x,y2)

# 保存输出绘制的图形到指定的路径中
plt.show()