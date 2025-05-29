class EmergencyMessage:
    def __init__(self, id, sos_id, sender, text):
        self.id = id
        self.sos_id = sos_id
        self.sender = sender
        self.text = text

    def sendMessage(self):
        print("[EmergencyMessage] Sent.")