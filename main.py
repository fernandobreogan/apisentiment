from pymongo import MongoClient
from flask import Flask, request

client = MongoClient('mongodb://localhost:27017/')
db = client['eslac']

app = Flask(__name__)

@app.route("/new_user")
def createUser (name):
    nombre = {"Name":f"{name}"}
    db.users.insert_one(nombre)
    return "The user {} has been created".format(name)

@app.route("/user_info")
def getUserInfo(name):
    usuario = db.users.find({"Name":f"{name}"}, projection={name:True})
    return list(usuario)

def totalChats():
    total = db.conversations.countDocuments({})
    return total

def createChat(*users):
    return chatID

pp.run("0.0.0.0", 5000, debug=True)


"""
#Para generars las ID's
db.collection.distinct()¶
max()+1


"""