# hiking_buddy/tests/test_create_challenge.py

import pytest
from datetime import datetime, timedelta

from domain.models.user import User
from domain.models.administrator import Administrator
from domain.models.challenge import Challenge
from application.use_cases.create_challenge import CreateChallenge


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

    def list_all(self):
        return list(self.challenges.values())


@pytest.fixture
def challenge_repo():
    return DummyChallengeRepo()


@pytest.fixture
def admin_user():
    return Administrator(
        id=1,
        username="admin",
        first_name="Admin",
        last_name="User",
        email="admin@example.com",
        phone_number="000",
        password_hash="pass",
        permissions="all",
    )


@pytest.fixture
def normal_user():
    return User(
        id=2,
        username="user",
        first_name="Normal",
        last_name="User",
        email="user@example.com",
        phone_number="111",
        password_hash="pass",
    )


@pytest.fixture
def create_challenge_uc(challenge_repo):
    return CreateChallenge(challenge_repo)


def test_admin_can_create_challenge(admin_user, create_challenge_uc, challenge_repo):
    start = datetime.utcnow()
    end = start + timedelta(days=7)
    challenge = create_challenge_uc.execute(
        creator=admin_user,
        title="Test Challenge",
        description="Desc",
        activity_type="hiking",
        category="individual",
        requirements={},
        start_at=start,
        end_at=end,
        visibility="public",
        gpx_uri="path/to/file.gpx",
        terms_pdf_uri="path/to/terms.pdf",
    )
    assert isinstance(challenge, Challenge)
    assert challenge.id == 1
    assert challenge.title == "Test Challenge"
    assert challenge.start_at == start
    assert challenge.end_at == end
    assert (challenge_gpx := challenge.gpx_uri.endswith(".gpx"))
    assert (challenge_pdf := challenge.terms_pdf_uri.endswith(".pdf"))
    assert len(challenge_repo.list_all()) == 1


def test_non_admin_cannot_create_challenge(normal_user, create_challenge_uc):
    with pytest.raises(PermissionError):
        create_challenge_uc.execute(
            creator=normal_user,
            title="X",
            description="",
            activity_type="hiking",
            category="individual",
            requirements={},
            start_at=datetime.utcnow(),
            end_at=datetime.utcnow(),
            visibility="public",
            gpx_uri="a.gpx",
            terms_pdf_uri="a.pdf",
        )


def test_invalid_gpx_format(admin_user, create_challenge_uc):
    with pytest.raises(ValueError):
        create_challenge_uc.execute(
            creator=admin_user,
            title="C",
            description="D",
            activity_type="hiking",
            category="individual",
            requirements={},
            start_at=datetime.utcnow(),
            end_at=datetime.utcnow() + timedelta(days=1),
            visibility="public",
            gpx_uri="file.txt",
            terms_pdf_uri="terms.pdf",
        )


def test_missing_title(admin_user, create_challenge_uc):
    with pytest.raises(ValueError):
        create_challenge_uc.execute(
            creator=admin_user,
            title="",
            description="Desc",
            activity_type="hiking",
            category="individual",
            requirements={},
            start_at=datetime.utcnow(),
            end_at=datetime.utcnow() + timedelta(days=1),
            visibility="public",
            gpx_uri="file.gpx",
            terms_pdf_uri="terms.pdf",
        )


def test_invalid_date_range(admin_user, create_challenge_uc):
    start = datetime.utcnow()
    end = start - timedelta(days=1)
    with pytest.raises(ValueError):
        create_challenge_uc.execute(
            creator=admin_user,
            title="DateTest",
            description="",
            activity_type="hiking",
            category="individual",
            requirements={},
            start_at=start,
            end_at=end,
            visibility="public",
            gpx_uri="file.gpx",
            terms_pdf_uri="terms.pdf",
        )
