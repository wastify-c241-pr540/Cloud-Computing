from pydantic import BaseModel

class Porter(BaseModel):
    user_id: int
    timestamp: str
