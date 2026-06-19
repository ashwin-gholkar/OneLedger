from fastapi import status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.dtos.response.response_envelope import build_response


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=build_response(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    message="Internal server error",
                    result=None,
                ).model_dump(),
            )
