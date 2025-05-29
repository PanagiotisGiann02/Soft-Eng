import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
from ui.login_screen import LoginScreen
from ui.register_screen import RegisterScreen
from ui.main_screen import MainScreen
from ui.profile_screen import ProfileScreen
from ui.maps_screen import MapsScreen
from ui.recording_screen import RecordingScreen
from ui.groups_screen import GroupsScreen
from core.navigation import AppNavigator


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Set global white background
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("white"))
    app.setPalette(palette)

    # Initialize navigator
    navigator = AppNavigator()

    # Screens
    login_screen = LoginScreen(navigator)
    register_screen = RegisterScreen(navigator)
    main_screen = MainScreen(navigator)
    profile_screen = ProfileScreen(navigator)
    maps_screen = MapsScreen(navigator)
    recording_screen = RecordingScreen(navigator)
    groups_screen = GroupsScreen(navigator)

    # Register screens
    navigator.add_screen("login", login_screen)
    navigator.add_screen("register", register_screen)
    navigator.add_screen("main", main_screen)
    navigator.add_screen("profile", profile_screen)
    navigator.add_screen("map", maps_screen)
    navigator.add_screen("record", recording_screen)
    navigator.add_screen("group", groups_screen)

    # Start at login
    navigator.navigate_to("group")

    # Setup window
    window = navigator.widget()
    window.setFixedSize(393, 852)
    window.setWindowTitle("Hiking Buddy")
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
