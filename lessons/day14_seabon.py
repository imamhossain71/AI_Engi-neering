import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")   # Built-in dataset
print(df.head())

sns.histplot(df["total_bill"], bins=10, kde=True)
plt.title("Total Bill Distribution")
plt.show()

sns.countplot(x="day", data=df)
plt.title("Number of Customers per Day")
plt.show()

sns.scatterplot(x="total_bill", y="tip", data=df, hue="sex")
plt.title("Bill vs Tip by Gender")
plt.show()