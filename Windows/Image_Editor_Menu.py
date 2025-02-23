import sys

import cv2 as cv

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QFileDialog, QMessageBox

from Packages.ASCII_Draw import drawAscii
from Windows.Widgets.Adjusted_Widgets import DEFAULT_IMAGE, ToolBar, Viewer

# Extends the main window.


class asciiWindowEditor(QMainWindow):
    targetImage = DEFAULT_IMAGE
    output = None

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
        # Calls the ASCII drawing function and saves the results.
        self.output = drawAscii(maxWidth=self.leftWindow.options.maxWidth.value(),
                                maxHeight=self.leftWindow.options.maxHeight.value(),
                                MaxThreshold=self.leftWindow.options.maxPixelDarkness.value(),
                                inverseMode=self.leftWindow.options.inversePixel.isChecked(),
                                image=cv.imread(self.targetImage))

        # Applies the text to the textbox. then calls for formatting.
        self.rightWindow.textDisplay.setText(self.output)
        self.rightWindow.textDisplay.formatText()

    def randomButton(self):
        self.leftWindow.options.randomValues()

    def saveButton(self):

        # Checks checks the output, if there is something to save then do so, otherwise throw out a basic warning.
        if self.output:

            # Opens a dialog to select the save location then uses it to save teh .txt file.
            saveDir, _ = QFileDialog.getSaveFileName(
                self, 'Save File', r"C:\\images\\", "Text (*.txt)")

            # Cancels the process if a locattion wasn't selected.
            if saveDir:
                with open(saveDir, "w") as f:
                    f.write(self.output)

        else:
            # Shows an error messages asking the user to press "Apply" before saving.
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("No File To Save")
            msg.setInformativeText(
                'No file has been created for saving.  Please press "Apply" before trying to save.')
            msg.setWindowTitle("Error")
            msg.exec()


def main():
    app = QApplication(sys.argv)
    window = asciiWindowEditor()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
