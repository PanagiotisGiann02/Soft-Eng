from domain.models.user import User

class RegisterUser:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def execute(self, username: str, email: str, phone: str, password: str, repeat_password: str, terms_accepted: bool):
        if not all([username, email, phone, password, repeat_password]):
            return False, "Please fill in all fields."
        if password != repeat_password:
            return False, "Passwords do not match."
        if not terms_accepted:
            return False, "You must accept the terms and privacy policy."

        user = User(username, email, phone, password)
        return self.auth_service.register(user.username, user.email, user.phone, user.password)
