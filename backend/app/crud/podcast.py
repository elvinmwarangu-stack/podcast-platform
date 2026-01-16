from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from .. import models, schemas


def get_podcast(db, podcast_id):
    return db.execute(
        select(models.Podcast)
        .options(joinedload(models.Podcast.category), joinedload(models.Podcast.owner))
        .where(models.Podcast.id == podcast_id)
    ).scalar_one_or_none()


def get_podcasts(db, skip=0, limit=20):
    stmt = (
        select(models.Podcast)
        .options(joinedload(models.Podcast.category), joinedload(models.Podcast.owner))
        .offset(skip)
        .limit(limit)
    )
    return db.execute(stmt).scalars().all()


def create_podcast(db, podcast, owner_id):
    podcast_data = dict(podcast)
    # Convert Pydantic Url objects to strings for database compatibility
    if podcast_data.get('cover_image_url'):
        podcast_data['cover_image_url'] = str(podcast_data['cover_image_url'])
    
    db_podcast = models.Podcast(
        **podcast_data,
        owner_id=owner_id,
    )
    db.add(db_podcast)
    db.commit()
    db.refresh(db_podcast)
    return get_podcast(db, db_podcast.id)


def update_podcast(db, podcast_id, podcast_update):
    podcast = db.get(models.Podcast, podcast_id)
    if not podcast:
        return None

    update_data = dict(podcast_update)
    # Convert Pydantic Url objects to strings for database compatibility
    if update_data.get('cover_image_url'):
        update_data['cover_image_url'] = str(update_data['cover_image_url'])
    
    for key, value in update_data.items():
        setattr(podcast, key, value)

    db.add(podcast)
    db.commit()
    db.refresh(podcast)
    return get_podcast(db, podcast_id)
