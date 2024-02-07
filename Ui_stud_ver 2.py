from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QTableWidgetItem
import psycopg2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_labl = QtWidgets.QLabel(self.centralwidget)
        self.main_labl.setGeometry(QtCore.QRect(220, 0, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_labl.setFont(font)
        self.main_labl.setObjectName("main_labl")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 801, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.stud_page = QtWidgets.QWidget()
        self.stud_page.setObjectName("stud_page")
        self.stud_tableWidget = QtWidgets.QTableWidget(self.stud_page)
        self.stud_tableWidget.setGeometry(QtCore.QRect(0, 10, 801, 341))
        self.stud_tableWidget.setObjectName("stud_tableWidget")
        self.stud_tableWidget.setColumnCount(4)
        self.stud_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.stud_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stud_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stud_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stud_tableWidget.setHorizontalHeaderItem(3, item)
        self.stud_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.stud_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) #Растягивание строк
        self.stud_but_add = QtWidgets.QPushButton(self.stud_page)
        self.stud_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.stud_but_add.setFont(font)
        self.stud_but_add.setObjectName("stud_but_add")
        self.stud_but_del = QtWidgets.QPushButton(self.stud_page)
        self.stud_but_del.setGeometry(QtCore.QRect(520, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.stud_but_del.setFont(font)
        self.stud_but_del.setObjectName("stud_but_del")
        self.tabWidget.addTab(self.stud_page, "")
        self.work_page = QtWidgets.QWidget()
        self.work_page.setObjectName("work_page")
        self.work_tableWidget = QtWidgets.QTableWidget(self.work_page)
        self.work_tableWidget.setGeometry(QtCore.QRect(0, 10, 801, 341))
        self.work_tableWidget.setObjectName("work_tableWidget")
        self.work_tableWidget.setColumnCount(4)
        self.work_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.work_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.work_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.work_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.work_tableWidget.setHorizontalHeaderItem(3, item)
        self.work_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.work_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) #Растягивание строк
        self.work_but_add = QtWidgets.QPushButton(self.work_page)
        self.work_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.work_but_add.setFont(font)
        self.work_but_add.setObjectName("work_but_add")
        self.work_but_del = QtWidgets.QPushButton(self.work_page)
        self.work_but_del.setGeometry(QtCore.QRect(520, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.work_but_del.setFont(font)
        self.work_but_del.setObjectName("work_but_del")
        self.tabWidget.addTab(self.work_page, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Панель администратора"))
        self.main_labl.setText(_translate("MainWindow", "Панель администратора"))
        item = self.stud_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.stud_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.stud_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Корпус"))
        item = self.stud_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Комната"))
        self.stud_but_add.setText(_translate("MainWindow", "Добавить"))
        self.stud_but_del.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stud_page), _translate("MainWindow", "Студенты"))
        item = self.work_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.work_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.work_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Должность"))
        item = self.work_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Корпус"))
        self.work_but_add.setText(_translate("MainWindow", "Добавить"))
        self.work_but_del.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.work_page), _translate("MainWindow", "Работники"))

    def add_function(self):
        self.stud_but_add.clicked.connect(self.add_record_stud)
        self.stud_but_del.clicked.connect(self.delete_records_stud)
        self.work_but_add.clicked.connect(self.add_record_work)
        self.work_but_del.clicked.connect(self.delete_records_work)


    def add_record_stud(self):
        row_count = self.stud_tableWidget.rowCount()
        self.stud_tableWidget.insertRow(row_count)

        combo = QComboBox() #ФИО
        for i in range(1, 4):
            combo.addItem(f"ФИО {i}")
        self.stud_tableWidget.setCellWidget(row_count, 1, combo)

        combo = QComboBox() #Корпуса
        for i in range(1, 4):
            combo.addItem(f"Корпус {i}")
        self.stud_tableWidget.setCellWidget(row_count, 2, combo)

        combo = QComboBox() #Комнаты
        for i in range(1, 4):
            combo.addItem(f"Комната {i}")
        self.stud_tableWidget.setCellWidget(row_count, 3, combo)

    def delete_records_stud(self):
        selected_row = self.stud_tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.stud_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            self.stud_tableWidget.removeRow(selected_row)

    def add_record_work(self):
        row_count = self.work_tableWidget.rowCount()
        self.work_tableWidget.insertRow(row_count)

        combo = QComboBox() #ФИО
        for i in range(1, 4):
            combo.addItem(f"ФИО {i}")
        self.work_tableWidget.setCellWidget(row_count, 1, combo)

        combo = QComboBox() #Должность
        for i in range(1, 4):
            combo.addItem(f"Должность {i}")
        self.work_tableWidget.setCellWidget(row_count, 2, combo)

        combo = QComboBox() #Комнаты
        for i in range(1, 4):
            combo.addItem(f"Корпус {i}")
        self.work_tableWidget.setCellWidget(row_count, 3, combo)


    def delete_records_work(self):
        selected_row = self.work_tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.work_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            self.work_tableWidget.removeRow(selected_row)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # app.aboutToQuit.connect(ui.save_red)
    MainWindow.show()
    sys.exit(app.exec_())