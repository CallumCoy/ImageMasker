import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from Widgets.Adjusted_Widgets import BasicButton

# Extends the main window


class MainWindow(QMainWindow):

    # Initialises
    def __init__(self):
        super().__init__()

        # Sets window name
        self.setWindowTitle("The Mapping App")

        # Sets the minimum size
        self.setMinimumSize(500, 300)

        # Sets the layout
        layout = QVBoxLayout()

        # Creates the button objects
        ascii_Button = BasicButton("ASCII Mapping", "green", width=200, height=50)
        edgeButton = BasicButton("Edge Mapping", "orange", width=200, height=50)
        button3 = BasicButton("3", "blue", width=200, height=50)
        exitButton = BasicButton("Exit", "red", width=200, height=50)

        # Add the button to the window
        layout.addWidget(ascii_Button)
        layout.addWidget(edgeButton)
        layout.addWidget(button3)
        layout.addWidget(exitButton)

        # Activates widgets and layout.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
