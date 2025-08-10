from fastapi import APIRouter, Query
from app.services.matcher_service import MatcherService

router = APIRouter(tags=["config"])
service = MatcherService()

@router.get("/get_client_config/{player_id}")
async def get_client_config(
    player_id: str,
    now: str = Query(
        None,
        description=(
            "Optional current time for matching, format 'YYYY-MM-DD HH:MM:SSZ'. "
            "Example: 2024-06-10 12:00:00Z. "
            "If omitted, server time (UTC) is used."
        )
    )
):
    return await service.get_client_config(player_id, now)
