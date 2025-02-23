import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from Windows.Ascii_Image_Generator import asciiWindowEditor
from Windows.Widgets.Adjusted_Widgets import BasicButton

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
        self.layout = QVBoxLayout()

        # Creates the button objects
        self.ascii_Button = BasicButton("ASCII Mapping", "green", width=200, height=50)
        self.edgeButton = BasicButton("Edge Mapping", "orange", width=200, height=50)
        self.button3 = BasicButton("3", "blue", width=200, height=50)
        self.exitButton = BasicButton("Exit", "red", width=200, height=50)

        # Add the button to the window
        self.layout.addWidget(self.ascii_Button)
        self.layout.addWidget(self.edgeButton)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.exitButton)

        # Activates widgets and layout.
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        self.ascii_Button.pressed.connect(self.openAsciiMapping)
        self.edgeButton.pressed.connect(self.openEdgeMapping)
        self.button3.pressed.connect(self.openOptionThree)
        self.exitButton.pressed.connect(self.closeButton)

    def openAsciiMapping(self):
        self.asciiWindow = asciiWindowEditor()
        self.asciiWindow.show()

        self.hide()
        self.asciiWindow.closed.connect(self.childClosed)
    
    def openEdgeMapping(self):
        print("Open edge mapping.")

    def openOptionThree(self):
        print("Open option 3, who know's what it will be")

    def childClosed(self):
        self.show()

    def closeButton(self):
        self.close()