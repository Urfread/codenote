import matplotlib.pyplot as plt
plt.figure()  # 创建一个新的图形
x=[1,2,3,4]
y=[1,2,1,2]
plt.plot(x, y)  # x 和 y 的值
plt.title('title')  # 添加标题
plt.xlabel('X')  # X轴标签
plt.ylabel('Y')  # Y轴标签
plt.show()  # 显示图形
#plt.grid(True)  # 显示网格