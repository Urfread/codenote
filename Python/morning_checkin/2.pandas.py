import pandas as pd

# 读取CSV文件
df = pd.read_csv('students.csv')

# 查看数据框架
#print(df)

# 查看前5行
#print(df.head())

# 选择 'Name' 和 'Math' 列
#print(df[['Name', 'Math']])

# 选择数学成绩超过90分的学生
# top_math_students = df[df['Math'] > 90]

# print(top_math_students)

# df_sorted = df.sort_values(by='Math', ascending=False)

# print(df_sorted)

# mean_scores = df[['Math', 'Science', 'Language']].mean()

# print(mean_scores)

mean_age_by_gender = df.groupby('Gender')['Age'].mean()

print(mean_age_by_gender)