from fastapi import FastAPI
app = FastAPI()

@app.get("/welcome")
def welcome():
    return {
        "message":"Hello World!"
    }
print([route.path for route in app.routes])
