class LoginUser:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def execute(self, identifier: str, password: str):
        if not identifier or not password:
            return False, "Please enter your login credentials."
        return self.auth_service.login(identifier, password)
