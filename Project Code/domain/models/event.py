class Event:
    def __init__(self, id, group_id, title, start_at, end_at, location, capacity):
        self.id = id
        self.group_id = group_id
        self.title = title
        self.start_at = start_at
        self.end_at = end_at
        self.location = location
        self.capacity = capacity

    def createEvent(self):
        print("[Event] Created.")

    def cancelEvent(self):
        print("[Event] Cancelled.")

    def registerParticipant(self, user):
        print(f"[Event] {user.username} registered for {self.title}.")
