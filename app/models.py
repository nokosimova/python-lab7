from pydantic import BaseModel

class Word(BaseModel):
    name: str
    definition: str | None = None

class CreateRequest(Word):
    pass

class UpdateRequest(BaseModel):
    definition: str | None = None

class GetResponse(Word):
    id: int

    class Config:
        orm_mode = True