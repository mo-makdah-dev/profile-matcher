# campaigns_service/app/repositories/campaigns_repo.py
from typing import List
from app.models.campaign import Campaign

MOCK_CAMPAIGNS = [
    {
        "game": "mygame",
        "name": "mycampaign",
        "priority": 10.5,
        "matchers": {
            "level": {"min": 1, "max": 3},
            "has": {"country": ["US", "RO", "CA"], "items": ["item_1"]},
            "does_not_have": {"items": ["item_4"]},
        },
        "start_date": "2022-01-25 00:00:00Z",
        "end_date": "2022-02-25 00:00:00Z",
        "enabled": True,
        "last_updated": "2021-07-13 11:46:58Z",
    }
]

class CampaignsRepository:
    def __init__(self):
        # in-memory store with the mock campaigns
        self._store: List[Campaign] = [Campaign(**c) for c in MOCK_CAMPAIGNS]


    async def list_all(self) -> List[Campaign]:
        return list(self._store)
