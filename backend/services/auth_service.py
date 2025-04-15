import hashlib
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from database.connection import get_sql_connection
from jose import JWTError, jwt
from datetime import datetime, timedelta
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 600  # 10 hours

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None



def create_user(form_data):
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ?", form_data.username)
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = hashlib.sha256(form_data.password.encode()).hexdigest()
    cursor.execute("INSERT INTO Users (username, password_hash) VALUES (?, ?)", form_data.username, hashed_pw)
    conn.commit()
    conn.close()
    return {"message": "User created successfully"}

def verify_user_credentials(form_data):
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password_hash FROM Users WHERE username = ?", form_data.username)
    user = cursor.fetchone()
    conn.close()

    hashed_input = hashlib.sha256(form_data.password.encode()).hexdigest()
    if not user or hashed_input != user[1]:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return user[0]

def get_current_user(token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM Users WHERE username = ?", username)
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": row[0], "username": row[1]}
