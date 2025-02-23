import sys

import cv2 as cv

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from Packages.ASCII_Draw import drawAscii
from Windows.Widgets.Adjusted_Widgets import DEFAULT_IMAGE, ToolBar, Viewer

# Extends the main window.


class MainWindow(QMainWindow):
    targetImage = DEFAULT_IMAGE
    output = "Hi"

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Sets window name.
        self.setWindowTitle("The Mapping App")

        # Sets the minimum size.
        self.setGeometry(100, 100, 1200, 1000)

        # Sets left right window layout.
        self.overallLayout = QHBoxLayout()

        self.leftWindow = ToolBar()
        self.rightWindow = Viewer()

        self.overallLayout.addWidget(self.leftWindow, 1)
        self.overallLayout.addWidget(self.rightWindow, 2)

        # sets up the main widget.

        self.widget = QWidget()
        self.widget.setLayout(self.overallLayout)
        self.setCentralWidget(self.widget)

        self.leftWindow.imageSelect.connect(self.changeImage)
        self.leftWindow.options.applyClicked.connect(self.applyButton)

        self.rightWindow.swapButtonClicked.connect(self.swapButton)
        self.rightWindow.savebuttonClicked.connect(self.saveButton)
        self.rightWindow.randombuttonClicked.connect(self.randomButton)
        self.rightWindow.resetbuttonClicked.connect(self.resetButton)
        self.rightWindow.backbuttonClicked.connect(self.backButton)

        self.rightWindow.successfulImageChange.connect(
            self.successfulImageChange)

    def successfulImageChange(self, text):
        self.targetImage = text
        print(text)

    def changeImage(self, text):
        self.rightWindow.changeImage(text)

    def swapButton(self):
        self.rightWindow.imageDisplay.setVisible(
            not (self.rightWindow.imageDisplay.isVisible()))
        self.rightWindow.textDisplay.setVisible(
            not (self.rightWindow.textDisplay.isVisible()))

    def backButton(self):
        print("go back here")

    def resetButton(self):
        self.leftWindow.options.resetValues()

    def applyButton(self):
        #Calls the ASCII drawing function and saves the results.
        self.output = drawAscii(maxWidth=self.leftWindow.options.maxWidth.value(),
                                maxHeight=self.leftWindow.options.maxHeight.value(),
                                MaxThreshold=self.leftWindow.options.maxPixelDarkness.value(),
                                inverseMode=self.leftWindow.options.inversePixel.isChecked(),
                                image=cv.imread(self.targetImage))

        #Applies the text to the textbox. then calls for formatting.
        self.rightWindow.textDisplay.setText(self.output)
        self.rightWindow.textDisplay.formatText()
        
    def randomButton(self):
        self.leftWindow.options.randomValues()

    def saveButton(self):
        print("save mofified image")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
