from pymongo import MongoClient
import pymongo
import json
import argparse
import requests
from flask import Flask, request
import database as dtb

#CONNECTION TO THE DB
client = MongoClient('mongodb://localhost:27017/')
db = client['eslac']  

#CREATING AND TESTING THE API
app = Flask(__name__)

@app.route("/test")
def test ():
    return {"Success":"The API works!"}

#CREATE USERS & CREATE CHATS
@app.route("/user/create/<username>")
def createUsers (username):
    nombre = {"Name":f"{username}"}
    laide = dtb.getUserIdbyName(db, username)
    
    if dtb.checkUserExistsByName(db, username) == True:
        return {"Error. That user already exists with the ID": f'{laide}'}
    else: 
        db.users.insert_one(nombre) #Creates document within the users collection
        laide = dtb.getUserIdbyName(db, username)
        return {f"The user {username} has been created with the ID": f'{laide}'}


@app.route("/chat/create/<chat_name>")
def createChat (chat_name):
    nombre = {"Chat name":f"{chat_name}", "Users": [], "Messages":[]}
    laide = dtb.getChatIDbyName(db, chat_name)
    
    if dtb.checkChatExistsByName(db, chat_name)== True:
        return {f"Error. The chat name {chat_name} exists with the ID": f'{laide}'}
    else: 
        db.conversations.insert_one(nombre) #Creates document within the conversations collection
        laide = dtb.getChatIDbyName(db, chat_name)
        return {f"The chat {chat_name} has been created with the ID": f'{laide}'}

#ADD USERS & ADD MESSAGES
@app.route("/chat/<chat_name>/adduser/<username>")
def addUserToChat(chat_name, username):
    chatID = dtb.getChatIDbyName(db, chat_name)

    if dtb.checkUserExistsByName(db, username) == True:
        if dtb.checkChatExistsByName(db, chat_name) == True:
            db.conversations.update_one({ "Chat name": f"{chat_name}" },{ "$push": {"Users": f"{username}"}})
            return {f"The user {username} has been added to the chat {chat_name} with the chatID" : f'{chatID}'}
    else:
        return "Error: either of them does not exist"

@app.route("/chat/<chat_name>/<username>/<message>")
def addMessagesToChat(chat_name, username, message):
    chatID = dtb.getChatIDbyName(db, chat_name)
    if  dtb.checkUserExistsByName(db, username) == True:
        if dtb.checkChatExistsByName(db, chat_name) == True:
            db.conversations.update_one({ "Chat name": chat_name }, { "$push": {"Messages":{ f"{username}": f'{message}'}}})
            return {f"The text {message} sent by the user {username} has been added to the chat {chat_name} with the chatID" : f'{chatID}'} #TO-DO: make this the messageID
    else:
        return "Error: either of them does not exist"

app.run("0.0.0.0", 8000, debug=True)
