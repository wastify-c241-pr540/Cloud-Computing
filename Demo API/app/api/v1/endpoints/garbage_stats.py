from fastapi import APIRouter, HTTPException
from app.db.schemas.garbage_stats import GarbageStats
from app.db.client import supabase

router = APIRouter()

@router.get("/garbage_stats")
async def get_garbage_stats():
    response = supabase.table("garbages_stats").select("*").execute()
    if response:
        garbage_stats = response.data
        for stats in garbage_stats:
            user_response = supabase.table("users").select("*").eq("user_id", stats['user_id']).single().execute()
            if user_response:
                stats['user'] = user_response.data
        return garbage_stats
    raise HTTPException(status_code=500, detail='Failed to get garbage stats')

@router.post("/garbage_stats")
async def create_garbage_stats(stats: GarbageStats):
    response = supabase.table("garbage_stats").insert(stats.dict(exclude={"user"})).execute()
    if response:
        return response.data
    raise HTTPException(status_code=500, detail="Failed to create garbage stats")
