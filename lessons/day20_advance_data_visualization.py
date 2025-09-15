import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Dataset Load
df = pd.read_csv("data/netflix_titles.csv", encoding="latin1")

# 1. Stacked Bar Chart: Release Year vs Content Type
plt.figure(figsize=(12,6))
content_year = df.groupby(["release_year","type"]).size().unstack().fillna(0)
content_year.plot(kind="bar", stacked=True, figsize=(14,6), colormap="coolwarm")
plt.title("Stacked Bar Chart: Movies vs TV Shows by Year", fontsize=16, fontweight="bold")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.legend(title="Content Type")
plt.show()

# 2. FacetGrid: Country-wise Netflix Content Distribution
top_countries = df['country'].value_counts().head(3).index   # Top 3 countries
df_top = df[df['country'].isin(top_countries)]

g = sns.FacetGrid(df_top, col="country", height=5, aspect=1.2)
g.map(sns.countplot, "type", order=df['type'].value_counts().index, palette="viridis")
g.set_axis_labels("Content Type", "Count")
g.set_titles("{col_name}")
plt.suptitle("Movies vs TV Shows in Top 3 Countries", fontsize=16, fontweight="bold", y=1.05)
plt.show()

# 3. WordCloud: Most Common Words in Descriptions
text = " ".join(str(desc) for desc in df['description'].dropna())
wordcloud = WordCloud(width=1000, height=500, background_color="white", colormap="plasma").generate(text)

plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Netflix Descriptions", fontsize=16, fontweight="bold")
plt.show()

# 4. Scatterplot (Numerical Relation) - Duration vs Release Year
# Clean duration column
df['duration_num'] = df['duration'].str.extract('(\d+)').astype(float)
df['duration_type'] = df['duration'].str.extract('([a-zA-Z]+)')

plt.figure(figsize=(10,6))
sns.scatterplot(x="release_year", y="duration_num", hue="type", data=df, alpha=0.6, palette="Set1")
plt.title("Duration vs Release Year (Movies & TV Shows)", fontsize=16, fontweight="bold")
plt.xlabel("Release Year")
plt.ylabel("Duration (Minutes / Seasons)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

#common actor
text1 = " ".join(str(desc) for desc in df['description'].dropna())
wordcloud = WordCloud(width=1000, height=500, background_color="white", colormap="plasma").generate(text1)


