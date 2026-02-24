from fastapi import FastAPI
from routes.auth_routes import router
from db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
	return {"success": True, "message": "home page"}