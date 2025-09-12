import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV load করার সময় encoding ঠিক করে নিতে হবে
df = pd.read_csv("data/netflix_titles.csv", encoding="latin1")

print(df.head())

plt.figure(figsize=(8,5))
sns.countplot(x="type", data=df, palette="coolwarm")
plt.title("Count of Movies vs TV Shows", fontsize=16, fontweight="bold")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.show()

plt.figure(figsize=(10,6))
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.title("Top 10 Countries Producing Netflix Content", fontsize=16, fontweight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()

plt.figure(figsize=(12,6))
df['release_year'].value_counts().sort_index().plot(kind="line", marker="o", color="purple")
plt.title("Netflix Content Release Trend by Year", fontsize=16, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

plt.figure(figsize=(8,5))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap (Netflix Data)", fontsize=16, fontweight="bold")
plt.show()
