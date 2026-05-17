# Notes App Backend API

A secure and scalable Notes Management Backend built using **FastAPI**, **SQLite**, and **JWT Authentication**.

This project supports:
- User Authentication
- CRUD Operations for Notes
- Secure Authorization
- Note Sharing Between Users
- Pin/Unpin Important Notes
- OpenAPI Documentation
- Live Deployment on Render

---

# Live Deployment

## API Docs
https://notes-app-backend-gnha.onrender.com/docs

## OpenAPI JSON
https://notes-app-backend-gnha.onrender.com/openapi.json

## About Endpoint
https://notes-app-backend-gnha.onrender.com/about

---

# Features

## Authentication
- User Registration
- User Login
- JWT Token Authentication
- Password Hashing using bcrypt

---

## Notes Management
- Create Notes
- Get All Notes
- Get Note By ID
- Update Notes
- Delete Notes

---

## Authorization & Security
- Protected Routes
- Ownership-based Access Control
- Shared User Access Validation

---

## Note Sharing
Users can securely share notes with other registered users.

Features:
- Share note with another user
- Prevent duplicate sharing
- Prevent self-sharing
- Shared users can access notes

---

## Extra Feature — Pin Notes ⭐
Implemented a productivity feature inspired by Google Keep:
- Pin Important Notes
- Unpin Notes
- Retrieve All Pinned Notes

---

# Tech Stack

- FastAPI
- Python
- SQLAlchemy
- SQLite
- JWT Authentication
- Uvicorn
- Render Deployment

---

# Project Structure

```bash
notes-app-backend/
│
├── app/
│   ├── routes/
│   │   ├── users.py
│   │   └── notes.py
│   │
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── requirements.txt
├── render.yaml
├── .gitignore
└── README.md

API Endpoints
Authentication
Method	Endpoint	Description
POST	/register	Register new user
POST	/login	Login user
Notes
Method	Endpoint	Description
POST	/notes	Create note
GET	/notes	Get all notes
GET	/notes/{note_id}	Get note by ID
PUT	/notes/{note_id}	Update note
DELETE	/notes/{note_id}	Delete note
Sharing
Method	Endpoint	Description
POST	/notes/{note_id}/share	Share note with another user
Pin Notes
Method	Endpoint	Description
PUT	/notes/{note_id}/pin	Pin/Unpin note
GET	/notes/pinned	Get pinned notes

Setup Instructions

Clone Repository
git clone repo
cd notes-app-backend
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt
Run Server
uvicorn app.main:app --reload
Open Swagger Docs
http://127.0.0.1:8000/docs


Author

Srushti Lakare