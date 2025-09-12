import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
df = sns.load_dataset("iris")  

# 1. Pairplot
sns.pairplot(df, hue="species")
plt.show()

# 2. Heatmap (correlation matrix)
corr = df.corr(numeric_only=True)  
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# 3. FacetGrid Example
tips = sns.load_dataset("tips")  # Restaurant tips dataset

g = sns.FacetGrid(tips, col="sex", row="time")  
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()
