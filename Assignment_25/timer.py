import time
from PySide6.QtCore import QThread , Signal
from My_time import MyTime

class TimerThread(QThread) :
    signal_show = Signal(MyTime)

    def __init__(self) :
        super().__init__()
        self.time = MyTime(0, 0, 0)

    def set_time(self , h , m , s) :
        self.time = MyTime(h , m , s) 

    signal_finished = Signal()

    def run(self) :
        while True :
            if self.time.hour == 0 and self.time.minute == 0 and self.time.second == 0 :
                self.signal_show.emit(self.time)
                self.signal_finished.emit()
                break
            self.time.minus()
            self.signal_show.emit(self.time)
            time.sleep(1)