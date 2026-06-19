from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dtos.response.business_response import BusinessTypeResponse
from app.dtos.response.response_envelope import ResponseEnvelope
from app.dtos.response.response_envelope import build_response
from app.services.business_service import list_business_types

router = APIRouter(
    prefix="/api/business-types",
    tags=["Business Types"],
)


@router.get("/", response_model=ResponseEnvelope[List[BusinessTypeResponse]])
def get_business_types(
    db: Session = Depends(get_db),
) -> ResponseEnvelope[List[BusinessTypeResponse]]:
    business_types = list_business_types(db)
    return build_response(
        status_code=200,
        message="Business types fetched successfully",
        result=business_types,
    )
