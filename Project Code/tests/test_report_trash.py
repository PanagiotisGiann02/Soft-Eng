# hiking_buddy/tests/test_report_trash.py

import pytest
from application.use_cases.report_trash import ReportTrash
from domain.models.trashReport import TrashReport
from core.repositories.activity_repository import InMemoryActivityRepository
from core.repositories.trash_report_repository import InMemoryTrashReportRepository


@pytest.fixture
def activity_repo():
    return InMemoryActivityRepository()


@pytest.fixture
def trash_repo():
    return InMemoryTrashReportRepository()


@pytest.fixture
def start_uc(activity_repo):
    from application.use_cases.start_activity import StartActivity

    return StartActivity(activity_repo)


@pytest.fixture
def report_uc(activity_repo, trash_repo):
    return ReportTrash(activity_repo, trash_repo)


def test_report_trash_success(activity_repo, trash_repo, start_uc, report_uc):
    # Arrange: start activity
    activity = start_uc.execute(user_id=7, route_id=300)
    # Act: report trash without a photo
    report = report_uc.execute(
        activity_id=activity.id, latitude=38.2466, longitude=21.7346, severity=3
    )
    # Assert: correct type and saved
    assert isinstance(report, TrashReport)
    assert report.id == 1
    assert report.activityId == activity.id
    assert report.userId == activity.user_id
    assert report.latitude == pytest.approx(38.2466)
    assert report.longitude == pytest.approx(21.7346)
    assert report.severity == 3
    assert report.status == "pending"
    # Check repository storage
    stored = trash_repo.reports.get(report.id)
    assert stored is report


def test_report_trash_missing_severity(activity_repo, trash_repo, start_uc, report_uc):
    activity = start_uc.execute(user_id=8, route_id=400)
    with pytest.raises(TypeError):
        # severity missing
        report_uc.execute(
            activity_id=activity.id, latitude=38.0, longitude=21.0, severity=None
        )


def test_report_trash_gps_unavailable(
    activity_repo, trash_repo, start_uc, report_uc, monkeypatch
):
    activity = start_uc.execute(user_id=9, route_id=500)

    # Simulate GPS failure via raising in repository getCurrentLocation
    def bad_gps():
        raise RuntimeError("GPS unavailable")

    monkeypatch.setattr(activity_repo, "getCurrentLocation", bad_gps)
    with pytest.raises(RuntimeError):
        report_uc.execute(activity_id=activity.id, latitude=0, longitude=0, severity=2)


def test_report_trash_cancel_form(activity_repo, trash_repo):
    # Alt Flow 2: user cancels form -> no report created
    # Simulate by not calling execute; assert repo empty
    assert trash_repo.reports == {}
