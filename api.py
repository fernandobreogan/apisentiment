from pymongo import MongoClient
from flask import Flask, request

client = MongoClient('mongodb://localhost:27017/') #Connection to the DB
db = client['eslac'] 

app = Flask(__name__) #Creates the API
 
#TESTING THE API
@app.route("/test")
def test ():
    return "The API works!"