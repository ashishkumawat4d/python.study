from typing import Union

from fastapi import FastAPI

app = FastAPI()



 # defines our route for HTTP git method at the root URL
 
@app.get("/")
def read_root():
    return{"Hello":"World"}  




@app.get("/items/{item_id}")
def read_item(item_id: int,q:Union[str,None] = None):
    return {"item":item_id,"q":q}