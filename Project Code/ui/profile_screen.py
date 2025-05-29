# hiking_buddy/ui/screens/profile_screen.py

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
        header.setStyleSheet("background-color: white; border: 1px solid #BBB5B5;")
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(15, 30, 15, 10)

        back_btn = QPushButton("<")
        back_btn.setFixedSize(25, 25)
        back_btn.clicked.connect(lambda: self.navigator.navigate_to("main"))
        back_btn.setStyleSheet(
            "color: black; font-size: 18px; font-weight: bold; border: none;"
        )

        title = QLabel("Home")
        # title.setAlignment(Qt.AlignmentFlag)
        title.setStyleSheet(
            "font-family: Roboto; font-size: 16px; color: black; border: none;"
        )

        settings_btn = QLabel()
        settings_btn.setPixmap(QPixmap("assets/icons/setting.png").scaled(25, 25))
        settings_btn.setStyleSheet("border: none;")

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
        profile_pic.setPixmap(QPixmap("assets/profile_icon.png").scaled(40, 40))
        user_info.addWidget(profile_pic)

        user_text = QVBoxLayout()
        username = QLabel(self.profile_data["username"])
        username.setStyleSheet(
            "color: black; font-size: 13px; font-weight: 700; font-family: Roboto;"
        )
        location = QLabel(self.profile_data["location"])
        location.setStyleSheet("color: black; font-size: 10px; font-family: Roboto;")
        user_text.addWidget(username)
        user_text.addWidget(location)
        user_info.addLayout(user_text)

        if self.profile_data["is_premium"]:
            premium_tag = QLabel("PREMIUM")
            premium_tag.setStyleSheet(
                "color: black; font-size: 9px; font-family: Roboto; color: #4E9E3D; border: 1px solid #4E9E3D; padding: 1px 4px;"
            )
            user_text.addWidget(premium_tag)

        profile_layout.addLayout(user_info)

        # Follower Info
        follow_layout = QHBoxLayout()
        following = QLabel(f"Following\n{self.profile_data['following']}")
        followers = QLabel(f"Followers\n{self.profile_data['followers']}")
        for label in (following, followers):
            label.setStyleSheet(
                "color: black; font-size: 10px; font-family: Roboto; text-align: center;"
            )
        follow_layout.addWidget(following)
        follow_layout.addWidget(followers)
        profile_layout.addLayout(follow_layout)

        # About section
        about_header = QLabel("About you")
        about_header.setStyleSheet(
            "color: black; font-size: 16px; font-weight: bold; font-family: Roboto;"
        )
        about_text = QLabel(self.profile_data["about"])
        about_text.setWordWrap(True)
        about_text.setStyleSheet("color: black; font-size: 11px; font-family: Roboto;")

        profile_layout.addWidget(about_header)
        profile_layout.addWidget(about_text)

        # Chart image
        chart = QLabel()
        chart.setPixmap(
            QPixmap("assets/Capture_11.png").scaled(
                294, 196, Qt.AspectRatioMode.KeepAspectRatio
            )
        )
        chart.setAlignment(Qt.AlignmentFlag.AlignCenter)
        profile_layout.addWidget(chart)

        # Section title row
        section_row = QHBoxLayout()
        section_row.addWidget(QLabel("Your Trails (25)"))
        section_row.addStretch()
        section_row.addWidget(QLabel("Lists (4)"))
        section_row.addStretch()
        section_row.addWidget(QLabel("Planned trails (0)"))
        profile_layout.addLayout(section_row)

        # Trail summary card
        trail = self.profile_data["trails"][0]
        trail_title = QLabel(trail["title"])
        trail_title.setStyleSheet(
            "color: black; font-size: 14px; font-weight: bold; font-family: Roboto;"
        )
        trail_type = QLabel(trail["type"])
        trail_type.setStyleSheet("color: black; font-size: 12px; font-family: Roboto;")

        metrics_layout = QHBoxLayout()
        for label, val in [
            ("Distance", trail["distance"]),
            ("Elev Gain", trail["elevation"]),
            ("Time", trail["duration"]),
        ]:
            column = QVBoxLayout()
            column.addWidget(QLabel(label))
            value = QLabel(val)
            value.setStyleSheet("color: black; font-weight: bold; font-size: 14px;")
            column.addWidget(value)
            metrics_layout.addLayout(column)

        profile_layout.addWidget(trail_title)
        profile_layout.addWidget(trail_type)
        profile_layout.addLayout(metrics_layout)

        layout.addWidget(profile_frame)
        self.setLayout(layout)

        # Bottom Nav Bar
        nav_bar = QFrame()
        nav_bar.setFixedSize(393, 77)
        nav_bar.setStyleSheet("background-color: white;")
        nav_layout = QHBoxLayout()

        icons = [
            ("home", lambda: self.navigator.navigate_to("main")),
            ("map", lambda: self.navigator.navigate_to("map")),
            ("record", lambda: self.navigator.navigate_to("record")),
            ("group", lambda: self.navigator.navigate_to("group")),
            ("stats", lambda: self.navigator.navigate_to("stats")),
        ]

        for icon_name, callback in icons:
            btn = QPushButton()
            btn.setIcon(QIcon(f"assets/icons/{icon_name}.png"))
            btn.setIconSize(QPixmap(f"assets/icons/{icon_name}.png").size())
            btn.setFlat(True)
            btn.clicked.connect(callback)
            nav_layout.addWidget(btn)

        nav_bar.setLayout(nav_layout)
        layout.addWidget(nav_bar)
