import pandas as pd

# 读取CSV文件
df = pd.read_csv('morning_times.csv')

# # 查看数据框架
# print(df)

# 将 'Date' 和 'Time' 列合并为一个 'DateTime' 列
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])



# # 查看数据框架
# print(df['DateTime'])

# # 检查早起时间的频率
# frequencies = df['DateTime'].value_counts()

# print(frequencies)

# 计算平均早起时间
# average_time = df['DateTime'].mean()

# print(f"Average wake up time: {average_time}")
