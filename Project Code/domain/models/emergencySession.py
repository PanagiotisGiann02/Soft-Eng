class EmergencySession:
    def __init__(self, id, sos_id, sender, ended_at, state):
        self.id = id
        self.sos_id = sos_id
        self.sender = sender
        self.ended_at = ended_at
        self.state = state

    def startSession(self):
        print("[EmergencySession] Started.")

    def endSession(self):
        print("[EmergencySession] Ended.")
