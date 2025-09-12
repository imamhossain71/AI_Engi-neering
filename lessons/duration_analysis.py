import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset load
df = pd.read_csv("data/netflix_titles.csv", encoding="latin1")

# 1. Movies এর Duration distribution
movies = df[df['type'] == "Movie"]
movies['duration_num'] = movies['duration'].str.replace(" min","").astype(float)

plt.figure(figsize=(10,5))
sns.histplot(movies['duration_num'], bins=30, kde=True, color="red")
plt.title("Distribution of Movie Durations", fontsize=16, fontweight="bold")
plt.xlabel("Duration (minutes)")
plt.ylabel("Count")
plt.show()

# 2. TV Shows এর Seasons distribution
tv_shows = df[df['type'] == "TV Show"]
tv_shows['seasons_num'] = tv_shows['duration'].str.replace(" Season","").str.replace("s","").astype(int)

plt.figure(figsize=(8,5))
sns.countplot(x="seasons_num", data=tv_shows, palette="coolwarm")
plt.title("Distribution of TV Show Seasons", fontsize=16, fontweight="bold")
plt.xlabel("Number of Seasons")
plt.ylabel("Count")
plt.show()

# Country-wise average duration
avg_duration_country = movies.groupby("country")['duration_num'].mean().sort_values(ascending=False).head(10)
print(avg_duration_country)
plt.figure(figsize=(12,6))
sns.barplot(x=avg_duration_country.values, y=avg_duration_country.index, palette="magma")
plt.title("Top 10 Countries by Average Movie Duration", fontsize=16, fontweight="bold")
plt.xlabel("Average Duration (minutes)")
plt.ylabel("Country")
plt.show()


# শুধু movies filter করি
movies = df[df['type'] == 'Movie'].copy()

# duration থেকে numeric value নিলাম
movies['duration_num'] = movies['duration'].str.replace(' min','').astype(float)

# শুধু Top 5 countries নিলাম visualization এর জন্য
top_countries = movies['country'].value_counts().head(5).index
movies_top = movies[movies['country'].isin(top_countries)]
avg_duration_year_country = movies_top.groupby(['release_year','country'])['duration_num'].mean().unstack()
print(avg_duration_year_country.head())
plt.figure(figsize=(14,7))
for country in avg_duration_year_country.columns:
    plt.plot(avg_duration_year_country.index, 
             avg_duration_year_country[country], 
             marker='o', linewidth=2, label=country)

plt.title("Average Movie Duration by Release Year & Country", fontsize=16, fontweight="bold")
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Average Duration (minutes)", fontsize=12)
plt.legend(title="Country")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

#-----pivote table-----
# # Movies filter করি
# movies = df[df['type'] == 'Movie'].copy()

# # Top 5 countries + Top 5 genres filter করে visualization clean রাখব
# top_countries = movies['country'].value_counts().head(5).index
# top_genres = movies['listed_in'].str.split(', ').explode().value_counts().head(5).index

# # Filtered movies
# movies_top = movies[movies['country'].isin(top_countries)]
# movies_top = movies_top[movies_top['listed_in'].str.contains('|'.join(top_genres))]

# # Genre column explode করা
# movies_top['Genre'] = movies_top['listed_in'].str.split(', ')
# movies_exploded = movies_top.explode('Genre')

# # Pivot table: Year vs Genre per Country
# heatmap_data = movies_exploded[movies_exploded['country']=='United States'].pivot_table(
#     index='Genre',
#     columns='release_year',
#     values='title',
#     aggfunc='count'
# )

# print(heatmap_data.head())

# plt.figure(figsize=(14,7))
# sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu", linewidths=.5)
# plt.title("Number of Movies per Genre by Release Year (USA)", fontsize=16, fontweight="bold")
# plt.xlabel("Release Year", fontsize=12)
# plt.ylabel("Genre", fontsize=12)
# plt.show()
