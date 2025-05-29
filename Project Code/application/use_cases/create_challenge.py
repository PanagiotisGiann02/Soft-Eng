# hiking_buddy/application/use_cases/create_challenge.py

from domain.models.challenge import Challenge
from datetime import datetime
from domain.models.user import Administrator


class CreateChallenge:
    def __init__(self, challenge_repository):
        self.challenge_repository = challenge_repository

    def execute(
        self,
        creator,
        title,
        description,
        activity_type,
        category,
        requirements,
        start_at,
        end_at,
        visibility,
        gpx_uri,
        terms_pdf_uri,
    ):
        # Authorization
        if not isinstance(creator, Administrator):
            raise PermissionError("Only administrators can create challenges.")
        # Validate inputs
        if not title or title.strip() == "":
            raise ValueError("Missing title")
        if not gpx_uri.lower().endswith(".gpx"):
            raise ValueError("Invalid file format for GPX")
        if not terms_pdf_uri.lower().endswith(".pdf"):
            raise ValueError("Invalid file format for terms PDF")
        if start_at >= end_at:
            raise ValueError("Invalid date range")
        # Create Challenge object
        challenge_id = self.challenge_repository.get_next_id()
        challenge = Challenge(
            id=challenge_id,
            creator_admin_id=creator.id,
            title=title,
            description=description,
            activity_type=activity_type,
            category=category,
            requirements=requirements,
            start_at=start_at,
            end_at=end_at,
            visibility=visibility,
            gpx_uri=gpx_uri,
            terms_pdf_uri=terms_pdf_uri,
        )
        # Publish immediately
        challenge.publish()
        # Persist
        self.challenge_repository.save(challenge)
        return challenge
