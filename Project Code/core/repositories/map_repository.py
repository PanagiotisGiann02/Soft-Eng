# hiking_buddy/core/repositories/map_repository.py

from domain.models.map import Map

class MapRepository:
    def get_map(self) -> Map:
        raise NotImplementedError

    def save(self, map_obj: Map) -> None:
        raise NotImplementedError

class InMemoryMapRepository(MapRepository):
    def __init__(self, initial_map: Map):
        self._map = initial_map

    def get_map(self) -> Map:
        return self._map

    def save(self, map_obj: Map) -> None:
        self._map = map_obj
        print(f"[MapRepository] Map {map_obj.id} saved.")
