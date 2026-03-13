import redis

r = redis.Redis(host= 'localhost', port= 6379, db= 0)

try:
    if r.ping():
        print("Connected to Redis!")
except ConnectionError:
    print("Reis Connection fails!")


r.set('framework', "FastAPI")
value = r.get('framework')
print(f"Strored value for: {value.decode()}")