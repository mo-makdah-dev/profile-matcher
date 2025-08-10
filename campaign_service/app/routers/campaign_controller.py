from fastapi import APIRouter
from typing import List
from app.models.campaign import Campaign
from app.services.campaign_service import CampaignsService

router = APIRouter(prefix="/campaigns", tags=["campaigns"])
service = CampaignsService()

@router.get("", response_model=List[Campaign])
async def list_campaigns():
    return await service.get_campaigns()
