[![Build Status](https://travis-ci.org/timolinn/hng.tech.svg?branch=master)](https://travis-ci.org/timolinn/hng.tech)

<div align="center">

![hng](https://res.cloudinary.com/iambeejayayo/image/upload/v1554240066/brand-logo.png)

<br>

</div>

# Team-Go
- Extracted .csv files of the following tables: users, following, posts, notifications.

Proposed approach:
1. Recommending who to follow for User X: if X follows  a User Y, then recommend to X the users Y follows that X is not following.
Input: Users already followed by X, check “Following” table to return users followed by Y
2. Recommending articles to User X:
If X follows a User Y, then recommend to X posts liked/loved by user Y.
Input: Users followed by X, check “Notifications” table to return posts with type “Reaction” (action “like” or “love”)
