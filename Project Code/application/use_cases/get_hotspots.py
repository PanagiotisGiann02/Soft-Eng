# hiking_buddy/application/use_cases/get_hotspots.py


class GetHotSpots:
    def __init__(self, hotspot_repository: HotSpotRepository):
        self.repo = hotspot_repository

    def execute(self):
        print("[UseCase] Retrieving hotspots")
        return self.repo.get_hotspots()
