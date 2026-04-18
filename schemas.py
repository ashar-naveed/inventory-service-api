from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    quantity: int

class ItemResponse(BaseModel):
    id: int
    name: str
    quantity: int

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str