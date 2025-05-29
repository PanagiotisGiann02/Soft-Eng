from user import User


class GroupManager(User):
    def __init__(
        self, *args, managed_group_ids: list[str], moderation_score: int = 0, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.managed_group_ids = managed_group_ids
        self.moderation_score = moderation_score

    def assignManager(self, userId: int):
        print(f"[GroupManager] Assigned user {userId} as a manager.")
