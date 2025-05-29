class RecordingSettings:
    def __init__(self, autoPause: bool, powerSaver: bool, envReportEnabled: bool):
        self.autoPause = autoPause
        self.powerSaver = powerSaver
        self.envReportEnabled = envReportEnabled

    def updateSettings(self, settings: dict):
        for key, value in settings.items():
            if hasattr(self, key):
                setattr(self, key, value)
        print("[RecordingSettings] Settings updated.")
