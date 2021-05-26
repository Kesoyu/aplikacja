import csv
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QWidget
from PyQt6 import uic

class tab1bar(QWidget):

    #column_name1 = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        uic.loadUi('tab1bar.ui', self)
        self.setWindowTitle('Wyszukaj')
        self.setcombobox()
        #self.pushButton.clicked.connect(self.setcombobox)

    def setcombobox(self):
        with open('produkty.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_reader = next(csv_reader)
            for column_number, data in enumerate(csv_reader):
                self.comboBox.addItem(data, column_number)

    #def emitSignal(self):
        #value = self.comboBox.currentText()
        #self.column_name1.emit(value)
        #print(value)
        #print(self.column_name1)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi('appGui.ui', self)
        self.tab1bar = tab1bar()
        self.pushButton_2.clicked.connect(self.LoadFirstTab)
        self.pushButton.clicked.connect(self.LoadSecondTab)
        self.actionTak.triggered.connect(self.firstbar)


    def firstbar(self):
        self.tab1bar.show()

    def initUI(self):
        self.show()

    def LoadFirstTab(self):
        with open('klienci.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(3)

            #for row_idx in range(7):
            for row_number, row_data in enumerate(csv_reader):
                self.tableWidget.insertRow(row_number)
                self.tableWidget.setItem(row_number, 0, QTableWidgetItem(row_data[0]))
                self.tableWidget.setItem(row_number, 1, QTableWidgetItem(row_data[1]))
                self.tableWidget.setItem(row_number, 2, QTableWidgetItem(row_data[2]))

    def LoadSecondTab(self):
        with open('produkty.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            text = self.tab1bar.comboBox.currentText()
            idx = 20
            a = 0
            for row in csv_reader:
                print(text, row)
                for a in range(6):
                    print(a)
                    if text == row[a]:
                        idx = a
                        break
                break
            if idx == 0:
                self.tableWidget_2.setRowCount(0)
                self.tableWidget_2.setColumnCount(5)
                i = 0
                for row_number, row_data in enumerate(csv_reader):
                    self.tableWidget_2.insertRow(row_number)
                    for i in range(5):
                        self.tableWidget_2.setItem(row_number, i, QTableWidgetItem(row_data[i]))
            else:
                self.tableWidget_2.setRowCount(0)
                self.tableWidget_2.setColumnCount(1)
                i = 0
                # for row_idx in range(7):
                for row_number, row_data in enumerate(csv_reader):
                    # print(row_data[1])
                    self.tableWidget_2.insertRow(row_number)
                    # for i in range(5):
                    self.tableWidget_2.setItem(row_number, 0, QTableWidgetItem(row_data[idx]))
                    # self.tableWidget_2.setItem(row_number, 1, QTableWidgetItem(row_data[1]))
                    # self.tableWidget_2.setItem(row_number, 2, QTableWidgetItem(row_data[2]))
                    # self.tableWidget_2.setItem(row_number, 3, QTableWidgetItem(row_data[3]))
                    # self.tableWidget_2.setItem(row_number, 4, QTableWidgetItem(row_data[4]))





def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
