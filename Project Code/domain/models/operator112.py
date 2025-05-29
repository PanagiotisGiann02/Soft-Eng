from user import User

class Operator112(User):
    def __init__(self, *args, operator_code: str, dispatch_center: str,
                 shift_start_at: int = None, shift_end_at: int = None,
                 certification: str = "multi", **kwargs):
        super().__init__(*args, **kwargs)
        self.operator_code = operator_code
        self.dispatch_center = dispatch_center
        self.shift_start_at = shift_start_at
        self.shift_end_at = shift_end_at
        self.certification = certification  # 'emt' | 'fire' | 'police' | 'multi'

    def handleSOS(self, alert):
        print(f"[112 Operator] Handling SOS alert from user {alert.user_id}.")
