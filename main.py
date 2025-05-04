import sys
import os
from fastapi import FastAPI
from routes.route import router

# Add the firebase directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

# Include the router
app.include_router(router)