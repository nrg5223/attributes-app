from pydantic import BaseModel

class AttributeBase(BaseModel):
    name: str

class AttributeCreate(AttributeBase):
    pass

class AttributeRead(AttributeBase):
    id: int

    class Config:
        orm_mode = True # let Pydantic read data from Attribute objs