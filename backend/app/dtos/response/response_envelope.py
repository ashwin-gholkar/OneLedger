from typing import Generic
from typing import Optional
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ResponseEnvelope(BaseModel, Generic[T]):
    status_code: int
    message: str
    result: Optional[T] = None


def build_response(
    status_code: int,
    message: str,
    result: Optional[T] = None,
) -> ResponseEnvelope[T]:
    return ResponseEnvelope[T](
        status_code=status_code,
        message=message,
        result=result,
    )
