# Suggested path: hiking_buddy/ui/components/trail_card.py

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class TrailCard(QFrame):
    def __init__(
        self,
        user_name,
        date_text,
        location_text,
        trail_name,
        distance,
        elevation,
        duration,
        map_image_path,
        parent=None,
    ):
        super().__init__(parent)
        self.setStyleSheet("border: none; background-color: white;")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(8)

        # Top user row
        user_layout = QHBoxLayout()
        profile_pic = QLabel()
        profile_pic.setPixmap(QPixmap("assets/icons/profile_icon_large.png"))
        user_layout.addWidget(profile_pic)

        info_layout = QVBoxLayout()
        username = QLabel(user_name)
        username.setStyleSheet("font-family: Roboto; font-size: 10px; color: black;")
        info_layout.addWidget(username)

        shoes_layout = QHBoxLayout()
        shoes_icon = QLabel()
        shoes_icon.setPixmap(QPixmap("assets/icons/shoes.png"))
        shoes_layout.addWidget(shoes_icon)

        meta = QLabel(f"{date_text}, {location_text}")
        meta.setWordWrap(True)
        meta.setStyleSheet(
            "font-family: Roboto; font-size: 9px; color: rgba(151, 151, 151, 0.8);"
        )
        shoes_layout.addWidget(meta)
        shoes_layout.setSpacing(5)
        info_layout.addLayout(shoes_layout)
        user_layout.addLayout(info_layout)
        main_layout.addLayout(user_layout)

        # Trail title
        trail_title = QLabel(trail_name)
        trail_title.setStyleSheet(
            "font-family: Roboto; font-size: 14px; font-weight: bold; color: black;"
        )
        main_layout.addWidget(trail_title)

        # Trail metrics
        metrics_layout = QHBoxLayout()
        for label, value in [
            ("Distance", distance),
            ("Elev Gain", elevation),
            ("Time", duration),
        ]:
            box = QVBoxLayout()
            tag = QLabel(label)
            tag.setStyleSheet("font-size: 9px; color: rgba(151,151,151,0.8);")
            val = QLabel(value)
            val.setStyleSheet("font-size: 10px; font-weight: bold; color: black;")
            box.addWidget(tag)
            box.addWidget(val)
            metrics_layout.addLayout(box)
        main_layout.addLayout(metrics_layout)

        # Trail image with safe fallback
        trail_image = QLabel()
        trail_image.setMinimumHeight(150)
        trail_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(map_image_path)
        if not pixmap.isNull():
            trail_image.setPixmap(
                pixmap.scaledToWidth(370, Qt.TransformationMode.SmoothTransformation)
            )
        else:
            trail_image.setText("[Map image not found]")
            trail_image.setStyleSheet("font-size: 12px; color: gray;")
        main_layout.addWidget(trail_image)

        # Social actions
        action_layout = QHBoxLayout()
        for icon_name in ["like", "comment", "share"]:
            icon = QLabel()
            icon.setPixmap(
                QPixmap(f"assets/icons/{icon_name}.png").scaled(
                    30, 30, Qt.AspectRatioMode.KeepAspectRatio
                )
            )
            action_layout.addWidget(icon)
        main_layout.addLayout(action_layout)

        # Separator
        sep = QLabel()
        sep.setStyleSheet("background-color: #D9D9D9;")
        sep.setFixedHeight(9)
        main_layout.addWidget(sep)
