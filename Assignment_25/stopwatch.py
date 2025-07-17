import time
from PySide6.QtCore import QThread , Signal
from My_time import MyTime


class StopwatchThread(QThread) : 

    signal_show = Signal(MyTime)

    def __init__(self) :
        super().__init__()
        self.time = MyTime(00, 00, 00) 
        
    def run(self) :
        while True :
            self.time.plus()
            # print(self.second)
            self.signal_show.emit(self.time)
            time.sleep(1)
            

    def reset(self) :
        self.time.second = 00
        self.time.minute = 00
        self.time.hour = 00