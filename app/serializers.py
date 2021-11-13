from pydantic import BaseModel


class DeviceCreate(BaseModel):

    class Config:
        orm_mode = True


class DeviceGet(BaseModel):
    id: int
    dev_id: str
    dev_type: str
    endpoints: list

    class Config:
        orm_mode = True


class Endpoint(BaseModel):
    comment: str

    class Config:
        orm_mode = True


class AnagramWords(BaseModel):
    first_word: str
    second_word: str
