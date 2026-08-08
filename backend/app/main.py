from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.routes import auth_router, session_router, provider_router, transaction_router, expense_router, report_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router, prefix=settings.API_V1_STR)
app.include_router(session_router.router, prefix=settings.API_V1_STR)
app.include_router(provider_router.router, prefix=settings.API_V1_STR)
app.include_router(transaction_router.router, prefix=settings.API_V1_STR)
app.include_router(expense_router.router, prefix=settings.API_V1_STR)
app.include_router(report_router.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Universal Wakala Management System API is Running!"}