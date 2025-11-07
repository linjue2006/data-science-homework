import pandas as pd

df = pd.read_csv(r'D:\china_salary.csv')
print(df.head())
print(df.info())
print(df.describe())#part1
#part2
print(df.isnull().sum())

# Fill missing salary with mean
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Drop rows with too many missing values
df = df.dropna(thresh=3)


#part3处理异常值

import numpy as np

# Detect outliers using Z-score
z = (df['Salary'] - df['Salary'].mean()) / df['Salary'].std()
outliers = df[z.abs() > 3]
print(outliers)

# Remove outliers
df = df[z.abs() < 3]

#part4  数据标准化和归一化
from sklearn.preprocessing import MinMaxScaler, StandardScaler

scaler = MinMaxScaler()
df[['Salary_scaled']] = scaler.fit_transform(df[['Salary']])

std_scaler = StandardScaler()
df[['Salary_standard']] = std_scaler.fit_transform(df[['Salary']])

print(df[['Salary', 'Salary_scaled', 'Salary_standard']].head())

#part5 

# Equal-width binning
df['SalaryBin_width'] = pd.cut(df['Salary'], bins=4, labels=['Low','Medium','High','Very High'])

# Equal-depth binning
df['SalaryBin_depth'] = pd.qcut(df['Salary'], q=4, labels=['Q1','Q2','Q3','Q4'])

print(df[['Salary', 'SalaryBin_width', 'SalaryBin_depth']].head())# Equal-width binning
df['SalaryBin_width'] = pd.cut(df['Salary'], bins=4, labels=['Low','Medium','High','Very High'])

# Equal-depth binning
df['SalaryBin_depth'] = pd.qcut(df['Salary'], q=4, labels=['Q1','Q2','Q3','Q4'])

print(df[['Salary', 'SalaryBin_width', 'SalaryBin_depth']].head())
 #part6  
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.hist(df['Salary'], bins=10, color='skyblue', edgecolor='black')
plt.title('Salary Distribution after Cleaning / 清洗后薪资分布')
plt.xlabel('Salary (RMB)')
plt.ylabel('Frequency')
plt.show()