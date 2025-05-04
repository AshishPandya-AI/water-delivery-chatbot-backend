from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

client = MongoClient(
    "mongodb+srv://ashishpandya7122000:ashish123@chatbot.uta4z.mongodb.net/todo_db?retryWrites=true&w=majority&tls=true&connectTimeoutMS=30000&socketTimeoutMS=30000"
)

db = client.todo_db
orders_collection = db["orders_collection"]  # Collection for orders

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)