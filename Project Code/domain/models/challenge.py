# hiking_buddy/domain/models/challenge.py

from datetime import datetime


class Challenge:
    def __init__(
        self,
        id: int,
        creator_admin_id: int,
        title: str,
        description: str,
        activity_type: str,
        category: str,
        requirements: dict,
        start_at: datetime,
        end_at: datetime,
        visibility: str,
        gpx_uri: str,
        terms_pdf_uri: str,
    ):
        self.id = id
        self.creator_admin_id = creator_admin_id
        self.title = title
        self.description = description
        self.activity_type = activity_type  # 'hiking' | 'running' | 'cycling' | 'multi'
        self.category = category  # 'individual' | 'team' | 'open' | 'eco'
        self.requirements = requirements  # dict or Requirements instance
        self.start_at = start_at
        self.end_at = end_at
        self.visibility = visibility  # 'public' | 'private'
        self.gpx_uri = gpx_uri
        self.terms_pdf_uri = terms_pdf_uri
        self.status = "draft"
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.participant_count = 0
        self.completed_count = 0

    def publish(self):
        self.status = "published"
        self.updated_at = datetime.utcnow()
