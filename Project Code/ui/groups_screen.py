# hiking_buddy/ui/screens/groups_screen.py

from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QScrollArea
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize


class GroupsScreen(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.setFixedSize(393, 852)
        self.setStyleSheet("background-color: white;")

        # Header
        header = QFrame(self)
        header.setGeometry(0, 0, 393, 91)
        header.setStyleSheet(
            "background-color: white; border-bottom: 1px solid #BBB5B5;"
        )

        # Search icon
        btn_search = QPushButton(header)
        btn_search.setIcon(QIcon("assets/icons/search.png"))
        btn_search.setIconSize(QSize(25, 25))
        btn_search.setGeometry(18, 55, 25, 25)
        btn_search.setStyleSheet("border:none;")

        # Title
        title = QLabel("Groups", header)
        title.setGeometry(155, 55, 83, 22)
        title.setStyleSheet(
            "color: black; font-family: Roboto; font-weight: 700; font-size: 20px; text-align:center; border:none;"
        )

        # Chat icon
        btn_chat = QPushButton(header)
        btn_chat.setIcon(QIcon("assets/icons/comment.png"))
        btn_chat.setIconSize(QSize(25, 25))
        btn_chat.setGeometry(309, 55, 25, 25)
        btn_chat.setStyleSheet("border:none;")

        # Settings icon
        btn_settings = QPushButton(header)
        btn_settings.setIcon(QIcon("assets/icons/setting.png"))
        btn_settings.setIconSize(QSize(25, 25))
        btn_settings.setGeometry(348, 55, 25, 25)
        btn_settings.setStyleSheet("border:none;")

        # Tabs bar
        tabs = QFrame(self)
        tabs.setGeometry(0, 91, 393, 40)
        tabs.setStyleSheet(
            "background-color: white; border-bottom: 1px solid #D9D9D9; border:none;"
        )

        lbl_active = QLabel("Active", tabs)
        lbl_active.setGeometry(18, 8, 50, 24)
        lbl_active.setStyleSheet(
            "color: black; font-family: Roboto; font-weight: 700; font-size: 14px; border:none;"
        )
        # active underline
        underline = QFrame(tabs)
        underline.setGeometry(18, 32, 50, 3)
        underline.setStyleSheet("background-color: #4E9E3D; border:none;")

        lbl_challenges = QLabel("Challenges", tabs)
        lbl_challenges.setGeometry(120, 8, 80, 24)
        lbl_challenges.setStyleSheet(
            "color: black; font-family: Roboto; font-weight: 400; font-size: 14px; color: #000000; border:none;"
        )

        lbl_clubs = QLabel("Clubs", tabs)
        lbl_clubs.setGeometry(268, 8, 50, 24)
        lbl_clubs.setStyleSheet(
            "color: black; font-family: Roboto; font-weight: 400; font-size: 14px; color: #000000; border:none;"
        )

        # Scroll area for active challenges
        scroll = QScrollArea(self)
        scroll.setGeometry(0, 131, 393, 580)
        scroll.setWidgetResizable(True)
        container = QWidget()
        scroll.setWidget(container)
        y = 0
        # Sample challenges
        challenges = [
            (
                "Personal Goal - 100k Cycling",
                "Complete 100k cycling within 1 week - Challenge by Test User",
                "March 9, 2025 to March 16, 2025",
            ),
            (
                "March Madness Hike",
                "Complete 100 hiking activities in March - Challenge by Admin User",
                "March 1, 2025 to March 31, 2025",
            ),
            (
                "Walk Madness",
                "Complete 100 walking activities in March - Challenge by Admin User",
                "March 1, 2025 to March 31, 2025",
            ),
        ]
        for title_text, desc, dates in challenges:
            card = QFrame(container)
            card.setGeometry(0, y, 393, 80)
            card.setStyleSheet(
                "background-color: white; border-bottom:1px solid #D9D9D9; border:none;"
            )
            icon = QLabel(card)
            icon.setPixmap(QIcon("assets/icons/challenge.png").pixmap(25, 25))
            icon.setGeometry(18, 12, 25, 25)
            lbl = QLabel(title_text, card)
            lbl.setGeometry(60, 8, 300, 20)
            lbl.setStyleSheet(
                "font-family: Roboto; font-weight: 700; font-size: 14px; border:none;"
            )
            desc_lbl = QLabel(desc, card)
            desc_lbl.setGeometry(60, 30, 320, 18)
            desc_lbl.setStyleSheet(
                "font-family: Roboto; font-weight: 400; font-size: 10px; color:#000000; border:none;"
            )
            date_lbl = QLabel(dates, card)
            date_lbl.setGeometry(60, 50, 320, 18)
            date_lbl.setStyleSheet(
                "font-family: Roboto; font-weight: 400; font-size: 9px; color: rgba(151,151,151,0.8); border:none;"
            )
            y += 80
        # 'See all' link
        see_all = QLabel("See all Active Challenges", container)
        see_all.setGeometry(260, y + 10, 130, 18)
        see_all.setStyleSheet(
            "font-family: Roboto; font-weight: 400; font-size: 10px; color: #4E9E3D; border:none;"
        )

        # Bottom image preview
        preview = QLabel(self)
        preview.setGeometry(0, 500, 600, 141)
        preview.setPixmap(
            QPixmap("assets/preview.png").scaled(
                393, 141, Qt.AspectRatioMode.IgnoreAspectRatio
            )
        )

        # 'Challenge' tag
        tag = QLabel("Challenge", preview)
        tag.setGeometry(15, 10, 70, 18)
        tag.setStyleSheet(
            "background-color: white; border-radius:4px; font-family: Roboto; font-size:10px; padding:2px;"
        )

        # Bottom navigation bar
        nav = QFrame(self)
        nav.setGeometry(0, 800, 393, 52)
        nav.setStyleSheet("background-color: white;")
        icons = ["home.png", "map.png", "record.png", "group.png", "stats.png"]
        for i, icon_file in enumerate(icons):
            btn = QPushButton(nav)
            btn.setIcon(QIcon(f"assets/icons/{icon_file}"))
            btn.setIconSize(QSize(30, 30))
            x = 20 + i * 75
            btn.setGeometry(x, 10, 30, 30)
            btn.setStyleSheet("border: none;")
            btn.clicked.connect(
                lambda _, idx=i: self.navigator.navigate_to(
                    ["main", "map", "record", "group", "stats"][idx]
                )
            )
