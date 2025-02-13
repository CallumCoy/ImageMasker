import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from Widgets.Adjusted_Widgets import ToolBar, Viewer


# Extends the main window.
class MainWindow(QMainWindow):

    # Inilitialising.
    def __init__(self):
        super().__init__()

        # Sets window name.
        self.setWindowTitle("The Mapping App")

        # Sets the minimum size.
        self.setGeometry(100, 100, 1200, 800)

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

        self.leftWindow.applyClicked.connect(self.changeImage)

        self.rightWindow.applybuttonClicked.connect(self.applyButton)
        self.rightWindow.savebuttonClicked.connect(self.saveButton)
        self.rightWindow.randombuttonClicked.connect(self.randomButton)
        self.rightWindow.resetbuttonClicked.connect(self.resetButton)
        self.rightWindow.backbuttonClicked.connect(self.backButton)

    def changeImage(self, text):
        self.rightWindow.changeImage(text)

    def backButton(self):
        print("go back here")

    def resetButton(self):
        self.leftWindow.options.resetValues()

    def applyButton(self):
        print("apply the settings to the midified image")

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
