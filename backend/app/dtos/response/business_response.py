from pydantic import BaseModel
from pydantic import ConfigDict


class BusinessResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    business_type: str
    gst_no: str
    phone: str
    email: str
    address: str
