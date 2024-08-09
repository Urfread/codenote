import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

# # 模拟的早起时间数据，格式为 (日期，时间)
# data = {
#     'date': ['2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05'],
#     'time': ['06:30', '06:45', '06:20', '06:10', '06:00']
# }

# 将模拟数据转换为DataFrame
df = pd.read_csv('morning_times.csv')

# 将日期和时间合并为datetime类型
df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

# 设置matplotlib支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 定义一个函数，将分钟转换为小时和分钟的格式
def format_time(y, pos=None):
    """The function to format the time in hours and minutes."""
    hours, minutes = divmod(int(y), 60)
    return f"{hours:02d}:{minutes:02d}"

# 创建图形和轴
fig, ax = plt.subplots()

# 绘制折线图，使用datetime列作为x轴，分钟数作为y轴
ax.plot(df['datetime'].dt.date, [m * 60 + n for m, n in zip(df['datetime'].dt.hour, df['datetime'].dt.minute)], marker='o', linestyle='-')

# 仅显示日期在x轴上
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator())

# 设置Y轴的格式为小时和分钟
formatter = FuncFormatter(format_time)
ax.yaxis.set_major_formatter(formatter)

# 旋转日期标签
plt.xticks(rotation=45)

# 添加标题和轴标签
plt.title('早起时间统计')
plt.xlabel('日期')
plt.ylabel('时间')

# 显示网格
plt.grid(True)

# 调整布局并显示图形
plt.tight_layout()
plt.show()