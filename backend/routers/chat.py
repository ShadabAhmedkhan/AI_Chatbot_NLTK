from fastapi import APIRouter, Depends
from models.schemas import ChatRequest
from services.chat_service import get_bot_reply, get_chat_history
from services.auth_service import get_current_user

router = APIRouter()

@router.post("/")
def chat(payload: ChatRequest, current_user: dict = Depends(get_current_user)):
    return get_bot_reply(payload.message, current_user)

@router.get("/history")
def chat_history(current_user: dict = Depends(get_current_user)):
    return get_chat_history(current_user)
