import pytz
import time
from PySide6.QtCore import QThread , Signal
from datetime import datetime

class WorldClock_Thread(QThread) :
    
    signal_clock = Signal(str , str , str)

    def __init__(self) :
        super().__init__()

        self.iran_tz = pytz.timezone("Asia/Tehran")
        self.usa_tz = pytz.timezone("America/New_York")
        self.germany_tz = pytz.timezone("Europe/Berlin")


    def run(self) :
        while True :

            now_utc = datetime.now(pytz.utc)

            USA_time = now_utc.astimezone(self.usa_tz).strftime("%H : %M : %S")
            Iran_time = now_utc.astimezone(self.iran_tz).strftime("%H : %M : %S")
            Germany_time = now_utc.astimezone(self.germany_tz).strftime("%H : %M : %S")

            self.signal_clock.emit(USA_time,Iran_time,Germany_time)

            time.sleep(1)
