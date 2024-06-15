from pydantic import BaseModel
from typing import Optional
# from app.db.schemas.user import User
# from app.db.schemas.user import User
from .users import User

class GarbageStats(BaseModel):
    garbage_id: int
    user_id: int
    garbage_type: bool
    garbage_count: int
    user: Optional[User] = None
