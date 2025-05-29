# hiking_buddy/tests/test_send_sos.py

import pytest
from datetime import datetime
from application.use_cases.send_sos import SendSOS
from domain.models.sosAlert import SOSAlert
from core.repositories.activity_repository import InMemoryActivityRepository
from core.repositories.sos_alert_repository import InMemorySOSAlertRepository


@pytest.fixture
def activity_repo():
    return InMemoryActivityRepository()


@pytest.fixture
def sos_repo():
    return InMemorySOSAlertRepository()


@pytest.fixture
def start_uc(activity_repo):
    from application.use_cases.start_activity import StartActivity

    return StartActivity(activity_repo)


@pytest.fixture
def send_sos_uc(activity_repo, sos_repo):
    return SendSOS(activity_repo, sos_repo)


def test_send_sos_success(activity_repo, sos_repo, start_uc, send_sos_uc):
    # Arrange: start an activity
    activity = start_uc.execute(user_id=5, route_id=100)
    # Act: send SOS
    alert = send_sos_uc.execute(activity_id=activity.id)
    # Assert: alert saved in repository
    assert isinstance(alert, SOSAlert)
    assert alert.id == 1
    assert alert.user_id == activity.user_id
    assert alert.status == "open"
    # The repository should have stored the alert
    stored = sos_repo.alerts.get(alert.id)
    assert stored is alert


def test_send_sos_no_activity(activity_repo, sos_repo, send_sos_uc):
    # Act & Assert: non-existent activity raises error
    with pytest.raises(ValueError):
        send_sos_uc.execute(activity_id=999)


def test_send_sos_gps_failure(
    activity_repo, sos_repo, start_uc, send_sos_uc, monkeypatch
):
    # Arrange: start activity
    activity = start_uc.execute(user_id=6, route_id=200)

    # Monkeypatch getCurrentLocation to raise an exception
    def bad_gps():
        raise RuntimeError("GPS unavailable")

    monkeypatch.setattr(activity_repo, "getCurrentLocation", bad_gps)
    # Act & Assert: expect exception
    with pytest.raises(RuntimeError):
        send_sos_uc.execute(activity_id=activity.id)
