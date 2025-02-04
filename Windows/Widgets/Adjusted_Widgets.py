from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

PYTHON_IMAGE = "Images\\pythonImage.jpg"

# Extends the base button class


class BasicButton(QPushButton):

    # Initialises some basic aspects of the buttons
    def __init__(self, text, color, **args):
        super().__init__()

        # Sets the buttons text
        self.setText(text)

        # Sets the minimum button size if needed
        if "width" in args and "height" in args:
            self.setMinimumSize(args["width"], args["height"])

        # Sets the color for the button
        self.setAutoFillBackground(True)
        self.setStyleSheet("""
            font-family: Titillium;
            font-size: 18px;
            background-color: """ + str(color))


class BaseLabel(QLabel):

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Sets styling for the labels.
        self.setStyleSheet("""
            background-color: #262626;
            color: #FFFFFF;
            font-family: Titillium;
            font-size: 18px;
        """)

        # Enables the background for the labels.
        self.setAutoFillBackground(True)
        self.show()


class ToolBar(BaseLabel):

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Setting up the background.
        self.setStyleSheet("""
            background-color: #262626;
            color: #FFFFFF;
        """)

        # Creating the widgets.
        browseBar = BrowseBar()
        Options = BaseLabel()

        # Setting up the layout.
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(browseBar, 1)
        leftLayout.addWidget(Options, 6)
        self.setLayout(leftLayout)


class BrowseBar(BaseLabel):

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Setting up the background.
        self.setStyleSheet("""
            background-color: #202020;
            color: #FFFFFF;
        """)

        searchBar = QLineEdit()
        browseButton = BasicButton("Browse", "light grey", width=80, height=50)
        browseButton.setText("Browse")

        searchBar.setClearButtonEnabled(True)
        searchBar.setStyleSheet("""
            font-family: Titillium;
            font-size: 18px;
        """)

        fileBrowserLayout = QVBoxLayout()
        fileBrowserLayout.addWidget(searchBar)
        fileBrowserLayout.addWidget(browseButton)
        self.setLayout(fileBrowserLayout)


class Viewer(BaseLabel):

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Setting up the background.
        self.setStyleSheet("""
            background-color: #262626;
            color: #FFFFFF;
        """)

        # Creating Widgets.
        imageDisplay = ImageDisp()
        buttonHolder = ButtonHolder()

        # Setting up the layout for the right window.
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(
            imageDisplay, 8, alignment=Qt.AlignmentFlag.AlignCenter)
        rightLayout.addWidget(buttonHolder, 1)
        self.setLayout(rightLayout)


class ButtonHolder(BaseLabel):

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Creating the buttons.
        applyButton = BasicButton("Apply", "light grey", width=80, height=50)
        saveButton = BasicButton("Save", "light grey", width=80, height=50)
        randomButton = BasicButton("Random", "light grey", width=80, height=50)
        resetButton = BasicButton("Swap", "light grey", width=80, height=50)
        backButton = BasicButton("Back", "light grey", width=80, height=50)

        # Assigning the buttons to the widget.
        layout = QHBoxLayout()
        layout.addWidget(applyButton)
        layout.addWidget(saveButton)
        layout.addWidget(randomButton)
        layout.addWidget(resetButton)
        layout.addWidget(backButton)
        self.setLayout(layout)


class ImageDisp(QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap(PYTHON_IMAGE)
        pixmap = pixmap.scaled(
            self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.setPixmap(pixmap)
