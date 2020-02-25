from pymongo import MongoClient
import pymongo
import json
import argparse
import requests
from flask import Flask, request
import database as dtb


client = MongoClient('mongodb://localhost:27017/') #Connection to the DB
db = client['eslac'] 
app = Flask(__name__) 

#TESTING THE API
@app.route("/test")
def test ():
    return "The API works!"

#CREATE USERS & CREATE CHATS

@app.route("/user/create/<username>")
def createUsers (username):
    nombre = {"Name":f"{username}"}
    if dtb.checkUserExistsByName(db, username) == True:
        return "That user already exists"
    else: 
        db.users.insert_one(nombre) #Creates document within the users collection
        laide = dtb.getUserIdbyName(db, username)
        return "The user {} has been created with the ID {}".format(username, laide)


@app.route("/chat/create/<chat_name>")
def createChat (chat_name):
    nombre = {"Chat name":f"{chat_name}", "Users": [], "Messages":{}}
    
    if dtb.checkChatExistsByName(db, chat_name) == True:
        return "That chat name already exists"
    else: 
        db.conversations.insert_one(nombre) #Creates document within the conversations collection
        laide = dtb.getChatIDbyName(db, chat_name)
        return "The chat {} has been created with the ID {}".format(chat_name, laide)

#ADD USERS & ADD MESSAGES

@app.route("/chat/<chat_name>/adduser/<username>")
def addUserToChat(chat_name, username):
     check_user = dtb.checkUserExistsByName(db, username)
     print(check_user)
     check_chat = dtb.checkChatExistsByName(db, chat_name)
     print(check_chat)
     
     if  check_user == True:
         if check_chat == True:
            db.conversations.update_one({ "Chat name": f"{chat_name}" },{ "$push": {"Users": f"{username}"}})
            return "The user {} has been added to the chat: {}".format(username, chat_name)
     else:
         return "Error: either of them does not exist"

@app.route("/chat/<chat_name>/<username>/<message>")
def addMessagesToChat(chat_name, username, message):
    check_user = dtb.checkUserExistsByName(db, username)
    check_chat = dtb.checkChatExistsByName(db, chat_name)
    print(type(message))
    if  check_user == True:
        if check_chat == True:
            db.conversations.update_one({ "Chat name": chat_name }, { "$addToSet": { "Messages": f'{message}'}})
            return "The text '{}' sent by {} has been added to the chat: {}".format(message, username, message)
    else:
        return "Error: either of them does not exist"

app.run("0.0.0.0", 8000, debug=True)
