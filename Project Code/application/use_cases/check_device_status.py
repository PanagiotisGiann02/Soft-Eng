# hiking_buddy/application/use_cases/check_device_status.py

from core.repositories.device_status_repository import DeviceStatusRepository


class CheckDeviceStatus:
    def __init__(self, device_status_repo: DeviceStatusRepository):
        self.repo = device_status_repo

    def execute(self):
        battery = self.repo.check_battery()
        gps_on = self.repo.is_gps_enabled()
        print(f"[UseCase] Battery={battery}%, GPS enabled={gps_on}")
        return {"battery": battery, "gpsEnabled": gps_on}
