from pydantic import BaseModel

class CreateGame(BaseModel):
    id: int
    name: str