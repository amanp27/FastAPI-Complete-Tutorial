import hashlib
import redis
from fastapi import FastAPI
import json

app = FastAPI()
redis_client = redis.Redis(host= "localhost", port= 6379, db= 0)

class PostRequest():
    post_id: int

def make_cache_key(post_id: int):
    raw = f"external_api:post_{post_id}"
    return hashlib.sha256(raw.encode()).hexdigest()

@app.post('/get-post')
async def get_post(data: PostRequest):
    cache_key = make_cache_key(data.post_id)

    cached_data = redis.client.get(cache_key)

    if cached_data:
        print("Server Cached Data")
        return json.loads(cached_data)
    
    print('Calling External API!')