class HotSpot:
    def __init__(self, id: int, location: dict, severity: int, reported_at: int):
        self.id = id
        self.location = location  # dict with 'lat' and 'lng'
        self.severity = severity
        self.reported_at = reported_at

    def getHotSpots(self):
        print("[HotSpot] Fetching hotspots...")
        return [self]
