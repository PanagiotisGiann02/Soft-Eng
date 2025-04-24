from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QSpacerItem,
    QSizePolicy,
    QFrame,
    QMessageBox,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from core.services.mock_auth_service import MockAuthService


class RegisterScreen(QWidget):
    def __init__(self, navigator):
        super().__init__()
        print("[RegisterScreen] Initializing Register Screen")
        self.navigator = navigator
        self.auth = MockAuthService()
        self.setFixedSize(393, 852)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 30)
        layout.setSpacing(15)

        # Header with back button
        print("[RegisterScreen] Creating header")
        header = QFrame()
        header.setStyleSheet("background-color: #4E9E3D;")
        header.setFixedSize(393, 109)
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(20, 40, 20, 0)
        header_layout.setSpacing(10)

        # Back button
        back_button = QPushButton()
        back_button.setIcon(QIcon("assets/icons/back_arrow.png"))
        back_button.setFlat(True)
        back_button.setStyleSheet("color: white;")
        back_button.setFixedSize(30, 30)
        back_button.clicked.connect(self.on_back_pressed)
        header_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Title in center
        title = QLabel("Sign Up")
        title.setStyleSheet("color: white; font-size: 22px; font-weight: bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(title, stretch=1)

        # Placeholder for spacing on the right
        placeholder = QLabel()
        placeholder.setFixedSize(30, 30)
        header_layout.addWidget(placeholder)

        header.setLayout(header_layout)
        layout.addWidget(header)

        # Fields
        print("[RegisterScreen] Creating input fields")
        self.username_input = self.create_input("Enter your username")
        self.username_input.setFixedSize(295, 46)
        layout.addWidget(self.username_input, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.email_input = self.create_input("Enter your email")
        self.email_input.setFixedSize(295, 46)
        layout.addWidget(self.email_input, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.phone_input = self.create_input("Enter your phone")
        self.phone_input.setFixedSize(295, 46)
        layout.addWidget(self.phone_input, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Password Field
        print("[RegisterScreen] Creating password input")
        password_layout = QHBoxLayout()
        self.password_input = self.create_input("Password", echo=True)
        self.password_input.setFixedSize(295, 46)
        password_layout.addWidget(self.password_input)
        layout.addLayout(password_layout)

        password_hint = QLabel(
            "Include a minimum of 8 characters with letters\nand at least one number"
        )
        password_hint.setStyleSheet(
            "color: #8C7E7E; font-size: 12px; font-family: Roboto; font-weight: 700; line-height: 100%; letter-spacing: 0%;"
        )
        password_hint.setFixedSize(292, 36)
        layout.addWidget(password_hint, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Repeat Password
        print("[RegisterScreen] Creating repeat password input")
        repeat_layout = QHBoxLayout()
        self.repeat_input = self.create_input("Repeat Password", echo=True)
        self.repeat_input.setFixedSize(295, 46)
        repeat_layout.addWidget(self.repeat_input)
        layout.addLayout(repeat_layout)

        # Terms agreement
        print("[RegisterScreen] Creating terms agreement")
        terms_container = QHBoxLayout()
        terms_widget = QWidget()
        terms_layout = QHBoxLayout()
        terms_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.terms_checkbox = QCheckBox()
        terms_label = QLabel(
            "I agree with Hiking Buddy Terms of Service and Privacy Policy"
        )
        terms_label.setWordWrap(True)
        terms_label.setFixedSize(204, 26)
        terms_label.setStyleSheet(
            "font-family: Roboto; font-weight: 400; font-size: 10px; line-height: 100%; letter-spacing: 0%; text-align: center; color: #000"
        )
        terms_layout.addWidget(self.terms_checkbox)
        terms_layout.addWidget(terms_label)
        terms_widget.setLayout(terms_layout)
        terms_container.addWidget(terms_widget, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(terms_container)

        layout.addItem(
            QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
        )

        # Create Account button
        print("[RegisterScreen] Creating 'Create an account' button")
        create_btn = QPushButton("Create an account")
        create_btn.setStyleSheet(
            "background-color: #679EC0; color: white; font-size: 14px; border-radius: 10px; border-width: 1px; border-color: #000; border-style: solid;"
        )
        create_btn.setFixedSize(298, 45)
        create_btn.clicked.connect(self.on_create_account)
        layout.addWidget(create_btn, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)
        print("[RegisterScreen] Register screen setup complete")

    def create_input(self, placeholder: str, echo=False):
        print(f"[RegisterScreen] Creating input field: '{placeholder}'")
        field = QLineEdit()
        field.setPlaceholderText(placeholder)
        field.setStyleSheet(
            "padding: 10px; border: 1px solid #ccc; border-radius: 10px; background-color: #f5f5f5; font-size: 14px; color: black; placeholder-text-color: #8C7E7E; opacity: 0.4;"
        )
        if echo:
            field.setEchoMode(QLineEdit.EchoMode.Password)
        return field

    def toggle_echo(self, field):
        current_mode = (
            "Password" if field.echoMode() == QLineEdit.EchoMode.Password else "Normal"
        )
        print(
            f"[RegisterScreen] Toggling password visibility. Current mode: {current_mode}"
        )
        if field.echoMode() == QLineEdit.EchoMode.Password:
            field.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            field.setEchoMode(QLineEdit.EchoMode.Password)

    def on_create_account(self):
        print("[RegisterScreen] 'Create an account' button clicked")
        username = self.username_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        password = self.password_input.text()
        repeat = self.repeat_input.text()
        terms_accepted = self.terms_checkbox.isChecked()

        if not all([username, email, phone, password, repeat]):
            QMessageBox.warning(self, "Missing Fields", "Please fill in all fields.")
            return

        if password != repeat:
            QMessageBox.warning(self, "Mismatch", "Passwords do not match.")
            return

        if not terms_accepted:
            QMessageBox.warning(
                self, "Terms", "You must accept the terms and privacy policy."
            )
            return

        success, message = self.auth.register(username, email, phone, password)
        if success:
            QMessageBox.information(self, "Success", message)
            self.navigator.navigate_to("login")
        else:
            QMessageBox.warning(self, "Registration Failed", message)

    def on_back_pressed(self):
        print("[RegisterScreen] Back button clicked")
        self.navigator.navigate_to("login")
