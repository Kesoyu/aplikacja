from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QFileDialog, QWidget, QTableWidget, QApplication
import csv
from PyQt6 import uic


class tab1bar(QWidget):

    column_name1 = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        uic.loadUi('tab1bar.ui', self)
        self.setWindowTitle('Wyszukaj')
        self.setcombobox()
        #self.search1.clicked.connect(self.LoadFirstTab)

    def setcombobox(self):
        with open('klienci.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_reader = next(csv_reader)
            for column_number, data in enumerate(csv_reader):
                self.comboBox.addItem(data, column_number)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget_2)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menutab1 = QtWidgets.QMenu(self.menubar)
        self.menutab1.setObjectName("menutab1")
        self.menutab2 = QtWidgets.QMenu(self.menubar)
        self.menutab2.setObjectName("menutab2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTak = QtGui.QAction(MainWindow)
        self.actionTak.setObjectName("actionTak")
        self.actionNie = QtGui.QAction(MainWindow)
        self.actionNie.setObjectName("actionNie")
        self.menutab1.addAction(self.actionTak)
        self.menutab2.addAction(self.actionNie)
        self.menubar.addAction(self.menutab1.menuAction())
        self.menubar.addAction(self.menutab2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.LoadFirstTab)
        self.pushButton.clicked.connect(self.LoadSecondTab)
        self.actionTak.triggered.connect(self.firstbar)


    def firstbar(self):
        self.tab1bar = tab1bar()
        self.tab1bar.show()


    def LoadFirstTab(self):
        with open('klienci.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            for row_number, row_data in enumerate(csv_reader):
                self.tableWidget.insertRow(row_number)
                for column_number in range(1):
                    self.tableWidget.insertColumn(column_number)
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(row_data[1])))
                    print(row_number, column_number)

    def LoadSecondTab(self):
        with open('produkty.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.setColumnCount(0)
            for row_number, row_data in enumerate(csv_reader):
                self.tableWidget_2.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_2.insertColumn(column_number)
                    self.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                    print(row_number, column_number)
                    print(data)


        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikacja"))
        self.pushButton_2.setText(_translate("MainWindow", "Load Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton.setText(_translate("MainWindow", "Load Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menutab1.setTitle(_translate("MainWindow", "tab1"))
        self.menutab2.setTitle(_translate("MainWindow", "tab2"))
        self.actionTak.setText(_translate("MainWindow", "Tak"))
        self.actionNie.setText(_translate("MainWindow", "Nie"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
