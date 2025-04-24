# mock_auth_service.py


class MockAuthService:
    def __init__(self):
        # Simulate user storage
        self.users = {
            "test@example.com": {
                "username": "testuser",
                "phone": "1234567890",
                "password": "password123",  # Insecure mock only!
            }
        }
        print("[MockAuthService] Initialized with 1 test user")

    def register(self, username, email, phone, password):
        print(f"[MockAuthService] Register attempt for: {email}")
        if email in self.users:
            print("[MockAuthService] Registration failed: User already exists")
            return False, "User already exists"

        self.users[email] = {"username": username, "phone": phone, "password": password}
        print("[MockAuthService] Registration successful")
        return True, "Registration successful"

    def login(self, email_or_username, password):
        print(f"[MockAuthService] Login attempt for: {email_or_username}")
        for email, data in self.users.items():
            if email_or_username in (email, data["username"]):
                if password == data["password"]:
                    print("[MockAuthService] Login successful")
                    return True, f"Welcome back {data['username']}"
                else:
                    print("[MockAuthService] Login failed: Incorrect password")
                    return False, "Incorrect password"

        print("[MockAuthService] Login failed: User not found")
        return False, "User not found"
