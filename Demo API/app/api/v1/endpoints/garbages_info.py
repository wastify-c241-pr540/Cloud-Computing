from fastapi import APIRouter, HTTPException
from app.db.schemas.garbages_info import GarbageInfo
from app.db.client import supabase

router = APIRouter()

@router.get("/garbages_info")
async def get_garbages_info():
    response = supabase.table("garbages_info").select("*").execute()
    if response:
        garbages_info = response.data
        for info in garbages_info:
            user_response = supabase.table("users").select("*").eq("user_id", info['user_id']).single().execute()
            if user_response:
                info['user'] = user_response.data
        return garbages_info
    raise HTTPException(status_code=500, detail="Failed to get garbages info")

@router.post("/garbages_info")
async def create_garbages_info(info: GarbageInfo):
    response = supabase.table("garbages_info").insert(info.dict(exclude={"user"})).execute()
    if response:
        return response.data
    raise HTTPException(status_code=500, detail="Failed to create garbages info")
