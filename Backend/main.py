from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from Backend.database import get_sql_connection  # the one using pyodbc

# from nltk_bot import get_bot_response
from ml_bot import get_bot_response
from Backend.auth import create_access_token, decode_token
from typing import List
from pydantic import BaseModel

# Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or "*" for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password_hash FROM Users WHERE username = ?", username)
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="User not found")

    # Create a simple object to simulate the User
    return {"id": row[0], "username": row[1], "password": row[2]}


import hashlib

@app.post("/signup")
def signup(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ?", form_data.username)
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    # Example hash (replace with bcrypt if needed)
    hashed_pw = hashlib.sha256(form_data.password.encode()).hexdigest()

    cursor.execute("INSERT INTO Users (username, password_hash) VALUES (?, ?)", form_data.username, hashed_pw)
    conn.commit()
    conn.close()
    return {"message": "User created successfully"}


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password_hash FROM Users WHERE username = ?", form_data.username)
    user = cursor.fetchone()
    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    hashed_input = hashlib.sha256(form_data.password.encode()).hexdigest()

    if hashed_input != user[1]:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user[0]})
    return {"access_token": access_token, "token_type": "bearer"}

# model class for chat request
class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(payload: ChatRequest, current_user: dict = Depends(get_current_user)):
    bot_reply = get_bot_response(payload.message.lower()) or "Sorry, I didn't understand that."
    #database
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_history (user_id, user_message, bot_reply) VALUES (?, ?, ?)",
        current_user["id"], payload.message.lower(), bot_reply
    )
    conn.commit()
    conn.close()

    return {"reply": bot_reply}


@app.get("/chat/history")
def get_history(current_user: dict = Depends(get_current_user)):
    print(current_user)
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_message, bot_reply, timestamp FROM chat_history WHERE user_id = ?",
        current_user["id"]
    )
    rows = cursor.fetchall()
    conn.close()
    return [{"user_message": row[0], "bot_reply": row[1], "timestamp": row[2]} for row in rows]
