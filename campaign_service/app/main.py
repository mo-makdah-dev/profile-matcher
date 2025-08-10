from fastapi import FastAPI
from app.routers.campaign_controller import router as campaigns_router

app = FastAPI(title="Campaigns Service")
app.include_router(campaigns_router)
