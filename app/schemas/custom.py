from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: Optional[str] = "bearer"


class TokenData(BaseModel):
    email: Optional[str] = None

