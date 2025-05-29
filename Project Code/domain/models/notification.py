class Notification:
    def __init__(self, id, user_id, title, message, link_target, created_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.message = message
        self.link_target = link_target
        self.created_at = created_at

    def send(self):
        print("[Notification] Sent.")

    def markAsRead(self):
        print("[Notification] Marked as read.")
