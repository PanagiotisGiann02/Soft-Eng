# hiking_buddy/core/repositories/hotspot_repository.py

from domain.models.hotSpot import HotSpot


class HotSpotRepository:
    def __init__(self, hotspot_model: HotSpot):
        self.hotspot_model = hotspot_model

    def get_hotspots(self):
        return self.hotspot_model.getHotSpots()
