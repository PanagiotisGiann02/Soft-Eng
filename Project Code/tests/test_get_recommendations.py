# hiking_buddy/tests/test_get_recommendations.py

import pytest
from application.use_cases.get_recommendations import GetRecommendations


class DummyRecommendationRepo:
    def __init__(self, result=None, exception=None):
        self.result = result
        self.exception = exception

    def get_recommendations(self, user_id):
        if self.exception:
            raise self.exception
        return self.result


# Unit tests for GetRecommendations use case


def test_get_recommendations_success():
    """Διαθεσιμότητα internet: returns ≥3 recommendations."""
    repo = DummyRecommendationRepo(result=[1, 2, 3, 4])
    use_case = GetRecommendations(repo)
    recommendations = use_case.execute(user_id=42)
    assert isinstance(recommendations, list)
    assert len(recommendations) >= 3


def test_get_recommendations_empty_list():
    """Λήψη 0 προτάσεων: returns empty list."""
    repo = DummyRecommendationRepo(result=[])
    use_case = GetRecommendations(repo)
    recommendations = use_case.execute(user_id=42)
    assert recommendations == []


def test_get_recommendations_timeout():
    """API timeout: raises exception that should be handled upstream."""
    timeout_exc = TimeoutError("Request timed out")
    repo = DummyRecommendationRepo(exception=timeout_exc)
    use_case = GetRecommendations(repo)
    with pytest.raises(TimeoutError):
        use_case.execute(user_id=42)
