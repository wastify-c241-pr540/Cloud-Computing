from fastapi import APIRouter, HTTPException
from app.db.schemas.users import User
from app.db.client import supabase

router = APIRouter()

@router.get("/users")
async def get_users():
    response = supabase.table("users").select("*").execute()
    if response:
        return response.data
    raise HTTPException(status_code=response.status_code, detail=response.error_message)

@router.post("/users")
async def create_user(user: User):
    response = supabase.table("users").insert(user.dict()).execute()
    if response:
        return response.data
    raise HTTPException(status_code=400, detail=response.error_message)
