# Day 3 – Pandas Practice
import pandas as pd 

# 1️⃣ Series creation
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print("Pandas Series:\n", s)
# Series হল এক ধরনের 1D labelled array
# এখানে index auto-generated (0-4) হবে

# Custom index
s2 = pd.Series(data, index=['a','b','c','d','e'])
print("\nSeries with custom index:\n", s2)
# এখন আমাদের নিজস্ব label/Index ব্যবহার করা হয়েছে

# 2️⃣ DataFrame creation
data_dict = {
    'Name': ['Imam', 'Ali', 'Sara', 'Nila'],
    'Age': [24, 25, 22, 23],
    'City': ['Dhaka', 'Sylhet', 'Chittagong', 'Khulna']
}
df = pd.DataFrame(data_dict)
print("\nDataFrame:\n", df)
# DataFrame হল 2D labeled data structure (table)
# Columns → Name, Age, City
# Rows → index 0-3

# 3️⃣ Basic Data Exploration
print("\nFirst 2 rows:\n", df.head(2))   # first 2 rows
print("\nLast 2 rows:\n", df.tail(2))    # last 2 rows
print("\nColumns:\n", df.columns)       # column names
print("\nShape:\n", df.shape)           # (rows, columns)
print("\nData types:\n", df.dtypes)     # column-wise datatype

# 4️⃣ Selecting columns & rows
print("\nSelect Age column:\n", df['Age'])
print("\nSelect multiple columns:\n", df[['Name','City']])
print("\nSelect first row:\n", df.iloc[0])       # by position
print("\nSelect row by index:\n", df.loc[1])     # by index label

# 5️⃣ Filtering Data
print("\nPeople older than 23:\n", df[df['Age'] > 23])
print("\nPeople in Dhaka:\n", df[df['City'] == 'Dhaka'])

# 6️⃣ Adding & Modifying columns
df['Country'] = 'Bangladesh'  # নতুন column add
print("\nAdd new column:\n", df)

df['Age'] = df['Age'] + 1      # modify existing column
print("\nIncrement Age by 1:\n", df)

# 7️⃣ Handling missing values
df2 = df.copy()
df2.loc[2,'City'] = None       # missing value add
print("\nData with missing value:\n", df2)
print("\nFill missing value:\n", df2.fillna('Unknown'))  # fillna

# 8️⃣ Reading & Writing CSV
df.to_csv('sample.csv', index=False)  # save to csv
df_from_csv = pd.read_csv('sample.csv')
print("\nRead from CSV:\n", df_from_csv)
# homework: practice with your own data!
data_f={
    'marks':[85,95,76,39,77,69],
    'class':[7,8,9,6,7,8],
    'grade':['A','A+','B','F','B+','A-']

}
df_f=pd.DataFrame(data_f)
print("\n Students get more than 80 marks:\n",df_f[df_f['marks']>80])
df_f['result']=['pass' if marks>=40 else 'fail' for marks in df_f['marks']]
print("\n Students with result:\n",df_f)

df_f.to_csv('students.csv',index=False)
df_f_from_csv=pd.read_csv('students.csv')
print("\n Read from CSV:\n",df_f_from_csv)