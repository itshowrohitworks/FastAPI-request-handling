# FastAPI Requesting Handling:

The repo demonstrates FastAPI request handling, especially the difference between:

Blocking I/O

Async / Non-blocking I/O

How FastAPI handles multiple requests concurrently

# Working:
FastAPI uses Python async/await + event loop so when a request waits for I/O (DB/API/file), other requests can run instead of blocking the server.