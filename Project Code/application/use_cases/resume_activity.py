# hiking_buddy/application/use_cases/resume_activity.py

from domain.models.activity import Activity


class ResumeActivity:
    def __init__(self, activity_repository):
        self.activity_repository = activity_repository

    def execute(self, activity_id: int) -> Activity:
        activity = self.activity_repository.get_by_id(activity_id)
        if not activity:
            raise ValueError("Activity not found")
        activity.status = "in_progress"
        activity.resume()
        self.activity_repository.save(activity)
        return activity
