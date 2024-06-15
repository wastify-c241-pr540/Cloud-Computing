from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    user_id: int
    username: str
    full_name: Optional[str] = None
    email: str
    password: str

class GarbageStats(BaseModel):
    garbage_id: int
    user_id: int
    garbage_type: bool
    garbage_count: int
    user: Optional[User] = None

class Porter(BaseModel):
    user_id: int
    timestamp: str

class GarbageInfo(BaseModel):
    pull_id: int
    user_id: int
    garbage_img: Optional[str] = None
    garbage_classification: bool = None
    location: str
    fee: int
    garbage_description: Optional[str] = None
    is_taken_by: Optional[int] = None