from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello, World"}

# Run the script: uvicorn main:app --reload