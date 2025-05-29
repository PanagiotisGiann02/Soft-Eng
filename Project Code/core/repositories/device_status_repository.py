# hiking_buddy/core/repositories/device_status_repository.py

from domain.models.deviceStatus import DeviceStatus


class DeviceStatusRepository:
    def __init__(self, device_status: DeviceStatus):
        self.device_status = device_status

    def check_battery(self) -> int:
        return self.device_status.checkBattery()

    def is_gps_enabled(self) -> bool:
        return self.device_status.isGPSEnabled()
