# hiking_buddy/application/use_cases/join_challenge.py

from datetime import datetime
from domain.models.user import User


class JoinChallenge:
    def __init__(self, challenge_repository, participant_repository):
        self.challenge_repository = challenge_repository
        self.participant_repository = participant_repository

    def execute(self, user, challenge_id: int):
        # Authentication check
        if user is None or not isinstance(user, User):
            raise PermissionError("User must be logged in to join a challenge")

        # Retrieve challenge
        challenge = self.challenge_repository.get_by_id(challenge_id)
        if not challenge:
            raise ValueError("Challenge not found")

        # Check expiration
        now = datetime.utcnow()
        if now > challenge.end_at:
            raise ValueError("Challenge expired")

        # Check privacy
        if getattr(challenge, "visibility", None) == "private":
            raise PermissionError("Challenge is private, access request needed")

        # Check existing participation
        if self.participant_repository.is_participant(challenge_id, user.id):
            raise ValueError("Already joined")

        # (Optional) Validate prerequisites here if needed

        # Add participant
        self.participant_repository.add_participant(challenge_id, user.id)
        # Return updated participant list
        return self.participant_repository.list_participants(challenge_id)
