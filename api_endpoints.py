from pymongo import MongoClient
import pymongo
import json
import argparse
import requests
from flask import Flask, request

from database import *
from api import *

client = MongoClient('mongodb://localhost:27017/') #Connection to the DB
db = client['eslac'] 

#CREATE USERS & CREATE CHATS

@app.route("/user/create/<username>")
def createUsers (username):
    nombre = {"Name":f"{username}"}
    names_match = db.users.find({"Name":f"{username}"}, projection={"Name":True})
    if len(list(names_match)) > 0: #Checks if the name is taken
        return "That chat name already exists"
    else: 
        db.users.insert_one(nombre) #Creates document within the users collection
        laide = getUserIdbyName(db, username)
        return laide


@app.route("/chat/create/<chat_name>")
def createChat (chat_name):
    nombre = {"Chat name":f"{chat_name}", "Users": {}}
    chats_match = db.conversations.find({"Chat name":f"{chat_name}"}, projection={"Chat name":True})
    if len(list(chats_match)) > 0: #Checks if the name is taken
        return "That chat name already exists"
    else: 
        db.conversations.insert_one(nombre) #Creates document within the conversations collection
        laide = getChatIDbyName(db, chat_name)
        return laide

#ADD USERS & ADD MESSAGES

@app.route("/chat/<chat_id>/adduser/<user_to_add>")
def addUserToChat(chat_id, user_to_add):
#Con el chatID y con los usuarios, UPDATEAR EL DOCUMENTO DENTRO DE LA COLECCIÓN
#devuelve: elchataidi
    
    db.conversations.update(
   { "$id": chat_id },
   { "$push": { "Users":user_to_add }})

    return chat_id

app.run("0.0.0.0", 8000, debug=True)