<<<<<<< HEAD
import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from worldclock import WorldClock_Thread
from stopwatch import StopwatchThread
from alarm import AlarmThread
from timer import TimerThread

def update_world_clock(usa , iran , germany) :
        
        main_window.usa_label.setText(usa)
        main_window.iran_label.setText(iran)
        main_window.germany_label.setText(germany)


def start_timer() :
    h = int(main_window.txt_hour.text())
    m = int(main_window.txt_min.text())
    s = int(main_window.txt_sec.text())
    thread_timer.set_time(h , m , s)
    thread_timer.start()

def stop_timer() :
    thread_timer.terminate()

def reset_timer() :
    main_window.txt_hour.setText("00")
    main_window.txt_min.setText("00")
    main_window.txt_sec.setText("00")
    thread_timer.terminate()
    # thread_timer.reset()


def start_stopwatch() :
    thread_stopwatch.start()

def stop_stopwatch() :
    thread_stopwatch.terminate()

def reset_stopwatch() :
    main_window.label_stopwatch.setText("00:00:00")
    thread_stopwatch.terminate()
    thread_stopwatch.reset()


def show_time_timer(time) : 
    main_window.txt_hour.setText(f"{time.hour:02}")
    main_window.txt_min.setText(f"{time.minute:02}")
    main_window.txt_sec.setText(f"{time.second:02}")

def show_timer_finished() :
    QMessageBox.critical(main_window , "00:00:00", "⏰ _ Time's up ❗❗❗") 

def show_time_stopwatch(time) :
    main_window.label_stopwatch.setText(f"{time.hour:02}:{time.minute:02}:{time.second:02}")


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    loader = QUiLoader()
    
    main_window = loader.load("mainwindow.ui")
    main_window.show()


    thread_worldclock = WorldClock_Thread()
    thread_worldclock.signal_clock.connect(update_world_clock)
    thread_worldclock.start()
    thread_stopwatch = StopwatchThread()
    thread_timer = TimerThread()
    thread_alarm = AlarmThread(main_window)
    thread_alarm.signal_alarm.connect(thread_alarm.read_from_database)
    thread_alarm.signal_alarm.emit(thread_alarm.db.get_tasks())
    thread_alarm.start()

    main_window.label_stopwatch.setText("00:00:00")
    main_window.start_stopwatch.clicked.connect(start_stopwatch)
    main_window.reset_stopwatch.clicked.connect(reset_stopwatch)
    main_window.stop_stopwatch.clicked.connect(stop_stopwatch)
    main_window.start_timer.clicked.connect(start_timer)
    main_window.reset_timer.clicked.connect(reset_timer)
    main_window.stop_timer.clicked.connect(stop_timer)
    thread_timer.signal_show.connect(show_time_timer)
    thread_timer.signal_finished.connect(show_timer_finished)
    thread_stopwatch.signal_show.connect(show_time_stopwatch)
    thread_alarm.signal_alarm.emit(thread_alarm.db.get_tasks())

=======
import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from worldclock import WorldClock_Thread
from stopwatch import StopwatchThread
from alarm import AlarmThread
from timer import TimerThread

def update_world_clock(usa , iran , germany) :
        
        main_window.usa_label.setText(usa)
        main_window.iran_label.setText(iran)
        main_window.germany_label.setText(germany)


def start_timer() :
    h = int(main_window.txt_hour.text())
    m = int(main_window.txt_min.text())
    s = int(main_window.txt_sec.text())
    thread_timer.set_time(h , m , s)
    thread_timer.start()

def stop_timer() :
    thread_timer.terminate()

def reset_timer() :
    main_window.txt_hour.setText("00")
    main_window.txt_min.setText("00")
    main_window.txt_sec.setText("00")
    thread_timer.terminate()
    # thread_timer.reset()


def start_stopwatch() :
    thread_stopwatch.start()

def stop_stopwatch() :
    thread_stopwatch.terminate()

def reset_stopwatch() :
    main_window.label_stopwatch.setText("00:00:00")
    thread_stopwatch.terminate()
    thread_stopwatch.reset()


def show_time_timer(time) : 
    main_window.txt_hour.setText(f"{time.hour:02}")
    main_window.txt_min.setText(f"{time.minute:02}")
    main_window.txt_sec.setText(f"{time.second:02}")

def show_timer_finished() :
    QMessageBox.critical(main_window , "00:00:00", "⏰ _ Time's up ❗❗❗") 

def show_time_stopwatch(time) :
    main_window.label_stopwatch.setText(f"{time.hour:02}:{time.minute:02}:{time.second:02}")


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    loader = QUiLoader()
    
    main_window = loader.load("mainwindow.ui")
    main_window.show()


    thread_worldclock = WorldClock_Thread()
    thread_worldclock.signal_clock.connect(update_world_clock)
    thread_worldclock.start()
    thread_stopwatch = StopwatchThread()
    thread_timer = TimerThread()
    thread_alarm = AlarmThread(main_window)
    thread_alarm.signal_alarm.connect(thread_alarm.read_from_database)
    thread_alarm.signal_alarm.emit(thread_alarm.db.get_tasks())
    thread_alarm.start()

    main_window.label_stopwatch.setText("00:00:00")
    main_window.start_stopwatch.clicked.connect(start_stopwatch)
    main_window.reset_stopwatch.clicked.connect(reset_stopwatch)
    main_window.stop_stopwatch.clicked.connect(stop_stopwatch)
    main_window.start_timer.clicked.connect(start_timer)
    main_window.reset_timer.clicked.connect(reset_timer)
    main_window.stop_timer.clicked.connect(stop_timer)
    thread_timer.signal_show.connect(show_time_timer)
    thread_timer.signal_finished.connect(show_timer_finished)
    thread_stopwatch.signal_show.connect(show_time_stopwatch)
    thread_alarm.signal_alarm.emit(thread_alarm.db.get_tasks())

>>>>>>> 6728bcf5d32f2f5a1539c3c4d5760f434ef7b9da
    sys.exit(app.exec())