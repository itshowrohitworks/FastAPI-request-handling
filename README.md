# FastAPI Requesting Handling:

The repo demonstrates FastAPI request handling, especially the difference between:

# Blocking I/O:
While waiting, server can't process other requests.

Blocking I/O stops the event loop until finished.

# Async / Non-blocking I/O:
This is a coroutine.

When await happens:
await asyncio.sleep(5)
The event loop switches to another request.

# Normal Function:
Runs each request with new thread.

# How FastAPI handles multiple requests concurrently

# Working:
FastAPI uses Python async/await + event loop so when a request waits for I/O (DB/API/file), other requests can run instead of blocking the server.

# Important Concepts:
## 1. Event Loop

Event loop = scheduler that runs async tasks.

Responsibilities:

schedule tasks

pause tasks

resume tasks

## 2. Coroutine

A function defined using:

async def my_function():

Example

async def fetch_data():
    await asyncio.sleep(1)

## 3. Awaitable Object

Something you can await.

Examples:

asyncio.sleep()
httpx request
database query
file read

## 4. Blocking vs Non-Blocking

Blocking:

time.sleep()
requests.get()

Non-Blocking:

asyncio.sleep()
httpx.AsyncClient()