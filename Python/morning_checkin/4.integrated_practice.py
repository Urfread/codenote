import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('morning_times.csv')

# 将 'Date' 和 'Time' 列合并为 'DateTime' 列
df['DateTime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'])

# 提取日期作为横坐标
dates = df['DateTime'].dt.date

# 提取时间作为字符串格式的纵坐标
times_str = df['DateTime'].dt.strftime('%H:%M')

print(dates)
print(times_str)

# 使用matplotlib绘制图形
plt.figure(figsize=(10, 5))

# 绘制散点图，每个点代表一天的早起时间
plt.scatter(dates, times_str, color='blue')

# 添加标题和轴标签
plt.title('Morning Wake Up Times')
plt.xlabel('Date')
plt.ylabel('Time')

# 显示网格
plt.grid(True)

# 旋转日期标签，便于阅读
plt.xticks(rotation=45)

# 显示图形
plt.tight_layout()
plt.show()