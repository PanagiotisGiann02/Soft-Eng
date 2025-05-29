class User:
    def __init__(
        self,
        id: int,
        username: str,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        password_hash: str
    ):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password_hash = password_hash

    def login(self, password: str) -> bool:
        # For now, simple comparison; use hash verification in production
        return password == self.password_hash

    def logout(self) -> None:
        print(f"[User] {self.username} logged out.")

    def updateProfile(self, data: dict) -> None:
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def joinGroup(self, groupId: int) -> None:
        print(f"[User] {self.username} joined group {groupId}.")

    def joinChallenge(self, challengeId: int) -> None:
        print(f"[User] {self.username} joined challenge {challengeId}.")

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"
