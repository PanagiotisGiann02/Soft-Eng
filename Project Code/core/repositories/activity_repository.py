# hiking_buddy/core/repositories/activity_repository.py

from domain.models.activity import Activity
from domain.models.gpsData import GPSData
from datetime import datetime

class ActivityRepository:
    def get_next_id(self) -> int:
        raise NotImplementedError

    def save(self, activity: Activity) -> None:
        raise NotImplementedError

    def get_by_id(self, activity_id: int) -> Activity:
        raise NotImplementedError


class InMemoryActivityRepository(ActivityRepository):
    def __init__(self):
        self.activities = {}
        self.current_id = 1

    def get_next_id(self) -> int:
        next_id = self.current_id
        self.current_id += 1
        return next_id

    def save(self, activity: Activity) -> None:
        self.activities[activity.id] = activity
        print(f"[Repository] Activity {activity.id} saved.")

    def get_by_id(self, activity_id: int) -> Activity:
        return self.activities.get(activity_id)

    def getCurrentLocation(self) -> GPSData:
        now = datetime.utcnow()
        return GPSData(
            id=0,
            activity_id=0,
            lat=38.2466,
            lng=21.7346,
            altitude_m=95.0,
            speed_mps=0.0,
            timestamp=now
        )
