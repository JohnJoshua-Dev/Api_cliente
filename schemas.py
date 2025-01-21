from pydantic import BaseModel


class ClienteCreate(BaseModel):
    name: str
    email: str

class ClienteResponse(ClienteCreate):
    id: int
    name: str
    email: str


    class Config:
        from_attributes = True