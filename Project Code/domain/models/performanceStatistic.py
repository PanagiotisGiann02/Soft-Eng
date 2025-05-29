class PerformanceStatistic:
    def __init__(
        self,
        id,
        userId,
        activityType,
        totalDistance,
        totalTime,
        averagePace,
        maxPace,
        caloriesBurned,
        elevationGain,
    ):
        self.id = id
        self.userId = userId
        self.activityType = activityType
        self.totalDistance = totalDistance
        self.totalTime = totalTime
        self.averagePace = averagePace
        self.maxPace = maxPace
        self.caloriesBurned = caloriesBurned
        self.elevationGain = elevationGain

    def calculate(self):
        print("Calculating stats")

    def calculateAveragePace(self):
        return self.totalTime / self.totalDistance

    def calculateMaxPace(self):
        return self.maxPace

    def calculateCalories(self, weight, duration):
        return weight * duration * 0.0175 * 3.5

    def summarizeStats(self):
        return vars(self)

    def reset(self):
        self.totalDistance = self.totalTime = 0
