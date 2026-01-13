from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select, delete
from .. import models


def get_favorite(db, user_id, podcast_id):
    result = db.execute(
        select(models.Favorite).where(
            models.Favorite.user_id == user_id,
            models.Favorite.podcast_id == podcast_id
        )
    )
    return result.scalar_one_or_none()


def is_podcast_favorited(db, user_id, podcast_id):
    result = db.execute(
        select(models.Favorite).where(
            models.Favorite.user_id == user_id,
            models.Favorite.podcast_id == podcast_id
        )
    )
    return result.scalar_one_or_none() is not None


def add_favorite(db, user_id, podcast_id):
    favorite = models.Favorite(user_id=user_id, podcast_id=podcast_id)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite


def remove_favorite(db, user_id, podcast_id):
    db.execute(
        delete(models.Favorite).where(
            models.Favorite.user_id == user_id,
            models.Favorite.podcast_id == podcast_id
        )
    )
    db.commit()


def get_user_favorite_podcasts(db, user_id, skip=0, limit=20):
    stmt = (
        select(models.Podcast)
        .join(models.Favorite)
        .where(models.Favorite.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .options(
            joinedload(models.Podcast.category),
            joinedload(models.Podcast.owner)
        )
    )
    return db.execute(stmt).scalars().all()
