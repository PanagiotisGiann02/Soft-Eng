class Post:
    def __init__(
        self, id, group_id, author_id, text, media_uris, location, status, created_at
    ):
        self.id = id
        self.group_id = group_id
        self.author_id = author_id
        self.text = text
        self.media_uris = media_uris
        self.location = location
        self.status = status
        self.created_at = created_at

    def createPost(self):
        print("[Post] Post created.")

    def edit(self, content):
        self.text = content
        print("[Post] Post edited.")

    def delete(self):
        print("[Post] Post deleted.")

    def addComment(self, comment):
        print(f"[Post] Comment added by {comment.author_id}.")
