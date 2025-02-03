import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QColor, QPalette


class leftMenuWidget(QLabel):

    BASE_WIDTH = 300
    BASE_HEIGHT = 200
    COLOR = "grey"

    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            background-color: #262626;
            color: #FFFFFF;
            font-family: Titillium;
            font-size: 18px;
        """)

        self.setAutoFillBackground(True)
        self.show()


class InnerWidget(QLabel):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            background-color: #260000;
            color: #FF0000;
            font-family: Titillium;
            font-size: 18px;
        """)

        self.setAutoFillBackground(True)
        self.show()


class LeftWindow(InnerWidget):

    def __init__(self):
        super().__init__()

        # Setting up the background
        self.setStyleSheet("""
            background-color: #262626;
            color: #FFFFFF;
            font-family: Titillium;
            font-size: 18px;
        """)

        self.setAutoFillBackground(True)
        self.show()

        # Creating the widgets
        browseBar = BrowseBar()
        Options = InnerWidget()

        # Setting up the layout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(browseBar, 1)
        leftLayout.addWidget(Options, 6)
        self.setLayout(leftLayout)

class BrowseBar(InnerWidget):
    def __init__(self):
        super().__init__()

        searchBar = QLineEdit()
        browseButton = QPushButton()
        browseButton.setText("Browse")

        fileBrowserLayout = QHBoxLayout()
        fileBrowserLayout.addWidget(searchBar)
        fileBrowserLayout.addWidget(browseButton)
        self.setLayout(fileBrowserLayout)


class RightWindow(InnerWidget):

    def __init__(self):
        super().__init__()

        # Setting up the background
        self.setStyleSheet("""
            background-color: #262626;
            color: #FFFFFF;
            font-family: Titillium;
            font-size: 18px;
        """)

        self.setAutoFillBackground(True)
        self.show()

        # Creating Widgets
        imageDisplay = InnerWidget()
        otherPrograms = InnerWidget()

        # Setting up the layout for the right window
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(imageDisplay, 8)
        rightLayout.addWidget(otherPrograms, 1)
        self.setLayout(rightLayout)

# Extends the base button class


class EditorButton(QPushButton):

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
        self.setGeometry(100, 100, 1200, 800)

        # Sets left right window layout
        overallLayout = QHBoxLayout()

        leftWindow = LeftWindow()
        rightWindow = RightWindow()

        overallLayout.addWidget(leftWindow, 1)
        overallLayout.addWidget(rightWindow, 2)

        # sets up the main widget.

        widget = QWidget()
        widget.setLayout(overallLayout)
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
