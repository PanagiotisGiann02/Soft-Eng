class Route:
    def __init__(
        self,
        id,
        name,
        distance,
        expected_duration_sec,
        difficulty,
        elevation_gain_m,
        elevation_loss_m,
        path_gpx_uri,
    ):
        self.id = id
        self.name = name
        self.distance = distance
        self.expected_duration_sec = expected_duration_sec
        self.difficulty = difficulty
        self.elevation_gain_m = elevation_gain_m
        self.elevation_loss_m = elevation_loss_m
        self.path_gpx_uri = path_gpx_uri

    def getRouteDetails(self):
        return vars(self)

    def calculateEstimatedTime(self, avgSpeed):
        return self.distance / avgSpeed if avgSpeed > 0 else 0

    def getElevationProfile(self):
        return [self.elevation_gain_m, self.elevation_loss_m]

    def toGeoJson(self):
        return (
            f"{{'type': 'LineString', 'coordinates': 'GPX_FROM_{self.path_gpx_uri}'}}"
        )

    def validatePath(self):
        return self.path_gpx_uri.endswith(".gpx")

    def optimizePath(self, criteria):
        print(f"Optimizing path by {criteria}")
