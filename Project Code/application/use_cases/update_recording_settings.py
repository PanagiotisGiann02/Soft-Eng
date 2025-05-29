# hiking_buddy/application/use_cases/update_recording_settings.py

from core.repositories.recording_settings_repository import RecordingSettingsRepository


class UpdateRecordingSettings:
    def __init__(self, settings_repo: RecordingSettingsRepository):
        self.repo = settings_repo

    def execute(self, settings_dict: dict):
        print(f"[UseCase] Updating recording settings: {settings_dict}")
        self.repo.update(settings_dict)
        return self.repo.settings
