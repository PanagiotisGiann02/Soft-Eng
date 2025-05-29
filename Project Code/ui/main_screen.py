from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFrame,
    QScrollArea,
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

from ui.components.trail_card import TrailCard
from application.use_cases.list_trails import ListTrails
from core.services.trail_service import TrailService


class MainScreen(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.setFixedSize(393, 852)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header
        header = QFrame()
        header.setFixedSize(393, 91)
        header.setStyleSheet("background-color: white;")
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(18, 30, 18, 10)

        profile_btn = QPushButton()
        profile_btn.setIcon(QIcon("assets/icons/profile_icon_small.png"))
        profile_btn.setIconSize(QPixmap("assets/icons/profile_icon_small.png").size())
        profile_btn.setFlat(True)
        profile_btn.clicked.connect(lambda: self.navigator.navigate_to("profile"))
        header_layout.addWidget(profile_btn)

        search_icon = QLabel()
        search_pixmap = QPixmap("assets/icons/search_icon.png")
        search_icon.setPixmap(search_pixmap)
        header_layout.addWidget(search_icon)

        title = QLabel("Home")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(
            "font-family: Roboto; font-weight: 700; font-size: 20px; color: #000000;"
        )
        header_layout.addWidget(title, stretch=1)

        speech_icon = QLabel()
        speech_pixmap = QPixmap("assets/icons/chat_icon.png")
        speech_icon.setPixmap(speech_pixmap)
        header_layout.addWidget(speech_icon)

        notif_icon = QLabel()
        notif_pixmap = QPixmap("assets/icons/bell_icon.png")
        notif_icon.setPixmap(notif_pixmap)
        header_layout.addWidget(notif_icon)

        header.setLayout(header_layout)
        layout.addWidget(header)

        # Scrollable main area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(10)

        # Goals Section
        goals_section = QFrame()
        goals_section.setStyleSheet("background-color: white;")
        goals_layout = QVBoxLayout(goals_section)
        goals_layout.setContentsMargins(15, 10, 15, 0)

        # Title and Add Button
        title_row = QHBoxLayout()
        goals_title = QLabel("Goals")
        goals_title.setStyleSheet(
            "font-family: Roboto; font-size: 11px; font-weight: 700; color: black;"
        )
        add_goal = QLabel("Add a Goal")
        add_goal.setStyleSheet(
            "font-family: Roboto; font-size: 11px; font-weight: 700; color: #1BA525;"
        )
        title_row.addWidget(goals_title)
        title_row.addStretch()
        title_row.addWidget(add_goal)
        goals_layout.addLayout(title_row)

        # Icon + Value Section
        goal_row = QHBoxLayout()
        box = QLabel()
        box.setFixedSize(51, 50)
        box.setStyleSheet("background-color: white; border: 2px solid black;")
        icon = QLabel()
        icon.setPixmap(QPixmap("assets/icons/Capture_9.png"))
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_container = QVBoxLayout()
        icon_container.addStretch()
        icon_container.addWidget(icon, alignment=Qt.AlignmentFlag.AlignCenter)
        icon_container.addStretch()
        box.setLayout(icon_container)

        goal_row.addStretch()
        goal_row.addWidget(box)

        goal_label = QVBoxLayout()
        count = QLabel("10")
        count.setStyleSheet(
            "font-size: 16px; font-weight: 700; font-family: Roboto; color: black;"
        )
        per_week = QLabel("10/week")
        per_week.setStyleSheet("font-size: 10px; font-family: Roboto; color: black;")
        goal_label.addWidget(count)
        goal_label.addWidget(per_week)

        goal_row.addLayout(goal_label)
        goal_row.addStretch()
        goals_layout.addLayout(goal_row)

        # Page dots
        dots = QHBoxLayout()
        dot1 = QLabel()
        dot1.setFixedSize(5, 5)
        dot1.setStyleSheet("background-color: black; border-radius: 3px;")
        dot2 = QLabel()
        dot2.setFixedSize(5, 5)
        dot2.setStyleSheet("background-color: #D2D1D1; border-radius: 3px;")
        dots.addStretch()
        dots.addWidget(dot1)
        dots.addSpacing(5)
        dots.addWidget(dot2)
        dots.addStretch()
        goals_layout.addLayout(dots)

        # Separator line
        line = QLabel()
        line.setFixedHeight(9)
        line.setStyleSheet("background-color: #D9D9D9;")
        goals_layout.addWidget(line)

        scroll_layout.addWidget(goals_section)

        trail_data = ListTrails(TrailService()).execute()
        for trail in trail_data:
            card = TrailCard(
                user_name=trail["user_name"],
                date_text=trail["date"],
                location_text=trail["location"],
                trail_name=trail["trail_name"],
                distance=trail["distance"],
                elevation=trail["elevation"],
                duration=trail["duration"],
                map_image_path=trail["map_image"],
            )
            scroll_layout.addWidget(card)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

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
