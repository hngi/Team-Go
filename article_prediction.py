
# coding: utf-8

# In[2]:


#importing libraries

import pandas as pd
import numpy as np
import pandas_profiling
#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')


# In[9]:


#loading  and copying post data

post_data = pd.read_csv('posts.csv')
post_data2 = post_data.copy()
post_data2.head(5)


# In[7]:


#understanding data

post_data2.dtypes


# In[17]:


#Loading and copying user data

user_data = pd.read_csv('users.csv')

user_data2 = user_data.copy()
user_data2.head(5)


# In[18]:


user_data2.dtypes


# In[19]:


#merging user and post data on user_id

df = pd.merge(post_data2, user_data2, on='user_id')


# In[21]:


#copying merged data

metadata = df.copy()

df.head(5)


# In[23]:


metadata.dtypes


# In[25]:


metadata.shape


# In[26]:


metadata.describe()


# In[28]:


#data with missing columns

metadata.isnull().sum()


# In[37]:


#dropping missing columns

metadata.dropna(axis=1, inplace=True)


# In[38]:


metadata.isnull().sum()


# In[42]:


metadata.describe()


# In[43]:


pandas_profiling.ProfileReport(metadata)


# In[44]:


#finding correlation

metadata.corr(method = 'pearson')


# In[45]:


#finding correlation

metadata.corr(method = 'kendall')


# In[50]:


import seaborn as sb
import matplotlib.pyplot as plt
metadata.columns


# In[59]:


#Getting the TF-IDF score or frequency of a word occurring in a document, i.e the title

tfidf_matrix = tfidf.fit_transform(metadata['content'])

#Output the shape of tfidf_matrix
tfidf_matrix.shape


# In[60]:


#compute users similarity score using the cosine similarity
# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


# In[61]:


#defining a function that takes in a post title as an input and outputs a list of the 10 most similar post.Firstly, for this, you need a reverse mapping of movie titles and DataFrame indices. In other words, you need a mechanism to identify the index of a movie in your metadata DataFrame, given its title.


#Construct a reverse map of indices and movie titles
indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

#Get the index of the post given its title.

#Get the list of cosine similarity scores for that particular post with all posts. Convert it into a list of tuples where the first element is its position and the second is the similarity score.


#Sort the aforementioned list of tuples based on the similarity scores; that is, the second element.

#Get the top 10 elements of this list. Ignore the first element as it refers to self (the post most similar to a particular post is the post itself).

#Return the titles corresponding to the indices of the top elements.



# In[68]:


def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return metadata['title'].iloc[movie_indices]
get_recommendations('What i have learnt so far on HTML')


# In[72]:


get_recommendations('Welcome to Lucid')


# In[66]:


metadata.title

