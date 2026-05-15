from fastapi import FastAPI
from app.database import engine
import app.models as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Notes App Backend Running"}