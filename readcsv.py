import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('UCS.csv','\t',skiprows = 1,header = None) #读取csv文件，分隔符指定为制表符
# 读文件方式，默认是以逗号“，”作为分割符，若是以其它分隔符，比如制表符“/t”，则需要显示的指定分隔符
# 因为原来的表格有表头，原来的表头会变成第一行数据，因此使用skiprows =1，跳过了第一行的读取。
# nrows: 读取多少行数据
# csv文件是以逗号为分隔符的文件，读取参数与excel基本类似，与excel的读取不一样的地方在于如遇到中文路径必须得设置engine参数
# header: 哪一行设置为列索引，默认是第一行，即header = 0
# header = None，表明不以表格的行为列索引，即没有表头，默认从0开始，如原来表格有列索引，则原来索引变为第一行数据；
# skiprows: 跳过前几行读取文件，默认从0开始
# print(df)

alt = df.values # 直接转成矩阵
print(alt)

x = [] #x，y声明为空矩阵
y = []
y1 = []

for a in alt:  # 从第二行开始读取
    x.append(a[0])  # 将第一列数据从第一行读取到最后一行赋给列表x
    y.append(a[1])  # 将第二列数据从第一行读取到最后一行赋给列表
    y1.append(a[2])

# plt.plot(x, y)  # 绘制x,y的折线图
# plt.plot(x, y1) # 绘制x,y1的折线图
# plt.show()  # 显示折线图

plt.figure() #声明画布
l1 = plt.scatter(x,y,s=50,c='red', marker="o",label = 'rocksdb') #画散点图,s=10是点大小，c是color
l2 = plt.scatter(x,y1,s=50,c='blue', marker="*", label = 'silk')#赋值给l1,l2是为了设置legend图例，否则直接如下格式就行
# plt.scatter(x,y,s=50,c='red', marker="o",label = 'rocksdb')
# plt.scatter(x,y1,s=50,c='blue', marker="*", label = 'silk')
plt.xlabel('time(s)') #横坐标轴标签
plt.ylabel('99 latency(us)') #纵坐标标签
plt.title('silk latency test') #标题
plt.legend(handles = [l1,l2],labels = ['rocksdb','silk'],loc = 'best')#为两个散点图设置图例，标签分别为...,loc是图例位置
plt.show()
plt.savefig(r"scatter.png")