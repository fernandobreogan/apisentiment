import pymongo
import json

#CHECK EXISTANCE
def checkUserExistsByName (db, username):
    for i in db.users.find({"Name":f"{username}"}):
        user_exists = db.users.find({"Name":f"{username}"}, projection={"Name":True})
        if len(list(user_exists)) > 0:
            return True

#def checkUserExistsByID ():
    #for i in db.users.find({"Name":f"{username}"}):
#def checkChatExistsByName(chat_name):
    #for i in db.conversations.find({"Chat name":f"{chat_name}"}):
#def checkChatExistsByID(chat_id):
    #for i in db.conversations.find({"_id":f"{chat_id}"}):

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
def getUserNamebyID(db, chat_id):
    #Get chat ID by inputting its name
    for i in db.users.find({"_id":f"{chat_id}"}):
        ides = i.get("Name")
    return json.dumps(ides, default=str)

def getChatNamebyID(db, user_id):
    #Get chat ID by inputting its name
    for i in db.conversations.find({"_id":f"{user_id}"}):
        ides = i.get("Chat name")
    return json.dumps(ides, default=str)