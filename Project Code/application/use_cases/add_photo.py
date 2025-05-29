# hiking_buddy/application/use_cases/add_photo.py

from datetime import datetime
from domain.models.media import Media


class AddPhoto:
    def __init__(self, activity_repository, media_repository):
        self.activity_repository = activity_repository
        self.media_repository = media_repository

    def execute(self, activity_id: int, media_type: str, media_url: str) -> Media:
        activity = self.activity_repository.get_by_id(activity_id)
        if not activity:
            raise ValueError("Activity not found")

        media_id = self.media_repository.get_next_id()
        created_at = int(datetime.utcnow().timestamp())
        media = Media(
            id=media_id,
            ownerId=activity.user_id,
            type=media_type,
            url=media_url,
            createdAt=created_at,
        )
        self.media_repository.save(media)

        activity.addPhoto(media)
        self.activity_repository.save(activity)
        return media
