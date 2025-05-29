# hiking_buddy/application/use_cases/get_recommendations.py

from core.repositories.recommendation_repository import RecommendationRepository


class GetRecommendations:
    def __init__(self, recommendation_repository: RecommendationRepository):
        self.repo = recommendation_repository

    def execute(self, user_id: int):
        print(f"[UseCase] Fetching recommendations for user {user_id}")
        return self.repo.get_recommendations(user_id)
