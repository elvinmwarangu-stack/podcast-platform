from pydantic import BaseModel
from typing import List
from .podcast import PodcastOut

class FavoriteCreate(BaseModel):
    podcast_id: int

class FavoriteOut(BaseModel):
    id: int
    user_id: int
    podcast_id: int
    created_at: datetime

class Config:
    from_attributes = True

class FavoriteList(BaseModel):
    favorites: List[PodcastOut]