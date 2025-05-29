# hiking_buddy/application/use_cases/end_activity.py

from datetime import datetime


class EndActivity:
    def __init__(self, activity_repository):
        self.activity_repository = activity_repository

    def execute(self, activity_id: int, final_stats: dict):
        activity = self.activity_repository.get_by_id(activity_id)
        if not activity:
            raise ValueError("Activity not found")

        activity.end_time = int(datetime.utcnow().timestamp())
        activity.duration_sec = final_stats.get("duration_sec", 0)
        activity.distance_meters = final_stats.get("distance_meters", 0)
        activity.elevation_gain_m = final_stats.get("elevation_gain_m", 0)
        activity.elevation_loss_m = final_stats.get("elevation_loss_m", 0)
        activity.average_speed_mps = final_stats.get("average_speed_mps", 0)
        activity.calories_kcal = final_stats.get("calories_kcal", 0)
        activity.path_gpx_uri = final_stats.get("path_gpx_uri", "")
        activity.status = "completed"

        self.activity_repository.save(activity)
        return activity
