from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from services.auth_service import create_user, verify_user_credentials, create_access_token

router = APIRouter()

@router.post("/signup")
def signup(form_data: OAuth2PasswordRequestForm = Depends()):
    return create_user(form_data)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = verify_user_credentials(form_data)
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}
