import pymongo
import json
from bson.objectid import ObjectId


#CHECK EXISTANCE
def checkUserExistsByName(db, username):
    user_exists = db.users.find({"Name":f"{username}"}, projection={"Name":True})
    if len(list(user_exists)) > 0:
        return True
    else:
        print("El usuario no existe")
        return False

def checkUserExistsByID(db, user_id):
    user_exists = list(db.users.find({"_id":ObjectId(user_id)}, projection={"_id":True}))
    if len(user_exists) > 0:
        return True
    else:
        return False

def checkChatExistsByName(db, chat_name):
    chat_exists = db.conversations.find({"Chat name":f"{chat_name}"}, projection={"Chat name":True})
    if len(list(chat_exists)) > 0:
        return True
    else:
        return False

def checkChatExistsByID(db, chat_id):

    chat_exists = list(db.conversations.find({"_id":ObjectId(chat_id)}, projection={"_id":True}))
    if len(chat_exists) > 0:
        return True
    else:
        return False


#BY NAME
def getUserIdbyName(db, username):
    #Get user's ID by inputting their name
    for i in db.users.find({"Name":f"{username}"}):
        ides = i.get('_id')
        if checkUserExistsByName(db, username) == False:
            return "The user doesn't exist"
        else:
            return json.dumps(ides, default=str)

def getChatIDbyName(db, chat_name):
    #Get chat ID by inputting its name
    for i in db.conversations.find({"Chat name":f"{chat_name}"}):
        ides = i.get('_id')
        return json.dumps(ides, default=str)

#BY ID
def getUserNamebyID(db, user_id):
    #Get user's name by inputting their ID
    for i in db.users.find({"_id":ObjectId(user_id)}):
        ides = i.get("Name")
    return json.dumps(ides, default=str)

def getChatNamebyID(db, chat_id):
    #Get chat name by inputting its ID
    for i in db.conversations.find({"_id":ObjectId(chat_id)}):
        ides = i.get("Chat name")
    return json.dumps(ides, default=str)