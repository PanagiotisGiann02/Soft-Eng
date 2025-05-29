# hiking_buddy/application/use_cases/toggle_map_layer.py

from domain.models.map import Map
from core.repositories.map_repository import MapRepository


class ToggleMapLayer:
    def __init__(self, map_repository: MapRepository):
        self.map_repository = map_repository

    def execute(self, layer_name: str) -> Map:
        m = self.map_repository.get_map()
        m.toggleLayer(layer_name)
        self.map_repository.save(m)
        return m
