from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.core.database import Base


class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    business_type = Column(String(100))
    gst_no = Column(String(50))
    phone = Column(String(20))
    email = Column(String(200))
    address = Column(String)