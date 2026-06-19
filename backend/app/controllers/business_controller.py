from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dtos.request.business_request import CreateBusinessRequest
from app.dtos.response.business_response import BusinessResponse
from app.dtos.response.response_envelope import ResponseEnvelope
from app.dtos.response.response_envelope import build_response
from app.services.business_service import create_business
from app.services.business_service import get_business
from app.services.business_service import list_businesses

router = APIRouter(
    prefix="/api/businesses",
    tags=["Businesses"],
)


@router.post("/", response_model=ResponseEnvelope[BusinessResponse], status_code=201)
def add_business(
    request: CreateBusinessRequest,
    db: Session = Depends(get_db),
) -> ResponseEnvelope[BusinessResponse]:
    business = create_business(db, request)
    return build_response(
        status_code=201,
        message="Business created successfully",
        result=business,
    )


@router.get("/", response_model=ResponseEnvelope[List[BusinessResponse]])
def get_businesses(
    db: Session = Depends(get_db),
) -> ResponseEnvelope[List[BusinessResponse]]:
    businesses = list_businesses(db)
    return build_response(
        status_code=200,
        message="Businesses fetched successfully",
        result=businesses,
    )


@router.get("/{business_id}", response_model=ResponseEnvelope[BusinessResponse])
def get_business_by_id(
    business_id: int,
    db: Session = Depends(get_db),
) -> ResponseEnvelope[BusinessResponse]:
    business = get_business(db, business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")

    return build_response(
        status_code=200,
        message="Business fetched successfully",
        result=business,
    )
