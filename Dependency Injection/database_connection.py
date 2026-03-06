from fastapi import FastAPI, Depends

app = FastAPI()

#depency function to get database connection
def get_db():
    db = {'connection': 'mock db connection'}  #Establish the connection
    try:
        yield db  # Connect to the Route Handler
    finally:
        db.close() # Close the connection

#Endpoint (RH)
@app.get("/home")
async def home(db = Depends(get_db)): #define the dependency in the route handler
    return {'db_status': db['connection']}