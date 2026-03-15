from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello, World"}


"""
Blocking Endpoint: Runs synchronously
"""
@app.get("/blocking")
async def blocking_io():
    print("Hello")
    time.sleep(5)
    print("Bye")
    return {"message":"Operation Completed!"}

"""
Non-Blocking Async Endpoint: 
"""
@app.get("/nonblocking")
async def nonblocking():
    print("Not")
    await asyncio.sleep(5)
    print("Hello")
    return {"message":"Operation Completed!"}

"""
Normal Function: 
"""
@app.get("/normal")
def normal():
    print("Nothing")
    time.sleep(5)
    print("Happened")
    return {"message":"Nothing lol"}

# Run the script: uvicorn main:app --reload