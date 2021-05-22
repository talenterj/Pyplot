# 导入相关的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 在线显示
%matplotlib inline

# 定义画布的大小
fig = plt.figure(figsize = (15,8))

# 添加主标题
plt.title("各品牌汽车的销量")

# 设置X周与Y周的标题
# plt.xlabel("品牌")
# plt.ylabel("销量")

# 显示网格线
# plt.grid(True)

# 设置 x轴 数据
x = np.array(["宝马","奔驰","奥迪","马自达","大众","布加迪","兰博基尼","法拉利","本田","丰田"])

# 设置 y轴 数据
y = np.array([1000,800,600,400,300,250,150,100,80,50])

# 直接绘制简单的柱状图
# plt.bar(x,y)

# 绘制柱状图，并把每根柱子的颜色设置为洋红色
# plt.bar(x,y,color = "m")

# 绘制柱状图，并把每根柱子的颜色设置为洋红色，顺便设置每根柱子的宽度
# plt.bar(x,y,color = "m",width = 0.6)

# 绘制柱状图，并给每根柱子的颜色根据自己的喜好来自定义
plt.bar(x,y,color = ["red","yellow","green","blue","black","gold","pink","purple","violet","Chocolate"])

# 保存输出绘制的图形到指定的路径中
plt.savefig(r"C:\Users\QDM\Desktop\car.png")