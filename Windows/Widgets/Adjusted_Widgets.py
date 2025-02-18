from PyQt6.QtWidgets import QCheckBox, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QScrollArea, QAbstractScrollArea
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal
import random


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


class ToolNumbox(QSpinBox):
    numberChange = pyqtSignal(str)

    def __init__(self, min=0, max=1, initialVal=None, tag=None, prefix=None):
        super().__init__()

        # Setting min and maxes.
        self.setMinimum(min)
        self.setMaximum(max)

        # Gives it an identifier for when the value is changed
        self.tag = tag

        # Sets the value to change by 1% when the arrows are presssed
        self.setSingleStep(int((max-min) / 100))

        # Sets the label
        self.setPrefix(prefix)

        # Sets a default value if given otherwise it is the midpoint of the min and max
        self.initialValue = int(initialVal if initialVal else ((min+max)/2))
        self.setValue(self.initialValue)

        self.textChanged.connect(self.changeRange)

    # If it has a tag send out a call to get the associated values changed.
    def changeRange(self):
        if self.tag:
            self.numberChange.emit(self.tag)

    def resetValue(self):
        self.setValue(self.initialValue)

    def randomValue(self):
        # Gets a random value
        self.setValue(random.randrange(
            self.minimum(), self.maximum()))


class BaseLabel(QLabel):

    # Inilitialising.
    def __init__(self):
        super().__init__(text="")

        # Sets styling for the labels.
        self.setStyleSheet("""
            font-family: Titillium;
            font-size: 18px;
        """)

        self.show()


class ToolBar(BaseLabel):
    imageSelect = pyqtSignal(str)
    applyClicked = pyqtSignal(bool)
    # Inilitialising.

    def __init__(self):
        super().__init__()

        # Creating the widgets.
        self.browseBar = BrowseBar()
        self.options = Tools()

        # Setting up the layout.
        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.browseBar, 1)
        self.leftLayout.addWidget(self.options, 6)
        self.setLayout(self.leftLayout)

        self.browseBar.applyClicked.connect(self.imageSelect)
        self.options.applyClicked.connect(self.applyClicked)


class Tools(BaseLabel):
    applyClicked = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        # Creates the inputs.
        self.inversePixel = QCheckBox("Inverse Pixels")
        self.maxPixelDarkness = ToolNumbox(
            min=0,
            max=255,
            tag="maxCutoffPercent",
            prefix="Max Pixal Darkness: ",
            initialVal=180)
        self.maxWidth = ToolNumbox(min=100, max=400, prefix="Max Width: ")
        self.maxHeight = ToolNumbox(min=100, max=400, prefix="Max Height: ")
        self.applySettings = BasicButton(
            "apply", "light grey", width=80, height=50)

        # Sets up the layout.
        self.toolLayout = QVBoxLayout()

        self.toolLayout.addWidget(self.inversePixel)
        self.toolLayout.addWidget(self.maxPixelDarkness)
        self.toolLayout.addWidget(self.maxWidth)
        self.toolLayout.addWidget(self.maxHeight)
        self.toolLayout.addWidget(self.applySettings)

        self.toolLayout.setContentsMargins(0, 0, 0, 0)
        self.toolLayout.setSpacing(0)

        self.setLayout(self.toolLayout)

        self.applySettings.clicked.connect(self.applyClicked)

    def resetValues(self):
        self.inversePixel.setChecked(False)
        self.maxPixelDarkness.resetValue()
        self.maxWidth.resetValue()
        self.maxHeight.resetValue()

    def randomValues(self):
        self.inversePixel.setChecked(bool(random.randrange(0, 2)))
        self.maxPixelDarkness.randomValue()
        self.maxWidth.randomValue()
        self.maxHeight.randomValue()


class BrowseBar(BaseLabel):
    applyClicked = pyqtSignal(str)
    textEntered = pyqtSignal(bool)

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Setting up the background.

        self.searchBar = FileTextbox()
        self.browseButtons = fileBrowserButtons()

        self.fileBrowserLayout = QVBoxLayout()
        self.fileBrowserLayout.addWidget(self.searchBar)
        self.fileBrowserLayout.addWidget(self.browseButtons)
        self.setLayout(self.fileBrowserLayout)

        self.searchBar.returnPressed.connect(self.emitImageDir)
        self.browseButtons.applyClicked.connect(self.emitImageDir)

    def emitImageDir(self):
        self.applyClicked.emit(self.searchBar.text().replace('"', ''))


