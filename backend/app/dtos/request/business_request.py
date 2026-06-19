from pydantic import BaseModel


class CreateBusinessRequest(BaseModel):
    name: str
    business_type: str
    gst_no: str
    phone: str
    email: str
    address: str
