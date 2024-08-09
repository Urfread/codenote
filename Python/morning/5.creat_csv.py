import pandas as pd
import numpy as np

# 设置随机种子以获得可重复的结果
np.random.seed(0)

# 定义日期范围
start_date = '2024-08-01'
end_date = '2024-09-01'  # 假设我们想要生成一个月的数据

# 生成日期范围
date_range = pd.date_range(start=start_date, end=end_date)

# 确保日期范围的长度与随机时间数组的长度相匹配
date_length = len(date_range)
random_hours = np.random.randint(5, 8, size=date_length)
random_minutes = np.random.randint(0, 60, size=date_length)

# 将小时和分钟转换为字符串，并格式化为HH:MM格式
time_strings = [f'{hour:02d}:{minute:02d}' for hour, minute in zip(random_hours, random_minutes)]

# 将时间字符串转换为datetime对象
random_times = pd.to_datetime(time_strings)

# 创建DataFrame
df = pd.DataFrame({
    'Date': date_range,
    'Time': random_times
})

# 查看生成的数据
print(df.head(10))

# 将数据保存到CSV文件
df.to_csv('morning_times.csv', index=False)