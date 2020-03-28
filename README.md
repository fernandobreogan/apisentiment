<p align="center">
  <img width="1000" height="300" src="https://github.com/breogann/apisentiment/blob/master/Images/cover.png" alt="Sentiment analysis">
</p>


# Sentiment Analysis API

This API allows you to crete a database with users, groups and messages so that you can retrieve that information and later analyze its sentiment using natural language processing. The information is retrieved in a JSON format so it can be easily manageable.

## Data 📊 ##

The API allows the input and retrieval of users, chats and messages:

<p align="center">
  <img width="500" height="200" src="https://github.com/fernandobreogan/apisentiment/blob/master/input/MongoDBstructure.png" alt="Data structure in MongoDB">
</p>

<p align="center">
  <img width="500" height="200" src="https://github.com/fernandobreogan/apisentiment/blob/master/input/MongoDBstructurejson.png" alt="[Data structure in MongoDB in JSON">
</p>

## Data processing 🛠 ## 

### __GET__ endpoints: retrieve info ###

- 



### __POST__ endpoints: input info into the DB ###

**Create a user**

    "/user/create/<username>"

**Create a chat**

    "/chat/create/<chat_name>"

**Add users to a chat**

    "/chat/<chat_name>/adduser/<username>"

**Add messages to a chat**

    "/chat/<chat_name>/<username>/<message>"



#### Used technologies 🔌: ####
- PyMongo
- Flask
- Docker
- Heroku


#### Used libraries 📚: ####
- Pandas
- Numpy


* TO-DO: deploy in Heroku!