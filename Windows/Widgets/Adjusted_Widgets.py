import re
from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal


DEFAULT_IMAGE = SELECTED_IMAGE = "C:\\Users\\gamec\\Downloads\\121017.jpg"

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
    textEntered = pyqtSignal(bool)
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
    buttonClicked = pyqtSignal(str)
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

        self.browseBar.buttonClicked.connect(self.buttonClicked)




class BrowseBar(BaseLabel):
    buttonClicked = pyqtSignal(str)
    textEntered = pyqtSignal(bool)

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

        self.browseButton.clicked.connect(self.emitImageDir)

    def emitImageDir(self):
        self.buttonClicked.emit(self.searchBar.text())  

class Viewer(BaseLabel):
    applybuttonClicked = pyqtSignal(bool)
    savebuttonClicked = pyqtSignal(bool)
    randombuttonClicked = pyqtSignal(bool)
    resetbuttonClicked = pyqtSignal(bool)
    backbuttonClicked = pyqtSignal(bool)

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

        self.buttonHolder.applybuttonClicked.connect(self.applybuttonClicked)
        self.buttonHolder.savebuttonClicked.connect(self.savebuttonClicked)
        self.buttonHolder.randombuttonClicked.connect(self.randombuttonClicked)
        self.buttonHolder.resetbuttonClicked.connect(self.resetbuttonClicked)
        self.buttonHolder.backbuttonClicked.connect(self.backbuttonClicked)

    def changeImage(self, imageDir):
        self.imageDisplay.changeImage(imageDir)



class ButtonHolder(BaseLabel):
    applybuttonClicked = pyqtSignal(bool)
    savebuttonClicked = pyqtSignal(bool)
    randombuttonClicked = pyqtSignal(bool)
    resetbuttonClicked = pyqtSignal(bool)
    backbuttonClicked = pyqtSignal(bool)

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

        self.applyButton.clicked.connect(self.applybuttonClicked)
        self.saveButton.clicked.connect(self.savebuttonClicked)
        self.randomButton.clicked.connect(self.randombuttonClicked)
        self.resetButton.clicked.connect(self.resetbuttonClicked)
        self.backButton.clicked.connect(self.backbuttonClicked)

class ImageDisp(QLabel):


    def __init__(self):
        super().__init__()

        #Makes sure the image doesn't get smaller over time, TODO look into size cap.
        self.initialSize = self.size()
        self.changeImage(DEFAULT_IMAGE)

    def changeImage(self, image):
        #Checks if the image is valid.
        pixmap = QPixmap(DEFAULT_IMAGE) if QPixmap(image).isNull() else QPixmap(image)

        #Scales the image using the original sizing.
        pixmap = pixmap.scaled(
            self.initialSize, Qt.AspectRatioMode.KeepAspectRatio)
        self.setPixmap(pixmap)
            
