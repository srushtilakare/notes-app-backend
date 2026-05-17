from fastapi import FastAPI
from app.database import engine
import app.models as models

from app.routes import users, notes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(notes.router)


@app.get("/")
def home():
    return {"message": "Notes App Backend Running"}

@app.get("/about")
def about():

    return {
        "name": "Srushti Lakare",
        "email": "srushti1924@gmail.com",

        "my_features": {

            "JWT Authentication":
            "Implemented secure JWT-based authentication for protected APIs.",

            "Note Sharing":
            "Users can securely share notes with other registered users.",

            "Ownership Protection":
            "Only note owners or shared users can access notes.",

            "Password Hashing":
            "Passwords are securely hashed using bcrypt."
        }
    }