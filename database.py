import pymongo
import json

#CHECK EXISTANCE
def checkUserExistsByName (db, username):
    for _ in db.users.find({"Name":f"{username}"}):
        user_exists = db.users.find({"Name":f"{username}"}, projection={"Name":True})
        if len(list(user_exists)) > 0:
            return True
        else:
            return "The user does not exist"

def checkUserExistsByID (db, user_id):
    for _ in db.users.find({"_id":f"{user_id}"}):
        user_exists = db.users.find({"_id":f"{user_id}"}, projection={"_id":True})
        if len(list(user_exists)) > 0:
            return True
        else:
            return "The user does not exist"

def checkChatExistsByName(db, chat_name):
    for _ in db.conversations.find({"Chat name":f"{chat_name}"}):
        chat_exists = db.conversations.find({"Chat name":f"{chat_name}"}, projection={"Chat name":True})
        if len(list(chat_exists)) > 0:
            return True
        else:
            return "The chat does not exist"

def checkChatExistsByID(db, chat_id):
    for i in db.conversations.find({"_id":f"{chat_id}"}):
        chat_exists = db.conversations.find({"_id":f"{chat_id}"}, projection={"_id":True})
        if len(list(chat_exists)) > 0:
            return True
        else:
            return "The chat does not exist"


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
    for i in db.users.find({"_id":f"{user_id}"}):
        ides = i.get("Name")
    return json.dumps(ides, default=str)

def getChatNamebyID(db, chat_id):
    #Get chat name by inputting its ID
    for i in db.conversations.find({"_id":f"{chat_id}"}):
        ides = i.get("Chat name")
    return json.dumps(ides, default=str)