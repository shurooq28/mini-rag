from fastapi import FastAPI
app = FastAPI()

def welcome():
    return {
        "message":"Hello World!"
    }
