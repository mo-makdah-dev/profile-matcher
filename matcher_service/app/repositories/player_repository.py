from typing import List, Optional
from app.models.player import Player
from app.db import players_collection
from pymongo import ReturnDocument

class PlayerRepository:
    def __init__(self) -> None:
        pass

    async def get_by_id(self, player_id: str) -> Optional[Player]:
        player_data = await players_collection.find_one({"player_id": player_id})
        if player_data:
            return Player(**player_data)
        return None

    async def update_active_campaigns(self, player_id: str, campaign_names: list[str]) -> Optional[Player]:
        result = await players_collection.find_one_and_update(
            {"player_id": player_id},
            {"$set": {"active_campaigns": campaign_names}},
            return_document=ReturnDocument.AFTER
        )
        if result:
            return Player(**result)
        return None

