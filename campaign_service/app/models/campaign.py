from pydantic import BaseModel
from typing import Optional, List

class LevelMatcher(BaseModel):
    min: Optional[int] = None
    max: Optional[int] = None

class HasMatcher(BaseModel):
    country: Optional[List[str]] = None
    items: Optional[List[str]] = None

class DoesNotHaveMatcher(BaseModel):
    items: Optional[List[str]] = None

class Matchers(BaseModel):
    level: Optional[LevelMatcher] = {}
    has: Optional[HasMatcher] = {}
    does_not_have: Optional[DoesNotHaveMatcher] = {}

class Campaign(BaseModel):
    game: str
    name: str
    priority: float
    matchers: Matchers = Matchers()
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    enabled: bool = True
    last_updated: Optional[str] = None
