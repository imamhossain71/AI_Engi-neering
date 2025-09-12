import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample dataset
data = {
    "Age": [25, 30, 29, 35, 40, 38, 28, 45, 32, 41],
    "Salary": [50000, 40000, 55000, 60000, 65000, 42000, 48000, 70000, 39000, 72000],
    "Marks": [85, 90, 88, 32, 95, 80, 87, 93, 89, 75]
}
df = pd.DataFrame(data)

# 1. Subplots
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)   # row=1, col=2, position=1
plt.hist(df["Age"], bins=5, color="orange")
plt.title("Age Distribution")

plt.subplot(1,2,2)   # row=1, col=2, position=2
plt.hist(df["Salary"], bins=5, color="blue")
plt.title("Salary Distribution")

plt.tight_layout()
plt.show()

# 2. Multiple Lines
plt.plot(df["Age"], df["Salary"], label="Salary")
plt.plot(df["Age"], df["Marks"], label="Marks")
plt.title("Age vs Salary & Marks")
plt.xlabel("Age")
plt.ylabel("Value")
plt.legend()
plt.show()

# 3. Pairplot
sns.pairplot(df)
plt.show()

# 4. Heatmap
corr = df.corr(numeric_only=True)   # correlation matrix
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
