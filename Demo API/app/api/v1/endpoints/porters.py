from fastapi import APIRouter, HTTPException
from app.db.schemas.porter import Porter
from app.db.client import supabase

router = APIRouter()

@router.get("/porters")
async def get_porters():
    response = supabase.table("porters").select("*").execute()
    if response:
        return response.data
    raise HTTPException(status_code=500, detail="Failed to get porters")

@router.post("/porters")
async def create_porter(porter: Porter):
    response = supabase.table("porters").insert(porter.dict()).execute()
    if response:
        return response.data
    raise HTTPException(status_code=500, detail="Failed to create porter")
