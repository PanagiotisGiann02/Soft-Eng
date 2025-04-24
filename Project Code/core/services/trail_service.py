# hiking_buddy/core/services/trail_service.py


class TrailService:
    def __init__(self):
        self.trails = [
            {
                "user_name": "Test User",
                "date": "March 6, 2025 at 4:34 PM",
                "location": "Patras, Peloponnese, Western Greece",
                "trail_name": "Patras - Kato Vasiliki",
                "distance": "16.69 km",
                "elevation": "80 m",
                "duration": "1h 23m",
                "map_image": "assets/mock_map.png",
            },
            {
                "user_name": "Test User",
                "date": "March 6, 2025 at 4:34 PM",
                "location": "Patras, Peloponnese, Western Greece",
                "trail_name": "Patras - Kato Vasiliki",
                "distance": "16.69 km",
                "elevation": "80 m",
                "duration": "1h 23m",
                "map_image": "assets/mock_map.png",
            },
        ]

    def get_all_trails(self):
        return self.trails
