# 📌 Netflix Data Analysis & Visualization
# Author: Md Imam Hossain
# Project: Netflix Visualization Project

# =============================
# 1. Import Libraries
# =============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

# =============================
# 2. Load Dataset
# =============================
df = pd.read_csv("data/netflix_titles.csv", encoding="latin1")
print("Dataset shape:", df.shape)
print(df.head())

# =============================
# 3. Count of Movies vs TV Shows
# =============================
plt.figure(figsize=(8,5))
sns.countplot(x="type", data=df, palette="coolwarm")
plt.title("Count of Movies vs TV Shows", fontsize=16, fontweight="bold")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.show()

# Insight:
print("👉 Netflix has more Movies than TV Shows.")

# =============================
# 4. Top 10 Countries Producing Content
# =============================
plt.figure(figsize=(10,6))
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.title("Top 10 Countries Producing Netflix Content", fontsize=16, fontweight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()

print("👉 USA and India produce the most Netflix content.")

# =============================
# 5. Release Year Trend
# =============================
plt.figure(figsize=(12,6))
df['release_year'].value_counts().sort_index().plot(kind="line", marker="o", color="purple")
plt.title("Netflix Content Release Trend by Year", fontsize=16, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

print("👉 Netflix content production increased sharply after 2015.")

# =============================
# 6. WordCloud of Descriptions
# =============================
text = " ".join(df["description"].dropna().astype(str).values)
wordcloud = WordCloud(width=1000, height=600, background_color="black", stopwords=set(STOPWORDS)).generate(text)

plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("WordCloud of Netflix Descriptions", fontsize=16, fontweight="bold")
plt.show()

print("👉 Common words like 'love', 'family', 'life' appear frequently in descriptions.")

# =============================
# 7. Correlation Heatmap
# =============================
plt.figure(figsize=(8,5))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap (Netflix Data)", fontsize=16, fontweight="bold")
plt.show()

print("👉 Marks, Ratings, or numeric features can show hidden correlations.")
