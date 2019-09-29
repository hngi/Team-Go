[![Build Status](https://travis-ci.org/timolinn/hng.tech.svg?branch=master)](https://travis-ci.org/timolinn/hng.tech)

<div align="center">

![hng](https://res.cloudinary.com/iambeejayayo/image/upload/v1554240066/brand-logo.png)

<br>

</div>

# Team-Go
- Extracted some tables on the sql database
- loaded, copied and merged both post and user data
- Due to high amount of missing data, columns with missing data was removed
- Got the TF-IDF score or frequency of a word occurring in a document, i.e the title
- defining a function that takes in a post title as an input and outputs a list of the 10 most similar post.
- Construct a reverse map of indices and movie titles
- Got the index of the post given its title.
- Got the list of cosine similarity scores for that particular post with all posts. Convert it into a list of tuples where the first element is its position and the second is the similarity score.
- Sorted the aforementioned list of tuples based on the similarity scores; that is, the second element.
- Got the top 10 elements of this list. Ignore the first element as it refers to self (the post most similar to a particular post is the  post itself).
- Returned the titles corresponding to the indices of the top elements.
# Article_prediction 

- open on colab
- call the get_recommendation function and pass in any post title in the post data to bring up similar post title recommendation

# Recommender System KNN testing
- Has models for posts and users recommendations
- Open with Jupyter 
- add all files to the same directory as the notebook
- Run testing_model function and follow intructions within

# Data Used
- Data used were extracted in csv format from the sql database provided using Xampp
- Data were then loaded and read using pandas
- Below is the link to the extracted data 
- https://www.dropbox.com/sh/0zmpvv3d7f525i5/AAAz96dXMfu2jr2Nfd_ia4uma?dl=0
