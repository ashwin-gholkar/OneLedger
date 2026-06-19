from fastapi import FastAPI

from app.controllers.business_type_controller import router as business_type_router
from app.controllers.business_controller import router as business_router
from app.core.exception_handlers import register_exception_handlers
from app.middlewares.error_handler_middleware import ErrorHandlerMiddleware

app = FastAPI()

app.add_middleware(ErrorHandlerMiddleware)
register_exception_handlers(app)
app.include_router(business_type_router)
app.include_router(business_router)
