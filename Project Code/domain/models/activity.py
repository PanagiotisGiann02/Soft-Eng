class Activity:
    def __init__(
        self,
        id,
        user_id,
        route_id,
        start_time,
        end_time,
        duration_sec,
        distance_meters,
        elevation_gain_m,
        elevation_loss_m,
        average_speed_mps,
        calories_kcal,
        path_gpx_uri,
        status,
    ):
        self.id = id
        self.user_id = user_id
        self.route_id = route_id
        self.start_time = start_time
        self.end_time = end_time
        self.duration_sec = duration_sec
        self.distance_meters = distance_meters
        self.elevation_gain_m = elevation_gain_m
        self.elevation_loss_m = elevation_loss_m
        self.average_speed_mps = average_speed_mps
        self.calories_kcal = calories_kcal
        self.path_gpx_uri = path_gpx_uri
        self.status = status

    def start(self):
        print("Activity started")

    def pause(self):
        print("Activity paused")

    def resume(self):
        print("Activity resumed")

    def end(self):
        print("Activity ended")

    def addPhoto(self, media):
        print("Photo added")

    def reportTrash(self, report):
        print("Trash reported")

    def sendSOS(self, alert):
        print("SOS sent")
