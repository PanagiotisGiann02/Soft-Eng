# hiking_buddy/ui/screens/recording_screen.py

from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize, Qt


class RecordingScreen(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        # Full app dimensions from Figma
        self.setFixedSize(393, 852)
        self.setStyleSheet("background-color: white;")

        # Green header
        header = QFrame(self)
        header.setGeometry(0, 0, 393, 109)
        header.setStyleSheet("background-color: #4E9E3D;")

        # Live Tracking badge
        badge = QLabel(header)
        badge.setGeometry(15, 55, 100, 30)
        badge.setStyleSheet(
            "background-color: black; color: white; font-family: Roboto; font-size: 10px;"
            "border-radius: 5px; padding: 5px;"
        )
        badge.setText("\ue80d Live Tracking")  # Assuming icon font fallback
        badge.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter
        )

        # Map placeholder
        map_label = QLabel(self)
        map_label.setGeometry(0, 109, 393, 559)
        map_label.setPixmap(
            QPixmap("assets/map_placeholder.png").scaled(
                393, 559, Qt.AspectRatioMode.IgnoreAspectRatio
            )
        )

        # Control panel above start card
        control = QFrame(self)
        control.setGeometry(0, 668, 393, 85)
        control.setStyleSheet("background-color: #E8E8E8;")

        # Hiker icon
        icon = QLabel(control)
        icon.setPixmap(
            QPixmap("assets/icons/hiking.png").scaled(
                30, 30, Qt.AspectRatioMode.KeepAspectRatio
            )
        )
        icon.setGeometry(20, 10, 30, 30)

        # Activity label
        act_label = QLabel("Hiking", control)
        act_label.setGeometry(60, 10, 200, 30)
        act_label.setStyleSheet(
            "color: black; font-family: Roboto; font-size: 14px; font-weight: 400;"
        )

        # Down arrow icon
        arrow = QLabel(control)
        arrow.setPixmap(
            QPixmap("assets/icons/arrow_upload.png").scaled(
                20, 20, Qt.AspectRatioMode.KeepAspectRatio
            )
        )
        arrow.setGeometry(360, 15, 20, 20)
        arrow.setCursor(Qt.CursorShape.PointingHandCursor)
        arrow.mousePressEvent = lambda e: print("Expand activity list")

        # Start button
        start_btn = QPushButton("Start", self)
        start_btn.setGeometry(96, 755, 200, 45)
        start_btn.setStyleSheet(
            "background-color: #4E9E3D; color: white; font-family: Roboto; font-size: 16px;"
            "border-radius: 5px;"
        )
        start_btn.clicked.connect(lambda: print("Start pressed"))

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
