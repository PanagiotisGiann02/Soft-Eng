class DeviceStatus:
    def __init__(self, batteryLevel: int, gpsEnabled: bool):
        self.batteryLevel = batteryLevel
        self.gpsEnabled = gpsEnabled

    def checkBattery(self) -> int:
        return self.batteryLevel

    def isGPSEnabled(self) -> bool:
        return self.gpsEnabled
