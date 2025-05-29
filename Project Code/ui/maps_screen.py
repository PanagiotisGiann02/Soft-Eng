# hiking_buddy/ui/screens/maps_screen.py

from PyQt6.QtWidgets import (
    QWidget,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize


class MapsScreen(QWidget):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        # Fixed screen size from Figma
        self.setFixedSize(393, 852)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header (status bar + app header)
        header = QFrame(self)
        header.setGeometry(0, 0, 393, 91)
        header.setStyleSheet("background-color: #A4D9F9;")
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(18, 30, 18, 10)

        # Back button on header
        back_btn = QPushButton(header)
        back_btn.setIcon(QIcon("assets/icons/left_arrow.png"))
        back_btn.setIconSize(QSize(25, 25))
        back_btn.setGeometry(15, 55, 25, 25)
        back_btn.setStyleSheet("border: none;")
        back_btn.clicked.connect(lambda: self.navigator.go_to("main"))
        header_layout.addWidget(back_btn)

        # Search bar
        search_frame = QFrame(self)
        search_frame.setGeometry(20, 55, 353, 40)
        search_frame.setStyleSheet(
            "background-color: white; border: 1px solid #D9D9D9; border-radius: 10px;"
        )
        # Icon in search
        search_icon = QLabel(search_frame)
        search_icon.setPixmap(
            QPixmap("assets/icons/shoe_icon.png").scaled(
                20, 20, Qt.AspectRatioMode.KeepAspectRatio
            )
        )
        search_icon.setGeometry(10, 10, 20, 20)
        search_icon.setStyleSheet("border: none;")
        # Input field
        search_input = QLineEdit(search_frame)
        search_input.setPlaceholderText("Search locations")
        search_input.setGeometry(40, 5, 300, 30)
        search_input.setStyleSheet("border: none; font-size: 14px; color: #999999;")
        header_layout.addWidget(search_input)

        # Scrollable main area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(10)

        # Map display placeholder
        map_label = QLabel(self)
        map_label.setGeometry(0, 91, 393, 559)
        map_label.setPixmap(
            QPixmap("assets/map_placeholder.png").scaled(
                393, 559, Qt.AspectRatioMode.IgnoreAspectRatio
            )
        )
        map_label.lower()  # send behind overlays

        # Bottom card
        card = QFrame(self)
        card.setGeometry(20, 600, 353, 140)
        card.setStyleSheet(
            "background-color: rgba(255,255,255,0.9); border-radius: 10px;"
        )
        # Trail image
        trail_img = QLabel(card)
        trail_img.setPixmap(
            QPixmap("assets/trail_preview.png").scaled(
                100, 80, Qt.AspectRatioMode.KeepAspectRatio
            )
        )
        trail_img.setGeometry(10, 10, 100, 80)
        # Trail info
        title = QLabel("Elos Aguias", card)
        title.setGeometry(120, 10, 200, 20)
        title.setStyleSheet("font-family: Roboto; font-size: 14px; font-weight: 700;")
        diff = QLabel("Easy", card)
        diff.setGeometry(120, 35, 40, 16)
        diff.setStyleSheet(
            "color: black; background-color: #C1F9A8; font-size: 10px; border-radius: 4px; text-align: center;"
        )
        # Metrics icons and text
        metrics = QLabel("6.75 km  16m  1h 21m", card)
        metrics.setGeometry(120, 55, 200, 16)
        metrics.setStyleSheet("font-size: 10px; color: #000000;")
        location = QLabel("Municipality of Patras, Peloponnese, Wes...", card)
        location.setGeometry(120, 75, 220, 16)
        location.setStyleSheet("font-size: 9px; color: #777777;")
        # Start button
        start_btn = QPushButton("START", card)
        start_btn.setGeometry(120, 100, 100, 30)
        start_btn.setStyleSheet(
            "background-color: #C1F9A8; color: black; border: none; border-radius: 5px;"
        )

        # Bottom navigation bar
        nav = QFrame(self)
        nav.setGeometry(0, 775, 393, 77)
        nav.setStyleSheet("background-color: white;")
        icons = [
            ("home.png", lambda: self.navigator.navigate_to("main")),
            ("map.png", lambda: self.navigator.navigate_to("map")),
            ("record.png", lambda: self.navigator.navigate_to("record")),
            ("group.png", lambda: self.navigator.navigate_to("group")),
            ("stats.png", lambda: self.navigator.navigate_to("stats")),
        ]
        i = 0
        for icon, callback in icons:
            btn = QPushButton(nav)
            btn.setIcon(QIcon(f"assets/icons/{icon}"))
            btn.setIconSize(QPixmap(f"assets/icons/{icon}").size())
            x = 20 + i * 75
            btn.setGeometry(x, 20, 30, 30)
            btn.setFlat(True)
            btn.clicked.connect(callback)
            btn.setStyleSheet("border: none;")
            i += 1

