from pydantic import BaseModel

class ProviderBase(BaseModel):
    name: str
    code: str

class ProviderCreate(ProviderBase):
    pass

class ProviderResponse(ProviderBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True