from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting":"Hello world"}

@app.get("/users/{user_id}")
async def user(user_id: str):
    return {"user_id":user_id}

@app.get("/getUserInfo")
def getUserInfo(id: int, name: str):
      return [{
          "id" : id,
          "firstName" : name
      }]
