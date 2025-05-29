class Comment:
    def __init__(self, id, post_id, author_id, text, created_at, edited_at, parent_comment_id, status):
        self.id = id
        self.post_id = post_id
        self.author_id = author_id
        self.text = text
        self.created_at = created_at
        self.edited_at = edited_at
        self.parent_comment_id = parent_comment_id
        self.status = status

    def create(self):
        print("[Comment] Created.")

    def edit(self, content):
        self.text = content
        print("[Comment] Edited.")

    def delete(self):
        print("[Comment] Deleted.")