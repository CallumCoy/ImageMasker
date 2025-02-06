import re
from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


DEFAULT_IMAGE = SELECTED_IMAGE = "Images\\pythonImage.jpg"

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

class FileTextbox(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setClearButtonEnabled(True)
        self.setStyleSheet("""
            font-family: Titillium;
            font-size: 18px;
        """)
    
    def textChanged(e):
        global SELECTED_IMAGE 
        SELECTED_IMAGE = e

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
        self.browseBar = BrowseBar()
        self.options = BaseLabel()

        # Setting up the layout.
        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.browseBar, 1)
        self.leftLayout.addWidget(self.options, 6)
        self.setLayout(self.leftLayout)


class BrowseBar(BaseLabel):

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Setting up the background.
        self.setStyleSheet("""
            background-color: #202020;
            color: #FFFFFF;
        """)

        self.searchBar = FileTextbox()
        self.browseButton = BasicButton("Browse", "light grey", width=80, height=50)
        self.browseButton.setText("Browse")

        self.fileBrowserLayout = QVBoxLayout()
        self.fileBrowserLayout.addWidget(self.searchBar)
        self.fileBrowserLayout.addWidget(self.browseButton)
        self.setLayout(self.fileBrowserLayout)


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
        self.imageDisplay = ImageDisp()
        self.buttonHolder = ButtonHolder()

        # Setting up the layout for the right window.
        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(
            self.imageDisplay, 8, alignment=Qt.AlignmentFlag.AlignCenter)
        self.rightLayout.addWidget(self.buttonHolder, 1)
        self.setLayout(self.rightLayout)


class ButtonHolder(BaseLabel):

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Creating the buttons.
        self.applyButton = BasicButton("Apply", "light grey", width=80, height=50)
        self.saveButton = BasicButton("Save", "light grey", width=80, height=50)
        self.randomButton = BasicButton("Random", "light grey", width=80, height=50)
        self.resetButton = BasicButton("Swap", "light grey", width=80, height=50)
        self.backButton = BasicButton("Back", "light grey", width=80, height=50)

        # Assigning the buttons to the widget.
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.applyButton)
        self.layout.addWidget(self.saveButton)
        self.layout.addWidget(self.randomButton)
        self.layout.addWidget(self.resetButton)
        self.layout.addWidget(self.backButton)
        self.setLayout(self.layout)


class ImageDisp(QLabel):
    def __init__(self):
        super().__init__()
        self.changeImage()

    def changeImage(self, image):
        image_pattern = re.compile(r'\.(jpg|jpeg|png|gif|bmp|tiff)$', re.IGNORECASE)

        pixmap = QPixmap(image if image_pattern else DEFAULT_IMAGE)
        pixmap = pixmap.scaled(
            self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.setPixmap(pixmap)
            
