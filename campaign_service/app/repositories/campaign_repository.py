from typing import List
from app.models.campaign import Campaign
from app.db import campaigns_collection

class CampaignsRepository:
    def __init__(self) -> None:
        pass

    async def list_all(self) -> List[Campaign]:
        cursor = campaigns_collection.find({}, {"_id": 0})  # exclude _id
        docs: List[Campaign] = []
        async for d in cursor:
            docs.append(Campaign(**d))
        return docs
