import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
from ui.login_screen import LoginScreen
from ui.register_screen import RegisterScreen
from ui.main_screen import MainScreen
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

    # Register screens
    navigator.add_screen("login", login_screen)
    navigator.add_screen("register", register_screen)
    navigator.add_screen("main", main_screen)

    # Start at login
    navigator.navigate_to("main")

    # Setup window
    window = navigator.widget()
    window.setFixedSize(393, 852)
    window.setWindowTitle("Hiking Buddy")
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
