from gettext import find
from urllib import response
from utils.mongo import collection
from service.operation import add, delete, update, find_data
from model.todomodel import Todo
from utils.logging import logg
from fastapi import FastAPI

app=FastAPI()


# TESTING TO GET DATA-----------
@app.get("/")
def show():
    return "Hi there"

# CREATING DATA------------
@app.post("/add/todo")
def add_data(todo:Todo):
    a= add(todo)
    try:
        if a:
            logg.info("Post api runs well")
            return "Added successfuly"
    except:
        logg.exception("Error happend")

#EDITING DATA----------
@app.put("/edit/{title}")
def edit(title:str, todo:Todo):
    b=update(title, todo)
    try:
        if b:
            logg.info("Post api runs well")
            return "Updated successfully"
    except:
        logg.exception("Error happend in put")


# GETTING DATA----------
@app.get("/find/{title}")
def search(title:str):
    return find_data(title)


# DELETE---------
@app.delete("/remove/{title}")
def remove(title:str):
    d= delete(title)
    if d:
        return(f"You have successfully deleted the task of {title}")


