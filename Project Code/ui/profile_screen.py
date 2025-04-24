# Suggested path: hiking_buddy/ui/screens/profile_screen.py

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QPushButton,
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

from application.use_cases.get_profile_data import GetProfileData
from core.services.profile_service import ProfileService


class ProfileScreen(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.setFixedSize(393, 852)
        self.setStyleSheet("background-color: white;")

        self.profile_data = GetProfileData(ProfileService()).execute()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header
        header = QFrame()
        header.setFixedSize(393, 91)
        header.setStyleSheet(
            "background-color: white; border: 1px solid #BBB5B5; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.25);"
        )
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(15, 30, 15, 10)

        back_btn = QPushButton("<")
        back_btn.setFixedSize(25, 25)
        back_btn.clicked.connect(lambda: self.navigator.go_to("main"))
        back_btn.setStyleSheet("font-size: 18px; font-weight: bold; border: none;")

        title = QLabel("Home")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-family: Roboto; font-size: 16px; color: black;")

        settings_btn = QLabel()
        settings_btn.setPixmap(QPixmap("assets/icons/setting.png").scaled(25, 25))

        header_layout.addWidget(back_btn)
        header_layout.addStretch()
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(settings_btn)
        header.setLayout(header_layout)
        layout.addWidget(header)

        # User Info
        profile_frame = QFrame()
        profile_layout = QVBoxLayout(profile_frame)

        user_info = QHBoxLayout()
        profile_pic = QLabel()
        profile_pic.setPixmap(QPixmap("assets/icons/Capture_8.png").scaled(40, 40))
        user_info.addWidget(profile_pic)

        user_text = QVBoxLayout()
        username = QLabel(self.profile_data["username"])
        username.setStyleSheet(
            "font-size: 13px; font-weight: 700; font-family: Roboto;"
        )
        location = QLabel(self.profile_data["location"])
        location.setStyleSheet("font-size: 10px; font-family: Roboto;")
        user_text.addWidget(username)
        user_text.addWidget(location)
        user_info.addLayout(user_text)

        if self.profile_data["is_premium"]:
            premium_tag = QLabel("PREMIUM")
            premium_tag.setStyleSheet(
                "font-size: 9px; font-family: Roboto; color: #4E9E3D; border: 1px solid #4E9E3D; padding: 1px 4px;"
            )
            user_text.addWidget(premium_tag)

        profile_layout.addLayout(user_info)

        # Follower Info
        follow_layout = QHBoxLayout()
        following = QLabel(f"Following\n{self.profile_data['following']}")
        followers = QLabel(f"Followers\n{self.profile_data['followers']}")
        for label in (following, followers):
            label.setStyleSheet(
                "font-size: 10px; font-family: Roboto; text-align: center;"
            )
        follow_layout.addWidget(following)
        follow_layout.addWidget(followers)
        profile_layout.addLayout(follow_layout)

        # About section
        about_header = QLabel("About you")
        about_header.setStyleSheet(
            "font-size: 16px; font-weight: bold; font-family: Roboto;"
        )
        about_text = QLabel(self.profile_data["about"])
        about_text.setWordWrap(True)
        about_text.setStyleSheet("font-size: 11px; font-family: Roboto;")

        profile_layout.addWidget(about_header)
        profile_layout.addWidget(about_text)

        layout.addWidget(profile_frame)

        # Future: Add chart + trail card previews here
        # layout.addWidget(...)

        self.setLayout(layout)
