class SOSAlert:
    def __init__(self, id, user_id, location, status, created_at, resolved_at):
        self.id = id
        self.user_id = user_id
        self.location = location
        self.status = status
        self.created_at = created_at
        self.resolved_at = resolved_at

    def send(self):
        print("[SOSAlert] SOS sent.")

    def cancel(self):
        print("[SOSAlert] Cancelled.")

    def scheduleCountdown(self, duration):
        print(f"[SOSAlert] Countdown {duration}s")

    def notifyContacts(self):
        print("[SOSAlert] Contacts notified.")

    def logEvent(self):
        print("[SOSAlert] Logged.")

    def retrySend(self):
        return True

    def escalate(self, level):
        print(f"[SOSAlert] Escalated: {level}")

    def trackStatus(self):
        return self.status
