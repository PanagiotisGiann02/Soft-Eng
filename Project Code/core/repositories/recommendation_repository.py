# hiking_buddy/core/repositories/recommendation_repository.py

from domain.models.recommendationEngine import RecommendationEngine


class RecommendationRepository:
    def __init__(self, engine: RecommendationEngine):
        self.engine = engine

    def get_recommendations(self, user_id: int):
        return self.engine.getRecommendations(user_id)
