import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    "Name": ["Rafiq", "Karim", "Rahim", "Unknown"],
    "Age": [28, 34, 29, 40],
    "City": ["Dhaka", "Chittagong", "Sylhet", "Dhaka"],
    "Salary": [65000, 55000, 70000, 42000]
}
df = pd.DataFrame(data)

# 1. Line Plot (Age vs Salary)
plt.plot(df["Age"], df["Salary"], marker="o")
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# 2. Bar Plot (City vs Salary)
plt.bar(df["City"], df["Salary"])
plt.title("Salary by City")
plt.xlabel("City")
plt.ylabel("Salary")
plt.show()

# 3. Histogram (Salary distribution)
plt.hist(df["Salary"], bins=5, color="skyblue", edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary Range")
plt.ylabel("Count")
plt.show()

# 4. Seaborn Countplot (City frequency)
sns.countplot(x="City", data=df)
plt.title("Number of Employees per City")
plt.show()

# 5. Seaborn Boxplot (Salary by City)
sns.boxplot(x="City", y="Salary", data=df)
plt.title("Salary Distribution by City")
plt.show()

# 6. Task 

data_2 = {
    "Employee": ["Imam", "Ayesha", "Karim", "Sadia", "Unknown", "Rahim", "Selina", "Farhan", "Lamia", "Rafiq","Imu", "Ayesha rim", " islam", "jannat", "Unknown", "Rahima", "Selim", "Farhana", "Lam", "Rafi"],
    "Department": ["IT", "HR", "IT", "Finance", "Finance", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR", "IT", "Finance", "Finance", "HR", "IT", "Finance", "HR", "Finance"],
    "Salary": [50000, 40000, 55000, 60000, 65000, 42000, 48000, 70000, 39000, 72000, 51000, 41000, 56000, 61000, 66000, 43000, 49000, 71000, 40000, 73000],
    "Age": [25, 30, 29, 35, 40, 38, 28, 45, 32, 41, 26, 31, 27, 36, 39, 33, 44, 34, 37, 42],
    "Marks": [85, 90, 88, 32, 95, 80, 87, 93, 89, 75, 90, 88, 52, 95, 50, 87, 23, 89, 94, 55],
    "Location": ["Dhaka", "Sylhet", "Dhaka", "Chittagong", "Dhaka", "Sylhet", "Dhaka", "Chittagong", "Sylhet", "Dhaka", "Dhaka", "Sylhet", "Dhaka", "Chittagong", "Dhaka", "Sylhet", "Dhaka", "Chittagong", "Sylhet", "Dhaka"]
}

df_2 = pd.DataFrame(data_2)
print(df_2)
# Populate the DataFrame with at least 10 entries.
plt.plot(df_2["Age"], df_2["Salary"], marker="o")
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

plt.bar(df_2["Department"], df_2["Salary"])
plt.title("Department by Location")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

plt.hist(df_2["Marks"], bins=5, color="skyblue", edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Count")
plt.show()

sns.countplot(x="Location", data=df_2)
plt.title("Number of Employees per Location")
plt.show()

sns.boxplot(x="Department", y="Salary", data=df_2)
plt.title("Salary Distribution by Department")
plt.show()

# Create a scatter plot showing the relationship between Age and Marks.
plt.scatter(df_2["Age"], df_2["Salary"], color="green")
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

