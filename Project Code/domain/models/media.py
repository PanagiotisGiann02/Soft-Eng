class Media:
    def __init__(self, id, ownerId, type, url, createdAt):
        self.id = id
        self.ownerId = ownerId
        self.type = type
        self.url = url
        self.createdAt = createdAt

    def upload(self):
        print("[Media] Uploading media.")

    def delete(self):
        print("[Media] Deleting media.")