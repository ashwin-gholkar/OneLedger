from typing import List
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.dtos.request.business_request import CreateBusinessRequest
from app.models.business import Business
from app.models.business import BusinessType


def list_business_types(db: Session) -> List[BusinessType]:
    return db.query(BusinessType).order_by(BusinessType.name.asc()).all()


def create_business(db: Session, request: CreateBusinessRequest) -> Business:
    business_type = (
        db.query(BusinessType)
        .filter(BusinessType.name == request.business_type.value)
        .first()
    )
    if business_type is None:
        raise HTTPException(status_code=404, detail="Business type not found")

    business = Business(
        name=request.name,
        business_type_id=business_type.id,
        gst_no=request.gst_no,
        phone=request.phone,
        email=request.email,
        address=request.address,
    )
    db.add(business)
    db.commit()
    db.refresh(business)
    return business


def list_businesses(db: Session) -> List[Business]:
    return (
        db.query(Business)
        .options(selectinload(Business.business_type))
        .order_by(Business.id.desc())
        .all()
    )


def get_business(db: Session, business_id: int) -> Optional[Business]:
    return (
        db.query(Business)
        .options(selectinload(Business.business_type))
        .filter(Business.id == business_id)
        .first()
    )
