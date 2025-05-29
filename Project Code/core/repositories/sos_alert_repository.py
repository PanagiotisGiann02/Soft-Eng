# hiking_buddy/core/repositories/sos_alert_repository.py

from domain.models.sosAlert import SOSAlert


class SOSAlertRepository:
    def get_next_id(self) -> int:
        raise NotImplementedError

    def save(self, alert: SOSAlert) -> None:
        raise NotImplementedError


class InMemorySOSAlertRepository(SOSAlertRepository):
    def __init__(self):
        self.alerts = {}
        self.current_id = 1

    def get_next_id(self) -> int:
        next_id = self.current_id
        self.current_id += 1
        return next_id

    def save(self, alert: SOSAlert) -> None:
        self.alerts[alert.id] = alert
        print(f"[SOSAlertRepository] SOSAlert {alert.id} saved.")
