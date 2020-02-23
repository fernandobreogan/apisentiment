from pymongo import MongoClient
from flask import Flask, request
import pymongo
import json
import argparse
import requests

client = MongoClient('mongodb://localhost:27017/')
db = client['eslac']

app = Flask(__name__)

#GET (GETTING INFORMATION) users & conversations
@app.route("/getid/<name>") 
def getUserId(name):
    #Get user's info by inputting their name
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


#TESTING THE API
@app.route("/")
def hello ():
    return "Add or get info using the endpoints"

@app.route("/test")
def test ():
    return "The API works!"


#CREATEEEEEEEEEEEEEEEE (INSERTING COLLECTIONS) users & conversations

@app.route("/user/create/<name>")
def createUser (name):
    nombre = {"Name":f"{name}"}
    users_match = db.users.find({"Name":f"{name}"}, projection={name:True})
    if len(list(users_match)) > 0:
        return "That username already exists"
    else: 
        db.users.insert_one(nombre) #Creates document within the users collection
        a = getUserId(name)
        return "The user {} has been created and added to the DB with {}.".format(name, a)

"""
@app.route("/user/create/<name>")
def createUser (name):
    nombre = {"Name":f"{name}"}
    db.users.insert_one(nombre) #Create document within the users collection
    #users = pymongo.Connection()['users']['name']
    #_id = collection.insert({"name": "tyler"}) #To retrieve the assigned _id
    return "The user {} has been created and added to the DB.".format(name)
"""
"""
@app.route("/chat/create") 
def createChatWithTwoPeopleOnJupyter ():
    #Create a two people conversation on jupyter
    user1 = request.args.get(key="First user")
    user2 = request.args.get(key="Second user")

    new_chat = {"First user" : user1, "Second user": user2}

    db.conversations.insert(new_chat) #Create document within the users collection in Mongo
    return f"{new_chat} has been created."

createUser (name)
"""

@app.route("/chat/create") 
def createChatWithTwoPeopleOnJupyter ():
    #Create a two people conversation on jupyter
    user1 = request.args.get(key="First user")
    user2 = request.args.get(key="Second user")

    new_chat = {"Users": {"First user" : user1, "Second user": user2}}

    db.conversations.insert(new_chat) #Create document within the users collection in Mongo
    return f"{new_chat} has been created."

"""
@app.route("/chat/<chat_id>/adduser")
def addUserToChat():
    #meterle un id
    add_user_to_chat = db.conversations.find({"_id":f"{chat_id}"}, projection={name:True})
    returns chat_id
"""


app.run("0.0.0.0", 5000, debug=True)


"""
#Para generars las ID's
db.collection.distinct()¶
max()+1


"""





