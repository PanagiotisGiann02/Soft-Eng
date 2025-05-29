from user import User


class Administrator(User):
    def __init__(self, *args, permissions: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.permissions = permissions

    def createUser(self, user: User) -> User:
        print(f"[Admin] Created user {user.username}.")
        return user

    def deleteUser(self, userId: int):
        print(f"[Admin] Deleted user with ID {userId}.")

    def manageSettings(self):
        print("[Admin] Managing system settings.")
