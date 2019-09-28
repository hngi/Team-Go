# Content based Recommender system to suggest post to user

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Helper functions
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


# Read Post CSV file
df = pd.read_csv("posts.csv")
print (df.columns)

# Select features

features = ["user_id","title","content"]

# Creating a column which combines all selected features
for feature in features:
    df[feature] = df[feature].fillna('')
def combine_features(row):
    try:
        return (row['user_id'] +" "+ row['title'] +" "+ row['content'])
    except:
        print("Error:", row)

df["combined_features"] = df.apply(combine_features,axis=1)
print("Combined Features:", df["combined_features"].head())

# To create count matrix
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

# Compute the Cosine Similarity on the count matrix
cos_sim = cosine_similarity(count_matrix)
post_user_likes = "HTML BEGINS HERE"

# Get the index of this post from its title

post_index = get_index_from_title(post_user_likes)

similar_posts = list(enumerate(cos_sim[post_index]))
sorted_similar_posts = sorted(similar_posts, key = lamda x:x[1], reverse=True)
# print titles of first 50 posts
i = 0
for post in similar_posts:
    print (get_title_from_index(post[0]))
    i = i + 1
    if i > 50:
        break