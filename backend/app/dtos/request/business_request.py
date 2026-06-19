from enum import Enum

from pydantic import BaseModel


class BusinessTypeName(str, Enum):
    CLOTHING = "CLOTHING"
    RETAIL = "RETAIL"
    GROCERY = "GROCERY"
    RESTAURANT = "RESTAURANT"
    CAFE = "CAFE"
    HARDWARE = "HARDWARE"
    ELECTRONICS = "ELECTRONICS"


class CreateBusinessRequest(BaseModel):
    name: str
    business_type: BusinessTypeName
    gst_no: str
    phone: str
    email: str
    address: str
