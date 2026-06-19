from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.core.database import Base


class BusinessType(Base):
    __tablename__ = "business_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(String(255))

    businesses = relationship("Business", back_populates="business_type")


class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    business_type_id = Column(
        Integer,
        ForeignKey("business_types.id"),
        nullable=False,
    )
    gst_no = Column(String(50))
    phone = Column(String(20))
    email = Column(String(200))
    address = Column(String)

    business_type = relationship("BusinessType", back_populates="businesses")
