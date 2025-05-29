# hiking_buddy/core/repositories/recording_settings_repository.py

from domain.models.recordingSettings import RecordingSettings


class RecordingSettingsRepository:
    def __init__(self, settings: RecordingSettings):
        self.settings = settings

    def update(self, new_settings: dict):
        self.settings.updateSettings(new_settings)
        print("[RecordingSettingsRepository] Settings persisted.")
