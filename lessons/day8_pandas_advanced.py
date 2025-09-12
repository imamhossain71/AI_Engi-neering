# lessons/day8_pandas_advanced.py

import pandas as pd  # pandas import করা হলো pd নামে

# 1️⃣ Sample DataFrame তৈরি
data = {
    'Full_Name': ['Imam', 'Ayesha', 'Karim', 'Unknown', 'Sadia'],
    'Age': [25, 30, 30, 40, 30],
    'Location': ['DHAKA', 'Sylhet', 'DHAKA', 'Chittagong', 'Unknown']
}

df = pd.DataFrame(data)

print("------ Original Data ------")
print(df)

# 2️⃣ Apply + Lambda

df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else ('Adult' if x < 40 else 'Senior'))

print("\n------ After Creating Age_Group ------")
print(df)

# 3️⃣ Map function
# Location কে short code এ convert করা হলো
location_map = {'DHAKA': 'DHK', 'Sylhet': 'SYL', 'Chittagong': 'CTG', 'Unknown': 'UNK'}
df['Location_Code'] = df['Location'].map(location_map)

print("\n------ After Mapping Location ------")
print(df)

# 4️⃣ applymap function
# পুরো DataFrame এর string column কে uppercase করা হলো
df_upper = df[['Full_Name', 'Location']].applymap(str.upper)

print("\n------ After applymap (Uppercase) ------")
print(df_upper)

# 5️⃣ value_counts
# Location এর unique values এর frequency বের করা হলো
location_counts = df['Location'].value_counts()

print("\n------ Location Value Counts ------")
print(location_counts)
