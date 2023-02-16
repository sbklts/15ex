import random

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import os


class Task:

    def __init__(self, path):
        text, ans = [], []
        self.task_number = 5

        if path == 'if_mix':
            lst = ['data/kon/' + file for file in os.listdir('data/kon/')] + \
                  ['data/koor/' + file for file in os.listdir('data/koor/')] + \
                  ['data/otrezki/' + file for file in os.listdir('data/otrezki/')]
            help_list = []
            for i in lst:
                if 'txt' in i:
                    help_list.append(i)
            rand = random.sample(range(1, len(help_list)), self.task_number)
            for j in rand:
                t, a = read_file(lst[j])
                text.append(t)
                ans.append(a)
        else:
            lst = []
            for i in os.listdir(path):
                if 'txt' in i:
                    lst.append(i)
            rand = random.sample(range(1, len(lst)), self.task_number)
            for j in rand:
                t, a = read_file(path + lst[j])
                text.append(t)
                ans.append(a)

        self.data = text
        self.answers = ans
        self.current_task = 0
        self.correct = 0

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    data = lines[:-1]
    answer = lines[-1].split(':')[1].strip()
    return ' '.join(data), answer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 100, 20))
        self.label.setLineWidth(2)
        self.label.setObjectName("label")
        self.label_type = QtWidgets.QLabel(self.centralwidget)
        self.label_type.setGeometry(QtCore.QRect(120, 90, 151, 16))
        self.label_type.setObjectName("label_type")
        self.Button_kon = QtWidgets.QPushButton(self.centralwidget)
        self.Button_kon.setGeometry(QtCore.QRect(90, 130, 221, 41))
        self.Button_kon.setObjectName("Button_kon")
        self.Button_otr = QtWidgets.QPushButton(self.centralwidget)
        self.Button_otr.setGeometry(QtCore.QRect(90, 180, 221, 41))
        self.Button_otr.setObjectName("Button_otr")
        self.Button_koor = QtWidgets.QPushButton(self.centralwidget)
        self.Button_koor.setGeometry(QtCore.QRect(90, 230, 221, 41))
        self.Button_koor.setObjectName("Button_koor")
        self.Button_mix = QtWidgets.QPushButton(self.centralwidget)
        self.Button_mix.setGeometry(QtCore.QRect(90, 280, 221, 41))
        self.Button_mix.setObjectName("Button_mix")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Button_kon.clicked.connect(self.if_kon)
        self.Button_koor.clicked.connect(self.if_koor)
        self.Button_otr.clicked.connect(self.if_otr)
        self.Button_mix.clicked.connect(self.if_mix)

    def if_kon(self):
        tasks = Task(path='data/kon/')
        self.tasks = tasks
        self.open_window_task()

    def if_otr(self):
        tasks = Task(path='data/otrezki/')
        self.tasks = tasks
        self.open_window_task()

    def if_koor(self):
        tasks = Task(path='data/koor/')
        self.tasks = tasks
        self.open_window_task()

    def if_mix(self):
        tasks = Task(path='if_mix')
        self.tasks = tasks
        self.open_window_task()

    def if_show(self):
        _translate = QtCore.QCoreApplication.translate
        self.window_with_tasks.Button_show_answer.setText(_translate("Process", f"{self.tasks.answers[self.tasks.current_task]}"))

    def if_check(self):
        _translate = QtCore.QCoreApplication.translate
        self.window_with_tasks.users_answer.text()
        if self.window_with_tasks.users_answer.text() == self.tasks.answers[self.tasks.current_task]:
            self.window_with_tasks.Button_check.setStyleSheet("background-color: rgba(130, 255, 54, 243);")
        else:
            self.window_with_tasks.Button_check.setStyleSheet("background-color: red")

    def if_button_next(self):
        if self.window_with_tasks.users_answer.text() == self.tasks.answers[self.tasks.current_task]:
            self.tasks.correct += 1
        self.tasks.current_task += 1
        self.open_window_task()

    def show_result(self):
        self.window = QtWidgets.QMainWindow()
        self.window_with_tasks = Ui_Results()
        self.window_with_tasks.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
        _translate = QtCore.QCoreApplication.translate
        self.window_with_tasks.label_res.setText(_translate("Process", f"Вы ответили правильно на {self.tasks.correct} из {self.tasks.task_number} заданий"))
        self.window_with_tasks.Button_again.clicked.connect(self.if_button_again)


    def if_button_again(self):
        self.window = QtWidgets.QMainWindow()
        self.window_main = Ui_MainWindow()
        self.window_main.setupUi(self.window)
        self.window.show()
        # QtWidgets.QMainWindow.close()


    def open_window_task(self):
        if self.tasks.current_task < self.tasks.task_number:
            self.window = QtWidgets.QMainWindow()
            self.window_with_tasks = Ui_Process()
            self.window_with_tasks.setupUi(self.window)
            self.window.show()
            MainWindow.hide()
            _translate = QtCore.QCoreApplication.translate
            self.window_with_tasks.label_number_of_task.setText(_translate("Process", f"{self.tasks.current_task + 1}/{self.tasks.task_number}"))
            self.window_with_tasks.label_text_of_example.setText(_translate("Process", f"{self.tasks.data[self.tasks.current_task]}"))
            self.window_with_tasks.Button_show_answer.clicked.connect(self.if_show)
            self.window_with_tasks.Button_check.clicked.connect(self.if_check)
            self.window_with_tasks.Button_next.clicked.connect(self.if_button_next)
        else:
            self.show_result()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выбор типа задания"))
        self.label.setText(_translate("MainWindow", "15 задание ЕГЭ"))
        self.label_type.setText(_translate("MainWindow", "Выберите тип задания:"))
        self.Button_kon.setText(_translate("MainWindow", "побитовая конъюнкция"))
        self.Button_otr.setText(_translate("MainWindow", "числовые отрезки"))
        self.Button_koor.setText(_translate("MainWindow", "координатная плоскость"))
        self.Button_mix.setText(_translate("MainWindow", "cмешанный вариант"))



