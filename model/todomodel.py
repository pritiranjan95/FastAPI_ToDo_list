from pydantic import BaseModel

class Todo(BaseModel):
    Name: str
    Date: str
    Title: str
    Text: str | None
