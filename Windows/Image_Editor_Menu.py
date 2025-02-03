import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from Widgets.Adjusted_Widgets import ToolBar, Viewer



# Extends the main window.
class MainWindow(QMainWindow):

    #Inilitialising.
    def __init__(self):
        super().__init__()

        # Sets window name.
        self.setWindowTitle("The Mapping App")

        # Sets the minimum size.
        self.setGeometry(100, 100, 1200, 800)

        # Sets left right window layout.
        overallLayout = QHBoxLayout()

        leftWindow = ToolBar()
        rightWindow = Viewer()

        overallLayout.addWidget(leftWindow, 1)
        overallLayout.addWidget(rightWindow, 2)

        # sets up the main widget.

        widget = QWidget()
        widget.setLayout(overallLayout)
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
