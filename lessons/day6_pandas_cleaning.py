import pandas as pd
import numpy as np
data = {
    "Name": ["Imam", "Ayesha", "Karim", "Imam", np.nan, "Sadia"],
    "Age": [25, 30, np.nan, 25, 40, 30],
    "City": ["Dhaka", "Sylhet", "Dhaka", "Dhaka", "Chittagong", np.nan]
}

df = pd.DataFrame(data)
print("------ Original Data ------")
print(df)

# 1. Missing Values 
print("\n------ Check Missing Values ------")
print(df.isnull().sum())
# 2. Missing Values handle 
df["Name"].fillna("Unknown", inplace=True)  
df["Age"].fillna(df["Age"].mean(), inplace=True)  
df["City"].fillna("Unknown", inplace=True) 

print("\n------ After Handling Missing Values ------")
print(df)
# 3. Duplicate Data 
print("\n------ Duplicate Rows ------")
print(df.duplicated())

# Duplicate remove
df = df.drop_duplicates()
print("\n------ After Removing Duplicates ------")
print(df)
# 4. Column rename
df.rename(columns={"Name": "Full_Name", "City": "Location"}, inplace=True)
print("\n------ After Renaming Columns ------")
print(df)

# 5. Values replace
df["Location"].replace("Dhaka", "DHAKA", inplace=True)
print("\n------ After Replacing Values ------")
print(df)
df["Full_Name"] = df["Full_Name"].str.title()
df["Age_Group"] = df["Age"].apply(lambda x: "Adult" if x >= 30 else "Young")
print("Duplicate count:", df.duplicated().sum())

print(df)