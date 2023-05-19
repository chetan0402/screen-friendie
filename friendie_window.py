import sys
import os
import platformdirs

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QMovie, QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class TransparentMainWindow(QMainWindow):
    config_path = os.path.join(platformdirs.user_config_path(), "friendie_config.json")

    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.gif_label)

        self.movie = QMovie("gif_to_be_played.gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()

    def paintEvent(self, event):
        # Paint the background with a transparent color
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(0, 0, 0, 0))
        painter.drawRect(self.rect())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the application style to fusion for a consistent look
    app.setStyle("fusion")

    window = TransparentMainWindow()
    window.show()

    sys.exit(app.exec())
