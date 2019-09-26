[![Build Status](https://travis-ci.org/timolinn/hng.tech.svg?branch=master)](https://travis-ci.org/timolinn/hng.tech)

<div align="center">

![hng](https://res.cloudinary.com/iambeejayayo/image/upload/v1554240066/brand-logo.png)

<br>

</div>

# Team-Go
- Extracted some tables on the sql databse
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
- Model can be tested by parsing an argument to the get recommmendations function. Since model was trained on data, arguments should be any of the title topics in the metadata csv file (merged file)
