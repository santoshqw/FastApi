from fastapi import FastAPI


app = FastAPI(title="FastAPI Starter")



@app.get("/")
def Home():
    return {"sucess":True,"message":"home page"}
