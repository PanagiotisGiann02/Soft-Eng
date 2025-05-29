# hiking_buddy/application/use_cases/start_activity.py

from domain.models.gpsData import GPSData
from domain.models.activity import Activity
from datetime import datetime


class StartActivity:
    def __init__(self, activity_repository):
        self.activity_repository = activity_repository

    def execute(self, user_id: int, route_id: int):
        print(f"[UseCase] Starting activity for user {user_id} on route {route_id}.")
        start_time = int(datetime.utcnow().timestamp())
        activity = Activity(
            id=self.activity_repository.get_next_id(),
            user_id=user_id,
            route_id=route_id,
            start_time=start_time,
            end_time=None,
            duration_sec=0,
            distance_meters=0,
            elevation_gain_m=0,
            elevation_loss_m=0,
            average_speed_mps=0,
            calories_kcal=0,
            path_gpx_uri="",
            status="in_progress",
        )
        self.activity_repository.save(activity)
        return activity
