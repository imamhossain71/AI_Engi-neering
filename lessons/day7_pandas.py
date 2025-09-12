

import pandas as pd

# 1️⃣ Data Load

data = {
    "Full_Name": ["Imam", "Ayesha", "Karim", "Unknown", "Sadia"],
    "Age": [25, 30, 30, 40, 30],
    "Location": ["DHAKA", "Sylhet", "DHAKA", "Chittagong", "Unknown"]
}
df = pd.DataFrame(data)

print("------ Original Data ------")
print(df)

# 2️⃣ Data Filtering
# Age > 30 row 
age_above_30 = df[df['Age'] > 30]
print("\n------ Age > 30 ------")
print(age_above_30)


dhaka_people = df[df['Location'] == 'DHAKA']
print("\n------ Location == DHAKA ------")
print(dhaka_people)

# Multiple conditions: Age > 30 এবং Location != 'Unknown'
filtered = df[(df['Age'] > 30) & (df['Location'] != 'Unknown')]
print("\n------ Age > 30 & Location != Unknown ------")
print(filtered)

# 3️⃣ Sorting Data
# Age ascending order
sorted_age_asc = df.sort_values(by='Age', ascending=True)
print("\n------ Age Ascending ------")
print(sorted_age_asc)

# Age descending order
sorted_age_desc = df.sort_values(by='Age', ascending=False)
print("\n------ Age Descending ------")
print(sorted_age_desc)

# Multiple column sorting: Location ascending, Age descending
sorted_multi = df.sort_values(by=['Location', 'Age'], ascending=[True, False])
print("\n------ Location Asc & Age Desc ------")
print(sorted_multi)

# 4️⃣ Group By + Aggregation
# Location average Age
grouped_mean = df.groupby('Location').agg({'Age':'mean'})
print("\n------ Average Age per Location ------")
print(grouped_mean)


grouped_multi = df.groupby('Location').agg({'Age':['mean','max']})
print("\n------ Mean & Max Age per Location ------")
print(grouped_multi)
