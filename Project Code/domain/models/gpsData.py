class GPSData:
    def __init__(
        self,
        id: int,
        activity_id: int,
        lat: float,
        lng: float,
        altitude_m: float,
        speed_mps: float,
        timestamp,
    ):
        self.id = id
        self.activity_id = activity_id
        self.lat = lat
        self.lng = lng
        self.altitude_m = altitude_m
        self.speed_mps = speed_mps
        self.timestamp = timestamp

    def getCurrentLocation(self):
        print("[GPSData] Returning current GPS data...")
        return self