class Ui_Process(object):
    def setupUi(self, Process):
        Process.setObjectName("Process")
        Process.resize(400, 400)
        Process.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.centralwidget = QtWidgets.QWidget(Process)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_next = QtWidgets.QPushButton(self.centralwidget)
        self.Button_next.setGeometry(QtCore.QRect(277, 340, 113, 32))
        self.Button_next.setObjectName("Button_next")
        self.label_answer = QtWidgets.QLabel(self.centralwidget)
        self.label_answer.setGeometry(QtCore.QRect(10, 230, 131, 16))
        self.label_answer.setObjectName("label_answer")
        self.Button_check = QtWidgets.QToolButton(self.centralwidget)
        self.Button_check.setGeometry(QtCore.QRect(270, 230, 121, 22))
        self.Button_check.setObjectName("Button_check")
        self.users_answer = QtWidgets.QLineEdit(self.centralwidget)
        self.users_answer.setGeometry(QtCore.QRect(140, 230, 121, 21))
        self.users_answer.setStyleSheet("color: rgb(0, 0, 0);")
        self.users_answer.setText("")
        self.users_answer.setObjectName("users_answer")
        self.Button_show_answer = QtWidgets.QToolButton(self.centralwidget)
        self.Button_show_answer.setGeometry(QtCore.QRect(140, 280, 71, 22))
        self.Button_show_answer.setObjectName("Button_show_answer")
        self.label_right = QtWidgets.QLabel(self.centralwidget)
        self.label_right.setGeometry(QtCore.QRect(10, 280, 131, 16))
        self.label_right.setObjectName("label_right")
        self.label_number_of_task = QtWidgets.QLabel(self.centralwidget)
        self.label_number_of_task.setGeometry(QtCore.QRect(370, 10, 41, 16))
        self.label_number_of_task.setObjectName("label_number_of_task")
        self.label_text_of_example = QtWidgets.QLabel(self.centralwidget)
        self.label_text_of_example.setWordWrap(True)
        self.label_text_of_example.setGeometry(QtCore.QRect(10, 30, 370, 200))
        self.label_text_of_example.setObjectName("label_text_of_example")
        Process.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Process)
        self.statusbar.setObjectName("statusbar")
        Process.setStatusBar(self.statusbar)

        self.retranslateUi(Process)
        QtCore.QMetaObject.connectSlotsByName(Process)

    def retranslateUi(self, Process):
        _translate = QtCore.QCoreApplication.translate
        Process.setWindowTitle(_translate("Process", "Решаем"))
        self.Button_next.setText(_translate("Process", "Далее"))
        self.label_answer.setText(_translate("Process", "Введите свой ответ:"))
        self.Button_check.setText(_translate("Process", "Проверить"))
        self.Button_show_answer.setText(_translate("Process", "Показать"))
        self.label_right.setText(_translate("Process", "Правильный ответ:"))
        self.label_number_of_task.setText(_translate("Process", "1/10"))
        self.label_text_of_example.setText(_translate("Process", "TextLabel"))

class Ui_Results(object):
    def setupUi(self, Process):
        self.centralwidget = QtWidgets.QWidget(Process)
        Process.setObjectName("Results")
        Process.resize(300, 200)
        self.Button_again = QtWidgets.QPushButton(self.centralwidget)
        self.Button_again.setGeometry(QtCore.QRect(180, 130, 113, 32))
        self.Button_again.setObjectName("Button_again")
        self.label_res = QtWidgets.QLabel(self.centralwidget)
        self.label_res.setGeometry(QtCore.QRect(10, 10, 300, 16))
        self.label_res.setObjectName("label_res")
        Process.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Process)
        self.statusbar.setObjectName("statusbar")
        Process.setStatusBar(self.statusbar)

        self.retranslateUi(Process)
        QtCore.QMetaObject.connectSlotsByName(Process)

    def retranslateUi(self, Process):
        _translate = QtCore.QCoreApplication.translate
        Process.setWindowTitle(_translate("Process", "Результаты"))
        self.Button_again.setText(_translate("Process", "Заново"))
        self.label_res.setText(_translate("Process", "Ваши результаты:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
