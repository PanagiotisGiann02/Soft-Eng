from PyQt6.QtWidgets import QStackedWidget


class AppNavigator:
    def __init__(self):
        self.stack = QStackedWidget()
        self.routes = {}

    def add_screen(self, name: str, widget):
        self.routes[name] = widget
        self.stack.addWidget(widget)

    def navigate_to(self, name: str):
        if name in self.routes:
            self.stack.setCurrentWidget(self.routes[name])

    def widget(self):
        return self.stack
