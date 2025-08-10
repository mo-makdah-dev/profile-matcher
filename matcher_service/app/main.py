from fastapi import FastAPI
from app.routers.matcher_controller import router as matcher_router

app = FastAPI(title="Profile Matcher Service")
app.include_router(matcher_router)
