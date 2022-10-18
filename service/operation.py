from ipaddress import collapse_addresses
from statistics import mode
from utils.mongo import collection

#insert data

def add(model):
    return collection.insert_one(model.__dict__)

def update(title, model):
    prev={"Title": title}
    next=model.__dict__
    
    return collection.update_one(prev,{"$set": next})

def find_data(title):
    return collection.find_one({"Title":title})

def delete(title):
    return collection.delete_one({"Title":title})

    

