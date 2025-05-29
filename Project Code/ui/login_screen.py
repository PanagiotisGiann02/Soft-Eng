# LoginScreen UI and logic integration
# hiking_buddy/ui/login_screen.py
# Depends on: core/services/mock_auth_service.py

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QFrame,
    QMessageBox,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os
from core.services.mock_auth_service import MockAuthService
from application.use_cases.login_user import LoginUser


class LoginScreen(QWidget):
    def __init__(self, navigator):
        super().__init__()
        print("[LoginScreen] Initializing login screen")
        self.navigator = navigator
        self.auth = MockAuthService()
        self.setWindowTitle("Hiking Buddy - Login")
        self.setFixedSize(393, 852)
        self.setStyleSheet("background-color: white;")

        # Layouts
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Hiking Buddy Logo
        print("[LoginScreen] Loading logo")
        logo = QLabel()
        pixmap = QPixmap(os.path.join("assets", "logo.png"))
        pixmap = pixmap.scaled(
            250,
            150,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo)

        # Title
        print("[LoginScreen] Adding title label")
        title = QLabel("Sign in to Hiking buddy")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: 500; color: black;")
        layout.addWidget(title)

        # Username Field
        print("[LoginScreen] Creating username input field")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username or email")
        self.username_input.setStyleSheet(
            self.input_style() + "color: black; placeholder-text-color: #8C7E7E;"
        )
        layout.addWidget(self.username_input)

        # Password Field with Eye Icon
        print("[LoginScreen] Creating password input field")
        password_layout = QHBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet(
            self.input_style() + "color: black; placeholder-text-color: #8C7E7E;"
        )
        password_layout.addWidget(self.password_input)
        layout.addLayout(password_layout)

        # Sign In Button
        print("[LoginScreen] Creating sign in button")
        sign_in_btn = QPushButton("Sign In")
        sign_in_btn.setStyleSheet(
            "background-color: #4E9E3D; color: white; border-radius: 15px; font-size: 16px;"
        )
        sign_in_btn.setFixedSize(140, 45)
        sign_in_btn.clicked.connect(self.on_sign_in)
        layout.addWidget(sign_in_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        # Divider Line
        print("[LoginScreen] Adding divider line")
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)

        layout.addItem(
            QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
        )

        # Register Button at Bottom
        print("[LoginScreen] Creating register button")
        register_btn = QPushButton("Register")
        register_btn.setStyleSheet(
            "background-color: #679EC0; color: white; font-size: 14px; border-radius: 10px; border-width: 1px; border-color: #000; border-style: solid;"
        )
        register_btn.setFixedSize(298, 45)
        register_btn.clicked.connect(lambda: self.on_navigate_register())
        layout.addWidget(register_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        print("[LoginScreen] Login screen setup complete")

    def input_style(self):
        return (
            "padding: 10px; border: 1px solid #ccc; border-radius: 10px;"
            "background-color: #f5f5f5; font-size: 14px;"
        )

    def on_sign_in(self):
        print("[LoginScreen] Sign In button clicked")
        identifier = self.username_input.text()
        password = self.password_input.text()

        success, message = self.auth.execute(identifier, password)
        if success:
            QMessageBox.information(self, "Success", message)
            self.navigator.navigate_to("main")
        else:
            QMessageBox.warning(self, "Login Failed", message)

    def on_navigate_register(self):
        print("[LoginScreen] Register button clicked")
        self.navigator.navigate_to("register")
