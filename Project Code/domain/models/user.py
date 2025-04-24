class User:
    def __init__(self, username: str, email: str, phone: str, password: str):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, phone={self.phone})"

    def check_password(self, input_password: str) -> bool:
        return (
            self.password == input_password
        )  # mock, replace with hash check in production
