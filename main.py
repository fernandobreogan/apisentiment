from pymongo import MongoClient
from flask import Flask, request
import pymongo
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['eslac']

app = Flask(__name__)

"""### 1. User endpoints

- (GET) `/user/create/<username>`
  OK - **Purpose:** Create a user and save into DB
  OK - **Params:** `username` the user name
  OK - **Returns:** `user_id`


- (GET) `/user/<user_id>/recommend`
  - **Purpose:** Recommend friend to this user based on chat contents
  - **Returns:** json array with top 3 similar users
"""

"""
def make_sure_exists(story, stories_col):
    data = stories_col.find_one({'story': story})
    if data is not None:
        return data.['_id']
    return stories_col.insert_one({'story': story}).inserted_id

"""

@app.route("/")
def hello ():
    return "Add or get info using the endpoints"

@app.route("/test")
def test ():
    return "The API works!"

@app.route("/user/create/<name>")
def createUser (name):
    nombre = {"Name":f"{name}"}
    db.users.insert_one(nombre) #Create document within the users collection
    #users = pymongo.Connection()['users']['name']
    #_id = collection.insert({"name": "tyler"}) #To retrieve the assigned _id
    return "The user {} has been created".format(name)

"""
@app.route("/getid/<name>")
def getUserId(name):
    item = db.users.find_one({"Name":f"{name}"})
    numero = item.get('_id')
    return json.dumps(numero, default=str)
"""
@app.route("/getid/<name>")
def getUserId(name):
    for i in db.users.find({"Name":f"{name}"}):
        ides = i.get('_id')
        return json.dumps(ides, default=str)

@app.route("/user_info")
def getUserInfo(name):
    usuario = db.users.find({"Name":f"{name}"}, projection={name:True})
    return list(usuario)

def totalChats():
    total = db.conversations.countDocuments({})
    return total

#def createChat(*users):
 #   return chatID

app.run("0.0.0.0", 5000, debug=True)


"""
#Para generars las ID's
db.collection.distinct()¶
max()+1


"""