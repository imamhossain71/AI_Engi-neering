import pandas as pd

data = {
    'Name': ['Imam', 'Priya', 'Ayub', 'Rahim'],
    'Age': [25, None, 5, 30],
    'City': ['Sylhet', 'London', None, 'Dhaka']
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# missing values count
print("\nMissing values count:\n", df.isnull().sum())
# fill missing values
df_filled = df.fillna({'Age': df['Age'].mean(), 'City': 'Unknown'})
print("\nDataFrame after filling missing values:\n", df_filled)
# drop rows with missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:\n", df_dropped)

sales = {
    'Person': ['Imam', 'Imam', 'Priya', 'Ayub', 'Ayub'],
    'Product': ['Book', 'Pen', 'Book', 'Book', 'Pen'],
    'Sales': [200, 100, 150, 300, 120]
}
df_sales = pd.DataFrame(sales)
print("\nSales DataFrame:\n", df_sales)
# group by Person and sum Sales
group_person = df_sales.groupby('Person')['Sales'].sum()
print("\nTotal Sales by Person:\n", group_person)
# group by Product and sum Sales
group_product = df_sales.groupby('Product')['Sales'].mean()
print("\nAverage Sales by Product:\n", group_product)

students = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Imam', 'Priya', 'Ayub']
})

scores = pd.DataFrame({
    'ID': [1, 2, 4],
    'Score': [85, 90, 75]
})
# Merge with common ID
merged = pd.merge(students, scores, on='ID', how='inner')
print("\nInner Merge:\n", merged)
# Left Join
left_join = pd.merge(students, scores, on='ID', how='left')
print("\nLeft Join:\n", left_join)
# Outer Join
outer_join = pd.merge(students, scores, on='ID', how='outer')
print("\nOuter Join:\n", outer_join)