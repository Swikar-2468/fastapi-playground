from fastapi import FastAPI
from .routers import posts, users, auth, votes
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "https://www.google.com",
#     "http://localhost:3000"
# ]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], #allow all methods
    allow_headers=["*"],
)

print(settings)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")    
def root():
    return {"message": "hello world!!!"}