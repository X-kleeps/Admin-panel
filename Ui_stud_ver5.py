from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QTableWidgetItem
import psycopg2


connection = psycopg2.connect(
    host = "127.0.0.1",
    user = "postgres",
    password = "xkleeps123",
    database = "postgres"
)
connection.autocommit = True

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT version();"
    )
    print(f"Версия сервера: {cursor.fetchone()}")
with connection.cursor() as cursor:
    cursor.execute(
        """SELECT id, fio, frame, room FROM stud ORDER BY id;"""
    )
    stud_records = cursor.fetchall()

with connection.cursor() as cursor:
    cursor.execute(
        """SELECT id, fio, job_title, frame FROM work ORDER BY id;"""
    )
    work_records = cursor.fetchall()

with connection.cursor() as cursor:
    cursor.execute(
        """SELECT id, fio_stud, frame, room, fio_work, job_title, description, status FROM applications ORDER BY id;"""
    )
    applications_records = cursor.fetchall()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_labl = QtWidgets.QLabel(self.centralwidget)
        self.main_labl.setGeometry(QtCore.QRect(330, 0, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_labl.setFont(font)
        self.main_labl.setObjectName("main_labl")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 1021, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.stud_page = QtWidgets.QWidget()
        self.stud_page.setObjectName("stud_page")
        self.stud_tableWidget = QtWidgets.QTableWidget(self.stud_page)
        self.stud_tableWidget.setGeometry(QtCore.QRect(0, 10, 1011, 341))
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
        self.stud_save_add = QtWidgets.QPushButton(self.stud_page)
        self.stud_save_add.setGeometry(QtCore.QRect(400, 360, 181, 61))
        self.stud_but_add = QtWidgets.QPushButton(self.stud_page)
        self.stud_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.stud_save_add.setFont(font)
        self.stud_save_add.setObjectName("stud_save_add")
        self.stud_but_add.setFont(font)
        self.stud_but_add.setObjectName("stud_but_add")
        self.stud_but_del = QtWidgets.QPushButton(self.stud_page)
        self.stud_but_del.setGeometry(QtCore.QRect(750, 360, 181, 61))
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
        self.work_tableWidget.setGeometry(QtCore.QRect(0, 10, 1011, 341))
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
        self.work_save_add = QtWidgets.QPushButton(self.work_page)
        self.work_save_add.setGeometry(QtCore.QRect(400, 360, 181, 61))
        self.work_but_add = QtWidgets.QPushButton(self.work_page)
        self.work_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.work_save_add.setFont(font)
        self.work_save_add.setObjectName("work_save_add")
        self.work_but_add.setFont(font)
        self.work_but_add.setObjectName("work_but_add")
        self.work_but_del = QtWidgets.QPushButton(self.work_page)
        self.work_but_del.setGeometry(QtCore.QRect(750, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.work_but_del.setFont(font)
        self.work_but_del.setObjectName("work_but_del")
        self.tabWidget.addTab(self.work_page, "")
        self.applications_page = QtWidgets.QWidget()
        self.applications_page.setObjectName("applications_page")
        self.applications_tableWidget = QtWidgets.QTableWidget(self.applications_page)
        self.applications_tableWidget.setGeometry(QtCore.QRect(0, 10, 1011, 341))
        self.applications_tableWidget.setObjectName("applications_tableWidget")
        self.applications_tableWidget.setColumnCount(8)
        self.applications_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(7, item)
        self.applications_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.applications_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) #Растягивание строк
        self.applications_but_add = QtWidgets.QPushButton(self.applications_page)
        self.applications_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.applications_but_add.setFont(font)
        self.applications_but_add.setObjectName("applications_but_add")
        self.applications_save_add = QtWidgets.QPushButton(self.applications_page)
        self.applications_save_add.setGeometry(QtCore.QRect(400, 360, 181, 61))
        self.applications_but_del = QtWidgets.QPushButton(self.applications_page)
        self.applications_but_del.setGeometry(QtCore.QRect(750, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.applications_save_add.setFont(font)
        self.applications_save_add.setObjectName("applications_save_add")
        self.applications_but_del.setFont(font)
        self.applications_but_del.setObjectName("applications_but_del")
        self.tabWidget.addTab(self.applications_page, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        for row_index, record in enumerate(stud_records):
            self.stud_tableWidget.insertRow(row_index)
            for col_index, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.stud_tableWidget.setItem(row_index, col_index, item)

        for row_index, record in enumerate(work_records):
            self.work_tableWidget.insertRow(row_index)
            for col_index, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.work_tableWidget.setItem(row_index, col_index, item)

        for row_index, record in enumerate(applications_records):
            self.applications_tableWidget.insertRow(row_index)
            for col_index, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.applications_tableWidget.setItem(row_index, col_index, item)

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
        self.stud_save_add.setText(_translate("MainWindow", "Сохранить"))
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
        self.work_save_add.setText(_translate("MainWindow", "Сохранить"))
        self.work_but_add.setText(_translate("MainWindow", "Добавить"))
        self.work_but_del.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.work_page), _translate("MainWindow", "Работники"))
        item = self.applications_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.applications_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО студента"))
        item = self.applications_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Корпус"))
        item = self.applications_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Комната"))
        item = self.applications_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ФИО работника"))
        item = self.applications_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Должность"))
        item = self.applications_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.applications_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Статус"))
        self.applications_save_add.setText(_translate("MainWindow", "Сохранить"))
        self.applications_but_add.setText(_translate("MainWindow", "Добавить"))
        self.applications_but_del.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.applications_page), _translate("MainWindow", "Заявки"))

    def add_function(self):
        self.stud_but_add.clicked.connect(self.add_record_stud)
        self.stud_but_del.clicked.connect(self.delete_records_stud)
        self.stud_save_add.clicked.connect(self.save_red)
        self.work_but_add.clicked.connect(self.add_record_work)
        self.work_but_del.clicked.connect(self.delete_records_work)
        self.work_save_add.clicked.connect(self.save_red)
        self.applications_but_add.clicked.connect(self.add_record_applications)
        self.applications_but_del.clicked.connect(self.delete_records_applications)
        self.applications_save_add.clicked.connect(self.save_red)


    def add_record_stud(self):
        row_count = self.stud_tableWidget.rowCount()
        self.stud_tableWidget.insertRow(row_count)

        conn = psycopg2.connect(
                host = "127.0.0.1",
                user = "postgres",
                password = "xkleeps123",
                database = "postgres"
        )

        cur = conn.cursor()
        cur.execute("SELECT fio FROM all_stud")
        data = cur.fetchall()

        combo = QComboBox()
        combo.addItems([item[0] for item in data])
        self.stud_tableWidget.setCellWidget(row_count, 1, combo)

        combo = QComboBox() #Корпуса
        for i in range(1, 6):
            combo.addItem(f"{i}")
        self.stud_tableWidget.setCellWidget(row_count, 2, combo)

        combo = QComboBox() #Комнаты
        for i in range(1, 301):
            combo.addItem(f"{i}")
        self.stud_tableWidget.setCellWidget(row_count, 3, combo)

    def delete_records_stud(self):
        selected_row = self.stud_tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.stud_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            id = item.text()  # Получение текста из элемента
            # Удаление записи из базы данных
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM stud WHERE id = %s;", (id,))
            # Удаление строки из таблицы
            self.stud_tableWidget.removeRow(selected_row)


    def add_record_work(self):
        row_count = self.work_tableWidget.rowCount()
        self.work_tableWidget.insertRow(row_count)

        # Получение значения id из предыдущей записи
        previous_id_item = self.work_tableWidget.item(row_count - 1, 0)
        previous_id = int(previous_id_item.text()) if previous_id_item is not None else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Автозаполнение поля "id" в таблице
        id_item = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.work_tableWidget.setItem(row_count, 0, id_item)

        # combo = QComboBox() #ФИО
        # for i in range(1, 4):
        #     combo.addItem(f"ФИО {i}")
        # self.work_tableWidget.setCellWidget(row_count, 1, combo)

        combo = QComboBox() #Должность
        combo.addItem("Сантехник")
        combo.addItem("Электрик")
        combo.addItem("Завхоз")
        self.work_tableWidget.setCellWidget(row_count, 2, combo)

        combo = QComboBox() #Комнаты
        for i in range(1, 6):
            combo.addItem(f"{i}")
        self.work_tableWidget.setCellWidget(row_count, 3, combo)

    def delete_records_work(self):
        selected_row = self.work_tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.work_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            id = item.text()  # Получение текста из элемента
            # Удаление записи из базы данных
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM work WHERE id = %s;", (id,))
            # Удаление строки из таблицы
            self.work_tableWidget.removeRow(selected_row)


    def add_record_applications(self):
        row_count = self.applications_tableWidget.rowCount()
        self.applications_tableWidget.insertRow(row_count)

        # Получение значения id из предыдущей записи
        previous_id_item = self.applications_tableWidget.item(row_count - 1, 0)
        previous_id = int(previous_id_item.text()) if previous_id_item is not None else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Автозаполнение поля "id" в таблице
        id_item = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.applications_tableWidget.setItem(row_count, 0, id_item)

        conn = psycopg2.connect(
                host = "127.0.0.1",
                user = "postgres",
                password = "xkleeps123",
                database = "postgres"
        )

        cur = conn.cursor()
        cur.execute("SELECT fio FROM stud")
        data = cur.fetchall()


        combo = QComboBox()
        combo.addItems([item[0] for item in data])
        self.applications_tableWidget.setCellWidget(row_count, 1, combo)

        combo = QComboBox() #Корпус
        for i in range(1, 6):
            combo.addItem(f"{i}")
        self.applications_tableWidget.setCellWidget(row_count, 2, combo)

        combo = QComboBox() #Корпус
        for i in range(1, 301):
            combo.addItem(f"{i}")
        self.applications_tableWidget.setCellWidget(row_count, 3, combo)

        combo = QComboBox() #Должность
        combo.addItem("Сантехник")
        combo.addItem("Электрик")
        combo.addItem("Завхоз")
        self.applications_tableWidget.setCellWidget(row_count, 5, combo)

        cur = conn.cursor()
        cur.execute("SELECT fio FROM work")
        data1 = cur.fetchall()

        combo = QComboBox()
        combo.addItems([item[0] for item in data1])
        self.applications_tableWidget.setCellWidget(row_count, 4, combo)

        combo = QComboBox() #Статус
        combo.addItem("В обработке")
        combo.addItem("Завнершенно")
        combo.addItem("Не завнершенно")
        self.applications_tableWidget.setCellWidget(row_count, 7, combo)        

    def delete_records_applications(self):
        selected_row = self.applications_tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.applications_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            id = item.text()  # Получение текста из элемента
            # Удаление записи из базы данных
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM applications WHERE id = %s;", (id,))
            # Удаление строки из таблицы
            self.applications_tableWidget.removeRow(selected_row)


    def save_red(self):
        try:
            for row in range(self.stud_tableWidget.rowCount()):
                id = self.stud_tableWidget.item(row, 0).text()

                # fio = self.stud_tableWidget.item(row, 1).text()

                fio_widget = self.stud_tableWidget.cellWidget(row, 1)  # Получаем виджет из указанной ячейки
                if fio_widget is not None:  # Проверяем, что виджет существует
                    fio = fio_widget.currentText()  # Получаем выбранное значение из комбобокса для корпуса
                else:
                    fio = ""  # Или устанавливаем значение по умолчанию

                frame_widget = self.stud_tableWidget.cellWidget(row, 2)  # Получаем виджет из указанной ячейки
                if frame_widget is not None:  # Проверяем, что виджет существует
                    frame = frame_widget.currentText()  # Получаем выбранное значение из комбобокса для корпуса
                else:
                    frame = ""  # Или устанавливаем значение по умолчанию

                room_widget = self.stud_tableWidget.cellWidget(row, 3)  # Получаем виджет из указанной ячейки
                if room_widget is not None:  # Проверяем, что виджет существует
                    room = room_widget.currentText()  # Получаем выбранное значение из комбобокса для комнаты
                else:
                    room = ""  # Или устанавливаем значение по умолчанию

            with connection.cursor() as cursor:
                cursor.execute('''INSERT INTO stud (id, fio, frame, room)
                    VALUES (%s, %s, %s, %s)''', (id, fio, frame, room))

            # Подтверждение изменений и закрытие соединения
            connection.commit()
            # connection.close()
            print("Данные успешно занесены в базу данных.")
        except Exception as a:
            print("Не введенны значения")

        try:
            for row in range(self.work_tableWidget.rowCount()):
                id = self.work_tableWidget.item(row, 0).text()
                fio = self.work_tableWidget.item(row, 1).text()

                frame_widget = self.work_tableWidget.cellWidget(row, 2)  # Получаем виджет из указанной ячейки
                if frame_widget is not None:  # Проверяем, что виджет существует
                    frame = frame_widget.currentText()  # Получаем выбранное значение из комбобокса для комнаты
                else:
                    frame = ""  # Или устанавливаем значение по умолчанию

                frame_widget = self.work_tableWidget.cellWidget(row, 3)  # Получаем виджет из указанной ячейки
                if frame_widget is not None:  # Проверяем, что виджет существует
                    frame = frame_widget.currentText()  # Получаем выбранное значение из комбобокса для комнаты
                else:
                    frame = ""  # Или устанавливаем значение по умолчанию

                job_title_widget = self.work_tableWidget.cellWidget(row, 5)  # Получаем виджет из указанной ячейки
                if job_title_widget is not None:  # Проверяем, что виджет существует
                    job_title = job_title_widget.currentText()  # Получаем выбранное значение из комбобокса для корпуса
                else:
                    job_title = ""  # Или устанавливаем значение по умолчанию


            with connection.cursor() as cursor:
                cursor.execute('''INSERT INTO work (id, fio, job_title, frame)
                    VALUES (%s, %s, %s, %s)''', (id, fio, job_title, frame))

            # Подтверждение изменений и закрытие соединения
            connection.commit()
            # connection.close()
            print("Данные успешно занесены в базу данных.")
        except Exception as a:
            print("Не введенны значения")

        try:
            for row in range(self.applications_tableWidget.rowCount()):
                id = self.applications_tableWidget.item(row, 0).text()
                description = self.applications_tableWidget.item(row, 6).text()

                fio_stud_widget = self.applications_tableWidget.cellWidget(row, 1)  # Получаем виджет из указанной ячейки
                if fio_stud_widget is not None:  # Проверяем, что виджет существует
                    fio_stud = fio_stud_widget.currentText()  # Получаем выбранное значение из комбобокса для комнаты
                else:
                    fio_stud = ""  # Или устанавливаем значение по умолчанию

                fio_work_widget = self.applications_tableWidget.cellWidget(row, 4)  # Получаем виджет из указанной ячейки
                if fio_work_widget is not None:  # Проверяем, что виджет существует
                    fio_work = fio_work_widget.currentText()  # Получаем выбранное значение из комбобокса для комнаты
                else:
                    fio_work = ""  # Или устанавливаем значение по умолчанию

                frame_widget = self.applications_tableWidget.cellWidget(row, 2)  # Получаем виджет из указанной ячейки
                if frame_widget is not None:  # Проверяем, что виджет существует
                    frame = frame_widget.currentText()  # Получаем выбранное значение из комбобокса для комнаты
                else:
                    frame = ""  # Или устанавливаем значение по умолчанию

                room_widget = self.applications_tableWidget.cellWidget(row, 3)  # Получаем виджет из указанной ячейки
                if room_widget is not None:  # Проверяем, что виджет существует
                    room = room_widget.currentText()  # Получаем выбранное значение из комбобокса для комнаты
                else:
                    room = ""  # Или устанавливаем значение по умолчанию

                job_title_widget = self.applications_tableWidget.cellWidget(row, 5)  # Получаем виджет из указанной ячейки
                if job_title_widget is not None:  # Проверяем, что виджет существует
                    job_title = job_title_widget.currentText()  # Получаем выбранное значение из комбобокса для корпуса
                else:
                    job_title = ""  # Или устанавливаем значение по умолчанию

                status_widget = self.applications_tableWidget.cellWidget(row, 7)  # Получаем виджет из указанной ячейки
                if status_widget is not None:  # Проверяем, что виджет существует
                    status = status_widget.currentText()  # Получаем выбранное значение из комбобокса для корпуса
                else:
                    status = ""  # Или устанавливаем значение по умолчанию
                

            with connection.cursor() as cursor:
                cursor.execute('''INSERT INTO applications (id, fio_stud, frame, room, fio_work, job_title, description, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', (id, fio_stud, frame, room, fio_work, job_title, description, status))

            # Подтверждение изменений и закрытие соединения
            connection.commit()
            # connection.close()
            print("Данные успешно занесены в базу данных.")
        except Exception as a:
            print("Не введенны значения")
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # app.aboutToQuit.connect(ui.save_red)
    MainWindow.show()
    sys.exit(app.exec_())