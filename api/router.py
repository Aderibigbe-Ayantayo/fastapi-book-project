from fastapi import APIRouter
from api.routes import books

api_router = APIRouter()

# Ensure the prefix is set correctly to match expected test URLs
api_router.include_router(books.router, prefix="/books", tags=["Books"])
