import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

# Extends the base button class


class BaseButton(QPushButton):

    # Initialises some basic aspects of the buttons
    def __init__(self, text, color):
        super().__init__()

        # Sets the buttons text
        self.setText(text)

        # Sets the minimum button size
        self.setMinimumSize(200, 50)

        # Sets the color for the button
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: " + str(color))

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
        ascii_Button = BaseButton("ASCII Mapping", "green")
        edgeButton = BaseButton("Edge Mapping", "orange")
        button3 = BaseButton("3", "blue")
        exitButton = BaseButton("Exit", "red")

        # Add the button to the window
        layout.addWidget(ascii_Button)
        layout.addWidget(edgeButton)
        layout.addWidget(button3)
        layout.addWidget(exitButton)

        # Activates widgets and layout.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
