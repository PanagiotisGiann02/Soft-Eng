# hiking_buddy/application/use_cases/send_sos.py

from datetime import datetime
from domain.models.sosAlert import SOSAlert


class SendSOS:
    def __init__(self, activity_repository, sos_alert_repository):
        self.activity_repository = activity_repository
        self.sos_alert_repository = sos_alert_repository

    def execute(self, activity_id: int) -> SOSAlert:
        activity = self.activity_repository.get_by_id(activity_id)
        if not activity:
            raise ValueError("Activity not found")

        alert_id = self.sos_alert_repository.get_next_id()
        created_at = int(datetime.utcnow().timestamp())
        # Assuming activity has a last known location via repository
        location = self.activity_repository.getCurrentLocation()

        alert = SOSAlert(
            id=alert_id,
            user_id=activity.user_id,
            location={"lat": location.lat, "lng": location.lng},
            status="open",
            created_at=created_at,
            resolved_at=None,
        )
        self.sos_alert_repository.save(alert)

        activity.sendSOS(alert)
        self.activity_repository.save(activity)
        return alert
