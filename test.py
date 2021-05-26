import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        newAction = QAction("New", self)
        fileMenu.addAction(newAction)
        uic.loadUi('test.ui', self)


# app = QApplication([])
app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget{
        font-size:25px;
    }

    QPushButton{
        font-size:10px;
    }
''')
if __name__ == "__main__":
    window = MyApp()
    window.show()

    app.exec()
