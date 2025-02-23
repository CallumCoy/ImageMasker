import shutil
import sys

import cv2 as cv
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QFileDialog, QMessageBox
from PyQt6.QtCore import pyqtSignal

from Packages.OutlineImage import outline
from Windows.Widgets.Edging_Adjusted_Widgets import ToolBar, Viewer
from Windows.Widgets.General_Adjusted_Widgets import DEFAULT_IMAGE

# Extends the main window.


class edgeWindowEditor(QMainWindow):
    targetImage = DEFAULT_IMAGE
    closed = pyqtSignal(bool)
    outputDir = None

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Sets window name.
        self.setWindowTitle("The Mapping App")

        # Creates a temp location for an image.
        self.outputDir = (str(Path.cwd())+"\\Images\\output.jpg").replace("\\", "\\\\")

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

    def changeImage(self, text):
        self.rightWindow.changeImage(text)

    def swapButton(self):
        self.rightWindow.imageDisplay.setVisible(
            not (self.rightWindow.imageDisplay.isVisible()))
        self.rightWindow.outputDisplay.setVisible(
            not (self.rightWindow.outputDisplay.isVisible()))

    def backButton(self):
        self.close()

    def resetButton(self):
        self.leftWindow.options.resetValues()

    def applyButton(self):
        # Calls the edging function
        output = outline(imageLoc=self.targetImage,
                              minCutoff=self.leftWindow.options.minCutoffPercent.value(),
                              maxCutoff=self.leftWindow.options.maxCutoffPercent.value(),
                              width=self.leftWindow.options.maxWidth.value(),
                              height=self.leftWindow.options.maxHeight.value())
        print(self.outputDir)
        cv.imwrite(self.outputDir, output)

        # Applies the text to the textbox. then calls for formatting.
        self.rightWindow.outputDisplay.changeImageDir(self.outputDir)

    def randomButton(self):
        self.leftWindow.options.randomValues()

    def saveButton(self):

        # Checks checks the output, if there is something to save then do so, otherwise throw out a basic warning.
        if self.outputDir:

            # Opens a dialog to select the save location then uses it to save teh .txt file.
            saveDir, _ = QFileDialog.getSaveFileName(
                self, 'Save File', r"C:\\images\\", "Image (*.png, *.jpg)")

            # Cancels the process if a locattion wasn't selected.
            if saveDir:
                shutil.copy(self.outputDir, saveDir)

        else:
            # Shows an error messages asking the user to press "Apply" before saving.
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("No File To Save")
            msg.setInformativeText(
                'No file has been created for saving.  Please press "Apply" before trying to save.')
            msg.setWindowTitle("Error")
            msg.exec()

    def closeEvent(self, a0):
        self.closed.emit(True)


def main():
    app = QApplication(sys.argv)
    window = edgeWindowEditor()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
