from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Inquiry(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Contact email")
    type: str = Field(..., description="Project type")
    message: Optional[str] = Field(None, description="Message")
