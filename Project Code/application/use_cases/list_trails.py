# hiking_buddy/application/use_cases/list_trails.py


class ListTrails:
    def __init__(self, trail_service):
        self.trail_service = trail_service

    def execute(self):
        return self.trail_service.get_all_trails()
