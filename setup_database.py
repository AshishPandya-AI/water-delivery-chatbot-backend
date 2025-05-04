from pymongo import MongoClient

# Singleton MongoDB client
def get_database():
    try:
        client = MongoClient(
            "mongodb+srv://ashishpandya7122000:SBKphuP0FM03fiov@chatbot.uta4z.mongodb.net/todo_db?retryWrites=true&w=majority&tls=true"
        )
        db = client["todo_db"]
        return db
    except Exception as e:
        print(f"Error: {e}")
        raise