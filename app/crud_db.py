from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2 
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True

# make a database connnection
while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'Q!W@E#123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection successful!!!")
        break
    except Exception as error:
        print("database connection failed!!!")
        print("error: ", error)
        time.sleep(2)

my_posts = [{"title":"title1", "content":"content1", "id": 1},
            {"title":"title2", "content":"content2", "id": 2}]


def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post

# retrive posts
@app.get("/posts")
def get_posts():
    # print(post.title)
    cursor.execute("""select * from posts""")
    posts = cursor.fetchall()
    # print(posts)
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post:Post): 
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0, 1000000)
    # my_posts.append(post_dict)
    
    # cursor.execute(f"insert into posts (title, content) values ({post.title}, {post.content})") #this exposes the database to sql injection
    
    cursor.execute("""insert into posts (title, content) values (%s, %s) returning *""", (post.title, post.content)) # need to pass tuple 

    new_post = cursor.fetchone()
    conn.commit() #commit the changes to the database

    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id:int):

    cursor.execute("""select * from posts where id = %s""", (id,)) #instead of converting the id into string and procedding with that, we have to pass the id as a tuple.
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found!!!")

    return {"post via id": post}


def find_index(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.delete("/posts/{id}", status_code=status.HTTP_404_NOT_FOUND)
def delete_post(id:int):
    cursor.execute("""delete from posts where id = %s returning *""", (id, ))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Post with id:{id} not found!!!")
    conn.commit()
    return {"Deleted data" : post}


@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    cursor.execute("""update posts set title = %s, content = %s, published = %s where id = %s returning *""", (post.title, post.content, post.published, id))
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id = {id} doesnot exist!!!")
    
    return {'data':updated_post}
