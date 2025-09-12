import pandas as pd  

data = {
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance'],
    'Employee': ['Imam', 'Ayesha', 'Karim', 'Sadia', 'Unknown', 'Rafiq'],
    'Salary': [50000, 40000, 55000, 60000, 42000, 65000]
}

df = pd.DataFrame(data)
print("------ Original Data ------")
print(df)

print(df.groupby('Department')['Salary'].mean())
print(df.groupby('Department')['Salary'].agg(['mean', 'max', 'min', 'count']))

# print(df.sort_values(by='Salary', ascending=False))
print(df.sort_values(by=['Department', 'Salary'], ascending=[True, False]))
grouped = df.groupby('Department')['Salary'].mean().reset_index()
print(grouped)

#task
print("------ Task Output ------")
print(df.groupby('Department')['Salary'].mean())
print(df.groupby('Department')['Salary'].agg(['mean','max','min','count']))
print(df.sort_values(by='Salary', ascending=False))
print(df.sort_values(by=['Department','Salary'], ascending=[True,False]))
# grouped = df.groupby('Department')['Salary'].mean().reset_index()
# print(grouped)
idx=df.groupby('Department')['Salary'].idxmax()
max_salary=df.loc[idx]
print(max_salary)