from pydantic import BaseModel
from pydantic import ConfigDict


class BusinessTypeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str


class BusinessResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    business_type: BusinessTypeResponse
    gst_no: str
    phone: str
    email: str
    address: str
