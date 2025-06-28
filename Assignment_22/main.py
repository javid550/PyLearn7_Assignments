import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from functools import partial
from Main_Window import Ui_MainWindow
from database import Database



class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.db = Database()

        self.read_from_database()

        self.ui.btn_NewTask.clicked.connect(self.new_task)

    def new_task(self) :
        title = self.ui.textbox_NewTask.text()
        discription = self.ui.tb_newtask_description.toPlainText()
        date = self.ui.DateTime.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        if title :
            feedback = self.db.add_new_task(title , discription , date)
            if feedback == True :
                self.ui.textbox_NewTask.setText("")
                self.ui.tb_newtask_description.clear()
                self.read_from_database()
            else :
                QMessageBox.critical(self, "Error", "Please try again : ( ")
        else :
            QMessageBox.warning(self, "❓❓❓", "Title cannot be empty.")

    def update_tasks(self , title) :
        self.db.update_task(title) 
        self.read_from_database()


    def remove_task(self , title) :
        self.db.remove_task(title) 
        self.read_from_database()

    def show_info(self , title , discription , date , event=None) :
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(f" {discription} \n Time : {date}")
        msg_box.exec()


    def read_from_database(self) :

        tasks = self.db.get_tasks()
        
        for i, task in enumerate(tasks):
            
            task_id , title , desc , is_done , date , priority = task
            
            checkbox = QCheckBox()
            checkbox.setChecked(bool(is_done))
            checkbox.stateChanged.connect(lambda stete , t=title : self.update_tasks(t))

            del_btn = QPushButton("❌")
            del_btn.clicked.connect(lambda _ , t=title : self.remove_task(t))

            # label = QLabel()
            label = QLabel(str(title))
            label.mousePressEvent = lambda event , t=title, d=desc, dt=date : self.show_info(t , d , dt) # or partial(self.show_info, title, desc, date)

            if is_done == 1 :
                label.setStyleSheet("color: rgb(60,60,60);text-decoration : line-through")

            if priority == 1 :
                label.setStyleSheet("color:rgb(255,0,0);")
                if is_done == 1 :
                    label.setStyleSheet("color: rgb(60,60,60);text-decoration : line-through")

            elif priority == 2 :
                label.setStyleSheet("color:rgb(170,0,0);")
                if is_done == 1 :
                    label.setStyleSheet("color: rgb(60,60,60);text-decoration : line-through")


            self.ui.gl_tasks.addWidget(checkbox , i , 1)
            self.ui.gl_tasks.addWidget(del_btn , i , 0)
            self.ui.gl_tasks.addWidget(label , i , 2)


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    # app.exec_()
    sys.exit(app.exec())