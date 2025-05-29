# hiking_buddy/core/repositories/media_repository.py

from domain.models.media import Media


class MediaRepository:
    def get_next_id(self) -> int:
        raise NotImplementedError

    def save(self, media: Media) -> None:
        raise NotImplementedError


class InMemoryMediaRepository(MediaRepository):
    def __init__(self):
        self.media_store = {}
        self.current_id = 1

    def get_next_id(self) -> int:
        next_id = self.current_id
        self.current_id += 1
        return next_id

    def save(self, media: Media) -> None:
        self.media_store[media.id] = media
        print(f"[MediaRepository] Media {media.id} saved.")
