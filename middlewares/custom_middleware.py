from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

# Custom Middleware to measure request processing time, once the response is ready
class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(f"Request: {request.url.path} processed in {process_time:.5f} seconds")
        return response
    
app.add_middleware(TimerMiddleware)
    
@app.get("/hello")
async def hello():
    for _ in range(1000000):  # Simulate some processing time
        pass
    return {"message": "Hello, World!"}