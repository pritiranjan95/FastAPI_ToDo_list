import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
db= client["TODO"]
collection=db["todolist"]

# collection.insert_one({"name": "bapi"})  #used for testing