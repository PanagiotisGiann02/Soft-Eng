# hiking_buddy/application/use_cases/report_trash.py

from datetime import datetime
from domain.models.trashReport import TrashReport


class ReportTrash:
    def __init__(self, activity_repository, trash_report_repository):
        self.activity_repository = activity_repository
        self.trash_report_repository = trash_report_repository

    def execute(
        self, activity_id: int, latitude: float, longitude: float, severity: int
    ) -> TrashReport:
        activity = self.activity_repository.get_by_id(activity_id)
        if not activity:
            raise ValueError("Activity not found")

        report_id = self.trash_report_repository.get_next_id()
        report = TrashReport(
            id=report_id,
            activityId=activity_id,
            userId=activity.user_id,
            latitude=latitude,
            longitude=longitude,
            severity=severity,
            status="pending",
        )
        self.trash_report_repository.save(report)

        activity.reportTrash(report)
        self.activity_repository.save(activity)
        return report
