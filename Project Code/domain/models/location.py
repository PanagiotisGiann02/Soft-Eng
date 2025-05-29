class Location:
    def __init__(
        self,
        id: int,
        lat: float,
        lng: float,
        name: str,
        description: str,
        address: str,
        category: str,
    ):
        self.id = id
        self.lat = lat
        self.lng = lng
        self.name = name
        self.description = description
        self.address = address
        self.category = category  # 'user', 'poi', 'trash', 'sos', 'event', 'route_wp'

    def getCoordinates(self):
        return (self.lat, self.lng)
