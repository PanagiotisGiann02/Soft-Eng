# hiking_buddy/tests/test_record_activity.py

import pytest
from application.use_cases.start_activity import StartActivity
from application.use_cases.end_activity import EndActivity
from application.use_cases.pause_activity import PauseActivity
from application.use_cases.resume_activity import ResumeActivity
from core.repositories.activity_repository import InMemoryActivityRepository


@pytest.fixture
def activity_repo():
    return InMemoryActivityRepository()


@pytest.fixture
def start_uc(activity_repo):
    return StartActivity(activity_repo)


@pytest.fixture
def end_uc(activity_repo):
    return EndActivity(activity_repo)


@pytest.fixture
def pause_uc(activity_repo):
    return PauseActivity(activity_repo)


@pytest.fixture
def resume_uc(activity_repo):
    return ResumeActivity(activity_repo)


def test_start_activity_creates_in_progress(activity_repo, start_uc):
    activity = start_uc.execute(user_id=1, route_id=10)
    assert activity.id == 1
    assert activity.user_id == 1
    assert activity.route_id == 10
    assert activity.status == "in_progress"
    # Repository saved
    stored = activity_repo.get_by_id(activity.id)
    assert stored is activity


def test_end_activity_sets_statistics(activity_repo, start_uc, end_uc):
    # Start then end with sample stats
    activity = start_uc.execute(user_id=2, route_id=20)
    final_stats = {
        "duration_sec": 3600,
        "distance_meters": 10000,
        "elevation_gain_m": 200,
        "elevation_loss_m": 150,
        "average_speed_mps": 2.78,
        "calories_kcal": 500,
        "path_gpx_uri": "path/to/route.gpx",
    }
    ended = end_uc.execute(activity_id=activity.id, final_stats=final_stats)
    assert ended.status == "completed"
    assert ended.duration_sec == 3600
    assert ended.distance_meters == 10000
    assert ended.elevation_gain_m == 200
    assert ended.elevation_loss_m == 150
    assert ended.average_speed_mps == pytest.approx(2.78)
    assert ended.calories_kcal == 500
    assert ended.path_gpx_uri == "path/to/route.gpx"


def test_pause_and_resume_activity(activity_repo, start_uc, pause_uc, resume_uc):
    activity = start_uc.execute(user_id=3, route_id=30)
    paused = pause_uc.execute(activity_id=activity.id)
    assert paused.status == "paused"
    resumed = resume_uc.execute(activity_id=activity.id)
    assert resumed.status == "in_progress"


def test_end_activity_nonexistent(activity_repo, end_uc):
    with pytest.raises(ValueError):
        end_uc.execute(activity_id=999, final_stats={})
