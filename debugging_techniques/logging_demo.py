import logging
from fastapi import FastAPI

app = FastAPI()

logging.basicConfig(
    level= logging.INFO,
    format= "[%(asctime)s (line %(lineno)d) - %(levelname)s] - %(message)s",
    datefmt= "%m-%d-%Y %H:%M:%S"
)

@app.get('/')
def debug_route():
    logging.info('Bebug endpoint hit.')
    logging.info('Yeh kya bak rhe ho')
    return {'message': 'Checl logs!'}