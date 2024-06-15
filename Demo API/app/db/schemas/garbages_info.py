from pydantic import BaseModel
from typing import Optional

class GarbageInfo(BaseModel):
    pull_id: int
    user_id: int
    garbage_img: Optional[str] = None
    garbage_classification: Optional[bool] = None
    location: str
    fee: int
    garbage_description: Optional[str] = None
    is_taken_by: Optional[int] = None
