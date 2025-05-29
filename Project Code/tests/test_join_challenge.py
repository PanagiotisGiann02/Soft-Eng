# hiking_buddy/tests/test_join_challenge.py

import pytest
from datetime import datetime, timedelta
from application.use_cases.join_challenge import JoinChallenge
from domain.models.user import User, Administrator
from domain.models.challenge import Challenge


class DummyChallengeRepo:
    def __init__(self):
        self.challenges = {}
        self._id = 1

    def get_next_id(self):
        nid = self._id
        self._id += 1
        return nid

    def save(self, challenge: Challenge):
        self.challenges[challenge.id] = challenge

    def get_by_id(self, challenge_id):
        return self.challenges.get(challenge_id)


class DummyParticipantRepo:
    def __init__(self):
        self.participants = {}  # key: challenge_id, value: set of user_ids

    def add_participant(self, challenge_id, user_id):
        self.participants.setdefault(challenge_id, set()).add(user_id)

    def is_participant(self, challenge_id, user_id):
        return user_id in self.participants.get(challenge_id, set())

    def list_participants(self, challenge_id):
        return list(self.participants.get(challenge_id, []))


@pytest.fixture
def challenge_repo():
    return DummyChallengeRepo()


@pytest.fixture
def participant_repo():
    return DummyParticipantRepo()


@pytest.fixture
def normal_user():
    return User(
        id=10,
        username="testuser",
        first_name="Test",
        last_name="User",
        email="test@example.com",
        phone_number="123",
        password_hash="pass",
    )


@pytest.fixture
def expired_challenge(challenge_repo):
    start = datetime.utcnow() - timedelta(days=10)
    end = datetime.utcnow() - timedelta(days=5)
    c = Challenge(
        id=challenge_repo.get_next_id(),
        creator_admin_id=1,
        title="Old",
        description="",
        activity_type="hiking",
        category="individual",
        requirements={},
        start_at=start,
        end_at=end,
        visibility="public",
        gpx_uri="a.gpx",
        terms_pdf_uri="a.pdf",
    )
    c.publish()
    challenge_repo.save(c)
    return c


@pytest.fixture
def active_challenge(challenge_repo):
    start = datetime.utcnow() - timedelta(days=1)
    end = datetime.utcnow() + timedelta(days=5)
    c = Challenge(
        id=challenge_repo.get_next_id(),
        creator_admin_id=1,
        title="Active",
        description="",
        activity_type="hiking",
        category="public",
        requirements={},
        start_at=start,
        end_at=end,
        visibility="public",
        gpx_uri="a.gpx",
        terms_pdf_uri="a.pdf",
    )
    c.publish()
    challenge_repo.save(c)
    return c


@pytest.fixture
def private_challenge(challenge_repo):
    start = datetime.utcnow() - timedelta(days=1)
    end = datetime.utcnow() + timedelta(days=5)
    c = Challenge(
        id=challenge_repo.get_next_id(),
        creator_admin_id=1,
        title="Private",
        description="",
        activity_type="hiking",
        category="individual",
        requirements={},
        start_at=start,
        end_at=end,
        visibility="private",
        gpx_uri="a.gpx",
        terms_pdf_uri="a.pdf",
    )
    c.publish()
    challenge_repo.save(c)
    return c


@pytest.fixture
def join_uc(challenge_repo, participant_repo):
    return JoinChallenge(challenge_repo, participant_repo)


def test_join_active_challenge(
    normal_user, active_challenge, join_uc, participant_repo
):
    participants = join_uc.execute(user=normal_user, challenge_id=active_challenge.id)
    assert normal_user.id in participants


def test_join_expired_challenge(normal_user, expired_challenge, join_uc):
    with pytest.raises(ValueError) as e:
        join_uc.execute(user=normal_user, challenge_id=expired_challenge.id)
    assert "expired" in str(e.value)


def test_join_private_challenge_shows_request(normal_user, private_challenge, join_uc):
    # Assuming private triggers some form request exception
    with pytest.raises(PermissionError):
        join_uc.execute(user=normal_user, challenge_id=private_challenge.id)


def test_join_when_not_logged_in(challenge_repo, participant_repo):
    # user=None simulates not logged in
    join_uc = JoinChallenge(challenge_repo, participant_repo)
    with pytest.raises(PermissionError):
        join_uc.execute(user=None, challenge_id=1)


def test_already_joined(normal_user, active_challenge, join_uc):
    # First join
    participants1 = join_uc.execute(user=normal_user, challenge_id=active_challenge.id)
    # Attempt second join
    with pytest.raises(ValueError) as e:
        join_uc.execute(user=normal_user, challenge_id=active_challenge.id)
    assert "Already joined" in str(e.value)


def test_cancel_before_join(normal_user, active_challenge, join_uc):
    # Simulate cancel by not calling execute: participants unchanged
    assert participant_repo.participants.get(active_challenge.id, []) == []
