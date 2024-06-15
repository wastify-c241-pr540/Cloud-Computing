from pydantic import BaseModel, EmailStr
from typing import Optional
# from app.db.schemas.garbage_stats import GarbageStats

class User(BaseModel):
    user_id: int
    username: str
    full_name: Optional[str] = None
    email: str
    password: str
