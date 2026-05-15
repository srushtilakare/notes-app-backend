from fastapi import FastAPI
from app.database import engine
import app.models as models

from app.routes import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users.router)


@app.get("/")
def home():
    return {"message": "Notes App Backend Running"}