class fileBrowserButtons(BaseLabel):
    applyClicked = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        # Setting up the background.

        self.browseButton = BasicButton(
            "Browse", "light grey", width=80, height=50)
        self.applyButton = BasicButton(
            "Apply", "light grey", width=80, height=50)

        self.browserButtonsLayout = QHBoxLayout()
        self.browserButtonsLayout.addWidget(self.browseButton)
        self.browserButtonsLayout.addWidget(self.applyButton)
        self.setLayout(self.browserButtonsLayout)

        self.applyButton.clicked.connect(self.applyClicked)


class Viewer(BaseLabel):
    swapButtonClicked = pyqtSignal(bool)
    savebuttonClicked = pyqtSignal(bool)
    randombuttonClicked = pyqtSignal(bool)
    resetbuttonClicked = pyqtSignal(bool)
    backbuttonClicked = pyqtSignal(bool)

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Setting up the background.

        # Creating Widgets.
        self.imageDisplay = ImageDisp()
        self.buttonHolder = ButtonHolder()

        # Setting up the layout for the right window.
        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(
            self.imageDisplay, 8, alignment=Qt.AlignmentFlag.AlignCenter)
        self.rightLayout.addWidget(self.buttonHolder, 1)
        self.setLayout(self.rightLayout)

        self.buttonHolder.swapButtonClicked.connect(self.swapButtonClicked)
        self.buttonHolder.savebuttonClicked.connect(self.savebuttonClicked)
        self.buttonHolder.randombuttonClicked.connect(self.randombuttonClicked)
        self.buttonHolder.resetbuttonClicked.connect(self.resetbuttonClicked)
        self.buttonHolder.backbuttonClicked.connect(self.backbuttonClicked)

    def changeImage(self, imageDir):
        self.imageDisplay.changeImage(imageDir)


class ButtonHolder(BaseLabel):
    swapButtonClicked = pyqtSignal(bool)
    savebuttonClicked = pyqtSignal(bool)
    randombuttonClicked = pyqtSignal(bool)
    resetbuttonClicked = pyqtSignal(bool)
    backbuttonClicked = pyqtSignal(bool)

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Creating the buttons.
        self.swapButton = BasicButton(
            "Swap", "light grey", width=80, height=50)
        self.saveButton = BasicButton(
            "Save", "light grey", width=80, height=50)
        self.randomButton = BasicButton(
            "Random", "light grey", width=80, height=50)
        self.resetButton = BasicButton(
            "Reset", "light grey", width=80, height=50)
        self.backButton = BasicButton(
            "Back", "light grey", width=80, height=50)

        # Assigning the buttons to the widget.
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.swapButton)
        self.layout.addWidget(self.saveButton)
        self.layout.addWidget(self.randomButton)
        self.layout.addWidget(self.resetButton)
        self.layout.addWidget(self.backButton)
        self.setLayout(self.layout)

        self.swapButton.clicked.connect(self.swapButtonClicked)
        self.saveButton.clicked.connect(self.savebuttonClicked)
        self.randomButton.clicked.connect(self.randombuttonClicked)
        self.resetButton.clicked.connect(self.resetbuttonClicked)
        self.backButton.clicked.connect(self.backbuttonClicked)


class ImageDisp(QLabel):

    def __init__(self):
        super().__init__()

        # Makes sure the image doesn't get smaller over time, TODO look into size cap.
        self.initialSize = self.size()
        self.changeImage(DEFAULT_IMAGE)

    def changeImage(self, image):
        # Checks if the image is valid.
        pixmap = QPixmap(DEFAULT_IMAGE) if QPixmap(
            image).isNull() else QPixmap(image)

        # Scales the image using the original sizing.
        pixmap = pixmap.scaled(
            self.initialSize, Qt.AspectRatioMode.KeepAspectRatio)
        self.setPixmap(pixmap)
