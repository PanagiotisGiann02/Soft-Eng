class Group:
    def __init__(self, id, name, description, logo_uri, visibility, created_by_user_id, created_at):
        self.id = id
        self.name = name
        self.description = description
        self.logo_uri = logo_uri
        self.visibility = visibility
        self.created_by_user_id = created_by_user_id
        self.created_at = created_at

    def addMember(self, user):
        print(f"[Group] Added {user.username} to group {self.name}.")

    def removeMember(self, user):
        print(f"[Group] Removed {user.username} from group {self.name}.")

    def postMessage(self, post):
        print(f"[Group] Post added by user {post.author_id}.")
