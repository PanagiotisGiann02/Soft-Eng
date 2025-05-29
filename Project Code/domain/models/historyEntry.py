class HistoryEntry:
    def __init__(self, id, userId, timestamp, action, metadata):
        self.id = id
        self.userId = userId
        self.timestamp = timestamp
        self.action = action
        self.metadata = metadata

    def record(self):
        print("[HistoryEntry] Recorded.")

    def undo(self):
        print("[HistoryEntry] Undo action.")

    def toJSON(self):
        return str(vars(self))

    def getSummary(self):
        return f"{self.timestamp}: {self.action}"

    def setTimestamp(self, ts):
        self.timestamp = ts
