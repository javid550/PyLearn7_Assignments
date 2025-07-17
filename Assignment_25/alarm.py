import time
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QThread , Signal , QTimer
from functools import partial
from datetime import datetime
from database import Database


class AlarmThread(QThread) :

    signal_alarm = Signal(list)

    def __init__(self , ui):
        super().__init__()
        self.ui = ui

        self.db = Database()

        self.signal_alarm.connect(self.read_from_database)
        
        self.ui.add_alarm.clicked.connect(self.add_alarms)

        self.alarm_timer = QTimer()
        self.alarm_timer.timeout.connect(self.check_alarm)
        self.alarm_timer.start(1000)

    def run(self) :
        while True :
            time.sleep(1)

    def add_alarms(self) :

        time = self.ui.timeEdit.time().toString("HH:mm:ss")

        if time :
            feedback = self.db.add_new_alarm(time)
            if feedback is True :
                alarms = self.db.get_tasks()
                self.signal_alarm.emit(alarms)
            else :
                QMessageBox.critical(self.ui, "Error", "Please try again : ( ")
        else :
            QMessageBox.warning(self.ui, "❓❓❓", "Title cannot be empty.")

    def edit_alarm(self , old_time ) :
        new_time , ok = QInputDialog.getText(self.ui, "Edit Alarm" , "Enter new time (HH:MM:SS): ")
        if ok and new_time :
            self.db.edit_task(old_time , new_time)
            alarms = self.db.get_tasks()
            self.signal_alarm.emit(alarms)

    def remove_alarm(self , time) :
        self.db.remove_task(time)
        alarms = self.db.get_tasks()
        self.signal_alarm.emit(alarms)

    def check_alarm(self) :
        now = datetime.now().strftime("%H:%M:%S")
        alarms = self.db.get_tasks()
        
        for i, alarm in enumerate(alarms):

            time_str = alarm[0]

            if time_str == now :
                QMessageBox.critical(self.ui, "Alarm ⏰", f"Alarm time: {now} ❗❗❗") 

    def read_from_database(self , alarms) :

        while self.ui.gird_alarm.count() :
            item = self.ui.gird_alarm.takeAt(0)
            widget = item.widget()
            if widget is not None :
                widget.deleteLater()
        
        for i, task in enumerate(alarms):
            time_str = task[0]
            
            del_btn = QPushButton("❌")
            del_btn.setFixedSize(32,32)
            del_btn.clicked.connect(partial(self.remove_alarm,time_str))

            edit_btn = QPushButton("🖊")
            edit_btn.setFixedSize(32,32)
            edit_btn.clicked.connect(partial(self.edit_alarm,time_str))

            label = QLineEdit(time_str)

            font = QFont()
            font.setPointSize(15)
            label.setFont(font)
            label.setFrame(False)
            label.setReadOnly(True)
            label.setFixedHeight(32)
            label.setAlignment(Qt.AlignCenter)

            self.ui.gird_alarm.addWidget(del_btn , i , 0)
            self.ui.gird_alarm.addWidget(edit_btn , i , 1)
            self.ui.gird_alarm.addWidget(label , i , 2)