class PrivacySetting:
    def __init__(self, group_id, visibility, require_post_approval):
        self.group_id = group_id
        self.visibility = visibility  # 'public' | 'private'
        self.require_post_approval = require_post_approval

    def update(self):
        print("[PrivacySetting] Updated privacy settings.")

    def setVisibility(self, visibility):
        self.visibility = visibility

    def enableApproval(self, require):
        self.require_post_approval = require

    def validateSettings(self):
        return self.visibility in ["public", "private"]

    def applyDefault(self):
        self.visibility = "public"
        self.require_post_approval = False

    def notifyMembers(self):
        print("[PrivacySetting] Members notified of changes.")

    def __str__(self):
        return f"Visibility: {self.visibility}, Post Approval: {self.require_post_approval}"
