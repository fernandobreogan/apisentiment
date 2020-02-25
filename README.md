# Sentiment Analysis Api

API project for Ironhack coding school.

This API allows you to crete a database with users, groups and messages so that you can retrieve that information and later analyze its sentiment using natural language processing. The information is retrieved in a json format so it can be easily manageable.

![Data structure in MongoDB](/input/MongoDBstructure)

![Data structure in MongoDB 2](/input/MongoDBstructure2)

## Authentication ##
This API does not require any kind of authentication.

## GET endpoints: retrieve info ##

- 



## POST endpoints: input info into the DB ##

**Create a user**

    "/user/create/<username>"

**Create a chat**

    "/chat/create/<chat_name>"

**Add users to a chat**

    "/chat/<chat_name>/adduser/<username>"

Add messages to a chat

    "/chat/<chat_name>/<username>/<message>"


Built with
- Flask
- Docker
- Heroku

To-do list:

* Sentiment analysis
Info retrieval endpoints (not just internally)


