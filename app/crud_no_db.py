from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel): #extend basemodel
    # define schema
    title:str   #require title to be string, so this does a level of data validation
    content:str
    published:bool = True
    rating: Optional[int] = None


# path operation decorator or route
# get is one of the http methods, others include post, put, delete
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}

# aync : perofmring a task and while waiting for the result, it can perform other tasks. aynchronous programming is a programming paradigm that allows for non-blocking operations, which can improve the performance and responsiveness of applications. In FastAPI, you can define asynchronous path operations using the `async def` syntax. This allows the server to handle multiple requests concurrently without blocking the execution of other tasks while waiting for I/O operations to complete.
# --reload is used in the terminal to automatically reload the server whenever you make changes to the code. This is particularly useful during development, as it allows you to see the effects of your changes immediately without having to manually restart the server each time. When you run the FastAPI application with `uvicorn main:app --reload`, it will watch for changes in the code and reload the server whenever a change is detected, making the development process more efficient and seamless.

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/posts")
# def create_post(payload: dict = Body(...)):  # the body field is being made a dictionary and it is being assigned to payload.
#     print(payload)
#     return {"new_post":f"Title = {payload['title']}, content:{payload['content']}"}
    
def create_posts(post:Post): #refrenced the Post, the post if it satisfies the above requirements then only it gets assigned to post
    print(post) #here, post already acts as an instance/object of class Post and is not a dict like payload.
    # print(post.dict())
    return {"Data" : post.dict()}
