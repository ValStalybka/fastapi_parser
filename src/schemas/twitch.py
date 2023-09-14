from datetime import datetime
from typing import List

from pydantic import BaseModel


class Game(BaseModel):
    name: str
    box_art_url: str
    igdb_id: str
    created_at: datetime = datetime.now()


class Stream(BaseModel):
    user_id: str
    user_login: str
    user_name: str
    game_id: str
    game_name: str
    title: str
    tags: List[str]
    viewer_count: int
    started_at: datetime
    language: str
    is_mature: bool
    created_at: datetime = datetime.now()
