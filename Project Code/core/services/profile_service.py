# Suggested path: hiking_buddy/core/services/profile_service.py

class ProfileService:
    def get_profile_data(self):
        return {
            "username": "Test User",
            "location": "Patra, West Greece, Greece",
            "followers": 111,
            "following": 125,
            "about": "Passionate about running, BBQ and waiting for your feedback to my activities. Happy to be a human being!",
            "is_premium": True,
            "trails": [
                {
                    "title": "Patra, Kataphygio Naupaktos and Limni from Windmills Panachaiko",
                    "type": "Hiking",
                    "distance": "16.69 km",
                    "elevation": "80 m",
                    "duration": "1h 23m",
                    "icon": "assets/icons/hiker.png",
                }
            ],
        }