class Map:
    def __init__(
        self,
        id,
        name,
        center,
        zoom_level,
        show_routes,
        show_user_locations,
        show_trash_reports,
        show_sos_alerts,
        show_events,
        show_points_of_interest,
        selected_object_id,
        selected_object_type,
        last_refreshed_at,
    ):
        self.id = id
        self.name = name
        self.center = center  # dict with 'lat' and 'lng'
        self.zoom_level = zoom_level
        self.show_routes = show_routes
        self.show_user_locations = show_user_locations
        self.show_trash_reports = show_trash_reports
        self.show_sos_alerts = show_sos_alerts
        self.show_events = show_events
        self.show_points_of_interest = show_points_of_interest
        self.selected_object_id = selected_object_id
        self.selected_object_type = selected_object_type
        self.last_refreshed_at = last_refreshed_at

    def display(self):
        print("[Map] Display map.")

    def pan(self, dx, dy):
        print(f"[Map] Pan dx={dx}, dy={dy}")

    def zoom(self, level):
        self.zoom_level = level
        print(f"[Map] Zoom set to {level}")

    def toggleLayer(self, layerName):
        print(f"[Map] Toggled layer: {layerName}")
