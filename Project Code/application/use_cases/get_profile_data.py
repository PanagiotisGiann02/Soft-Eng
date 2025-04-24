# Suggested path: hiking_buddy/application/use_cases/get_profile_data.py

class GetProfileData:
    def __init__(self, profile_service):
        self.profile_service = profile_service

    def execute(self):
        return self.profile_service.get_profile_data()
