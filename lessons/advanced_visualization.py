# lessons/advanced_visualization.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# ----------------------------
# Load Netflix dataset
# ----------------------------
df = pd.read_csv("data/netflix_titles.csv", encoding="latin1")

# duration k numeric a convert 
df['duration_int'] = df['duration'].str.extract('(\d+)')
df['duration_int'] = pd.to_numeric(df['duration_int'], errors='coerce')

# ----------------------------
# 1. Pairplot (relationship between numeric features)
# ----------------------------
# plt.figure(figsize=(12,8))
sns.pairplot(df[['duration_int']].dropna())

plt.suptitle("Pairplot - Netflix Duration", y=1.02)
plt.show()

# ----------------------------
# 2. Jointplot (scatter + histogram) - Iris dataset
# ----------------------------
iris = sns.load_dataset("iris")
sns.jointplot(x="sepal_length", y="petal_length", data=iris, kind="scatter")
plt.suptitle("Jointplot - Iris Dataset", y=1.02)
plt.show()

# ----------------------------
# 3. Catplot (categorical vs numeric)
# ----------------------------
sns.catplot(x="species", y="petal_length", data=iris, kind="box")
plt.suptitle("Catplot (Boxplot) - Species vs Petal Length", y=1.02)
plt.show()

# ----------------------------
# 4. Heatmap (correlation)
# ----------------------------
corr = iris.corr(numeric_only=True)   # only numeric columns
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap - Correlation Matrix")
plt.show()

# ----------------------------
# 5. WordCloud (text visualization)
# ----------------------------
text = " ".join(df['description'].dropna().astype(str))

wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color="white",
                      width=800,
                      height=400).generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("WordCloud - Netflix Descriptions")
plt.show()
