from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QDoubleSpinBox, QFileDialog, QTextEdit
from PyQt6.QtGui import QPixmap, QImage
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


class ToolIntBox(QSpinBox):
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


class ToolDoubleBox(QDoubleSpinBox):
    numberChange = pyqtSignal(str)

    def __init__(self, min=0, max=1, initialVal=None, tag=None, prefix=None):

        super().__init__()

        # Setting min and maxes.
        self.setMinimum(min)
        self.setMaximum(max)

        # Gives it an identifier for when the value is changed
        self.tag = tag

        # Sets the value to change by 1% when the arrows are presssed
        self.setSingleStep((max-min) / 100)

        # Sets the label
        self.setPrefix(prefix)

        # Sets a default value if given otherwise it is the midpoint of the min and max
        self.initialValue = initialVal if initialVal else ((min+max)/2)
        self.setValue(self.initialValue)

        self.textChanged.connect(self.changeRange)

    # If it has a tag send out a call to get the associated values changed.

    def changeRange(self):
        if self.tag:
            self.numberChange.emit(self.tag)

    def resetValue(self):
        self.setValue(self.initialValue)

    def randomValue(self):
        # Gets a random value at a factor of 100 so the random values can include decimals.
        self.setValue(random.randrange(
            int(self.minimum()*100), int(self.maximum()*100))/100)


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


class BaseTextBox(QTextEdit):
    maxHeight = 900

    # Inilitialising.

    def __init__(self):
        super().__init__()

        # Sets styling for the labels.
        self.setStyleSheet("""
            font-family: Courier;
            white-space: pre;
        """)

        # Sets the section to be visible, read only, and the base width.
        self.show()
        self.setReadOnly(True)
        self.setFixedWidth(600)

        # Connects the resize function to the text change event
        self.textChanged.connect(self.autoResize)

    def autoResize(self):
        # Sets the width to the texts width.
        self.document().setTextWidth(self.viewport().width())

        # Sets up the value that may be used as the height for the viewer.
        margin = self.contentsMargins()
        height = int(self.document().size().height() +
                     margin.top() + margin.bottom())

        # If the height is greater than the max then just use the max value.
        if height > self.maxHeight:
            height = self.maxHeight

        self.setFixedHeight(height)

    def formatText(self):

        # Selects all ext, then applies the fomartting.
        self.selectAll()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFontPointSize(4)

        # Clears the cursor selections so the text isn't selected no longer.
        textCursor = self.textCursor()
        textCursor.clearSelection()
        self.setTextCursor(textCursor)

    # Overwrites the resize event to the new auto resize function.
    def resizeEvent(self, e):
        self.autoResize()

    def resetValues(self):
        self.basicVersion.setChecked(False)
        self.inversePixel.setChecked(False)
        self.maxPixelDarkness.resetValue()
        self.maxWidth.resetValue()
        self.maxHeight.resetValue()

    def randomValues(self):
        self.basicVersion.setChecked(bool(random.randrange(0, 2)))
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
        self.browseButtons.fileSelected.connect(self.inputFileText)

    def emitImageDir(self):
        self.applyClicked.emit(self.searchBar.text().replace('"', ''))

    def inputFileText(self, newFile):
        # Changed the input in the textbar and sends out the command to use the new input.
        self.searchBar.setText(newFile)
        self.emitImageDir()


class fileBrowserButtons(BaseLabel):
    applyClicked = pyqtSignal(bool)
    fileSelected = pyqtSignal(str)

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
        self.browseButton.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        # Opens file search directory.
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            r"C:\\images\\",
            "Images (*.png *.jpg)"
        )

        # If a file name is returned then emit the file selection.
        if filename:
            self.fileSelected.emit(filename)


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
    successfulImageChange = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # Makes sure the image doesn't get smaller over time, TODO look into size cap.
        self.initialSize = self.size()
        self.changeImageDir(DEFAULT_IMAGE)
        self.successfulImageChange.emit(DEFAULT_IMAGE)

    def changeImageDir(self, image):
        # Checks if the image is valid.
        pixmap = QPixmap(DEFAULT_IMAGE) if QPixmap(
            image).isNull() else QPixmap(image)

        # Scales the image using the original sizing.
        pixmap = pixmap.scaled(
            self.initialSize, Qt.AspectRatioMode.KeepAspectRatio)
        self.setPixmap(pixmap)

        self.successfulImageChange.emit(DEFAULT_IMAGE if QPixmap(
            image).isNull() else image)