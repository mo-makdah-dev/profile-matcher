from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class Device(BaseModel):
    id: int
    model: str
    carrier: str
    firmware: str


class Clan(BaseModel):
    id: str
    name: str

class Player(BaseModel):
    player_id: str
    credential: str
    created: str
    modified: str
    last_session: Optional[str] = None
    total_spent: float = 0.0
    total_refund: float = 0.0
    total_transactions: int = 0
    last_purchase: Optional[str] = None
    active_campaigns: List[str] = []
    devices: List[Device] = []
    level: int = 1
    xp: int = 0
    total_playtime: int = 0
    country: Optional[str] = None
    language: Optional[str] = None
    birthdate: Optional[str] = None
    gender: Optional[str] = None
    inventory: Dict[str, int] = {}
    clan: Optional[Clan] = None
