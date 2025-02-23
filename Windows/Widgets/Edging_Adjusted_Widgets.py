from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
import random

from Windows.Widgets.General_Adjusted_Widgets import BaseLabel, BaseTextBox, BasicButton, BrowseBar, ButtonHolder, ImageDisp, ToolDoubleBox, ToolIntBox

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
        self.minCutoffPercent = ToolDoubleBox(
            min=0,
            max=1,
            tag="minCutoffPercent",
            prefix="Min Cut-oof Percent: ",
            initialVal=0.45)
        self.maxCutoffPercent = ToolDoubleBox(
            min=0,
            max=1,
            tag="maxCutoffPercent",
            prefix="Max Cut-off Percent: ",
            initialVal=0.05)
        self.maxWidth = ToolIntBox(min=100, max=1400, prefix="Max Width: ")
        self.maxHeight = ToolIntBox(min=100, max=1400, prefix="Max Height: ")
        self.applySettings = BasicButton(
            "apply", "light grey", width=80, height=50)

        # Sets up the layout.
        self.toolLayout = QVBoxLayout()

        self.toolLayout.addWidget(self.minCutoffPercent)
        self.toolLayout.addWidget(self.maxCutoffPercent)
        self.toolLayout.addWidget(self.maxWidth)
        self.toolLayout.addWidget(self.maxHeight)
        self.toolLayout.addWidget(self.applySettings)

        self.toolLayout.setContentsMargins(0, 0, 0, 0)
        self.toolLayout.setSpacing(0)

        self.setLayout(self.toolLayout)

        self.applySettings.clicked.connect(self.applyClicked)

    def resetValues(self):
        self.minCutoffPercent.resetValue()
        self.maxCutoffPercent.resetValue()
        self.maxWidth.resetValue()
        self.maxHeight.resetValue()

    def randomValues(self):
        self.minCutoffPercent.randomValue()
        self.maxCutoffPercent.randomValue()
        self.maxWidth.randomValue()
        self.maxHeight.randomValue()

class Viewer(BaseLabel):
    swapButtonClicked = pyqtSignal(bool)
    savebuttonClicked = pyqtSignal(bool)
    randombuttonClicked = pyqtSignal(bool)
    resetbuttonClicked = pyqtSignal(bool)
    backbuttonClicked = pyqtSignal(bool)
    successfulImageChange = pyqtSignal(str)

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Setting up the background.

        # Creating Widgets.
        self.imageDisplay = ImageDisp()
        self.outputDisplay = ImageDisp()
        self.buttonHolder = ButtonHolder()

        # Setting up the layout for the right window.
        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(
            self.imageDisplay, 8, alignment=Qt.AlignmentFlag.AlignCenter)
        self.rightLayout.addWidget(
            self.outputDisplay, 8, alignment=Qt.AlignmentFlag.AlignCenter)
        self.rightLayout.addWidget(self.buttonHolder, 1)
        self.setLayout(self.rightLayout)

        self.outputDisplay.hide()

        self.buttonHolder.swapButtonClicked.connect(self.swapButtonClicked)
        self.buttonHolder.savebuttonClicked.connect(self.savebuttonClicked)
        self.buttonHolder.randombuttonClicked.connect(self.randombuttonClicked)
        self.buttonHolder.resetbuttonClicked.connect(self.resetbuttonClicked)
        self.buttonHolder.backbuttonClicked.connect(self.backbuttonClicked)

        self.imageDisplay.successfulImageChange.connect(
            self.successfulImageChange)

    def changeImage(self, imageDir):
        self.imageDisplay.changeImageDir(imageDir)
    
    def changeOutput(self, image):
        self.imageDisplay.changeImageWithCVImage(image)