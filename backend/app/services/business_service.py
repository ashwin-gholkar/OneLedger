from typing import List
from typing import Optional

from sqlalchemy.orm import Session

from app.dtos.request.business_request import CreateBusinessRequest
from app.models.business import Business


def create_business(db: Session, request: CreateBusinessRequest) -> Business:
    business = Business(**request.model_dump())
    db.add(business)
    db.commit()
    db.refresh(business)
    return business


def list_businesses(db: Session) -> List[Business]:
    return db.query(Business).order_by(Business.id.desc()).all()


def get_business(db: Session, business_id: int) -> Optional[Business]:
    return db.query(Business).filter(Business.id == business_id).first()
