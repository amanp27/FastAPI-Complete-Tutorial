from fastapi import FastAPI
import redis
import json
import joblib
import hashlib
from pydantic import BaseModel

app = FastAPI()
redis_client = redis.Redis(host= 'localhost', port= 6379, db= 0)

model = joblib.load("/home/tacktile/FastAPI-Complete-Tutorial/performance_optimization_and_monitoring/ml_caching/model.joblib")

class IrisFlower(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    def to_list(self):
        return [self.SepalLengthCm,
                self.SepalWidthCm,
                self.PetalLengthCm,
                self.PetalWidthCm]
    
    def cach_key(self):
        raw = json.dump(self.model_dump(), sort_keys = True)
        return f"Predict: {hashlib.sha256(raw.encode()).hexdigest()}"
    

app.post("/predict")
async def predict(data: IrisFlower):
    key = data.cache_key()

    cached_result = redis_client.get(key)
    if cached_result:
        print("Serving Prediction from Cached")
        return json.loads(cached_result)