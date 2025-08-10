import os
from datetime import datetime, timezone
from typing import List, Optional

import httpx
import logging

from app.models.player import Player
from app.models.campaign import Campaign
from app.repositories.player_repository import PlayerRepository


CAMPAIGNS_SERVICE_URL = os.getenv("CAMPAIGNS_SERVICE_URL", "http://campaign_service:8001")


class MatcherService:
    def __init__(self, repo: Optional[PlayerRepository] = None):
        self.repo = repo or PlayerRepository()

    async def get_client_config(self, player_id: str, now: Optional[str] = None) -> Optional[Player]:
        """
        1) Load player by id
        2) Fetch campaigns from mock API
        3) Match player against each campaign
        4) Update player's active_campaigns via repo
        5) Return updated player
        """
        player = await self.repo.get_by_id(player_id)
        
        if not player:
            return None
        

        campaigns = await self._fetch_campaigns()
        now_utc = self._parse_datetime(now) or datetime.now(timezone.utc)
        
        
        logging.info(f"Matching player {player_id} against {len(campaigns)} campaigns at {now_utc.isoformat()}")

        matched_names: List[str] = []
        for camp in campaigns:
            if self._matches(player, camp, now_utc):
                if camp.name:
                    matched_names.append(camp.name)

        # Update player's active campaigns
        updated = await self.repo.update_active_campaigns(player_id, matched_names)
        return updated

    # -------------------- Campaigns API --------------------
    async def _fetch_campaigns(self) -> List[Campaign]:
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(f"{CAMPAIGNS_SERVICE_URL}/campaigns", timeout=10)
                r.raise_for_status()
                campaigns_data = r.json()
                return [Campaign(**item) for item in campaigns_data] if isinstance(campaigns_data, list) else []
        except Exception:
            return []

    # -------------------- Match checks (per category) --------------------
    def _matches(self, player: Player, campaign: Campaign, now_utc: datetime) -> bool:
        return (
            self._match_enabled(campaign)
            and self._match_date_window(campaign, now_utc)
            and self._match_level(player, campaign)
            and self._match_has_country(player, campaign)
            and self._match_has_items(player, campaign)
            and self._match_does_not_have_items(player, campaign)
        )

    @staticmethod
    def _match_enabled(campaign: Campaign) -> bool:
        return campaign.enabled

    def _match_date_window(self, campaign: Campaign, now_utc: datetime) -> bool:
        start = self._parse_datetime(campaign.start_date)
        end = self._parse_datetime(campaign.end_date)
        if start and now_utc < start:
            return False
        if end and now_utc > end:
            return False
        return True

    @staticmethod
    def _match_level(player: Player, campaign: Campaign) -> bool:
        level = campaign.matchers.level
        min_level = level.min
        max_level = level.max
        player_level = player.level
        if min_level is not None and player_level < min_level:
            return False
        if max_level is not None and player_level > max_level:
            return False
        return True

    @staticmethod
    def _match_has_country(player: Player, campaign: Campaign) -> bool:
        has = campaign.matchers.has
        countries = has.country
        if not countries:
            return True
        for country in countries:
            if player.country and player.country.strip().upper() == country.strip().upper():
                return True
        return False

    @staticmethod
    def _match_has_items(player: Player, campaign: Campaign) -> bool:
        has = campaign.matchers.has
        items = has.items
        if not items:
            return True
        inv = player.inventory
        for item in items:
            if inv.get(item, 0) <= 0:
                return False
        return True

    @staticmethod
    def _match_does_not_have_items(player: Player, campaign: Campaign) -> bool:
        does_not_have = campaign.matchers.does_not_have
        items = does_not_have.items
        if not items:
            return True
        inv = player.inventory
        for item in items:
            if inv.get(item, 0) > 0:
                return False
        return True

    # -------------------- Utils --------------------
    @staticmethod
    def _parse_datetime(dt_str: Optional[str]) -> Optional[datetime]:
        # Accept 'YYYY-MM-DD HH:MM:SSZ' and returns a UTC datetime object
        if not dt_str:
            return None
        s = str(dt_str).replace(" ", "T").replace("Z", "+00:00")
        try:
            dt = datetime.fromisoformat(s)
        except Exception:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
