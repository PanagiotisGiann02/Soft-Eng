class RecommendationEngine:
    def __init__(self, id: str, model_version: str, active: bool, last_trained_at: int):
        self.id = id
        self.model_version = model_version
        self.active = active
        self.last_trained_at = last_trained_at

    def getRecommendations(self, userId: int):
        print(f"[RecommendationEngine] Generating recommendations for user {userId}.")
        return []

    def trainModel(self):
        print("[RecommendationEngine] Training model...")
