class TrashReport:
    def __init__(self, id, activityId, userId, latitude, longitude, severity, status):
        self.id = id
        self.activityId = activityId
        self.userId = userId
        self.latitude = latitude
        self.longitude = longitude
        self.severity = severity
        self.status = status

    def report(self):
        print("[TrashReport] Trash reported.")

    def updateStatus(self, status):
        self.status = status

    def collect(self):
        print("[TrashReport] Trash collected.")