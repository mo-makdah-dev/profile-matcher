from typing import List, Optional
from app.models.campaign import Campaign
from app.repositories.campaign_repository import CampaignsRepository

class CampaignsService:
    def __init__(self, repo: Optional[CampaignsRepository] = None):
        self.repo = repo or CampaignsRepository()

    async def get_campaigns(self) -> List[Campaign]:
        return await self.repo.list_all()
