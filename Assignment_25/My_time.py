<<<<<<< HEAD
from PySide6.QtWidgets import *

class MyTime :
    def __init__(self, h , m , s) :
        self.hour = h
        self.minute = m
        self.second = s

    def plus(self) :
        self.second += 1
        if self.second >= 60 :
            self.minute += 1
            self.second -= 60
        if self.minute >= 60 :
            self.hour += 1
            self.minute -= 60

    def minus(self) :

        if self.second == 0 and self.minute == 0 and self.second == 0 :
            return
        if self.second > 0 :
            self.second -= 1
        elif self.minute > 0 :
            self.minute -= 1
            self.second = 59
        elif self.hour > 0 :
                self.hour -= 1
                self.minute = 59
=======
from PySide6.QtWidgets import *

class MyTime :
    def __init__(self, h , m , s) :
        self.hour = h
        self.minute = m
        self.second = s

    def plus(self) :
        self.second += 1
        if self.second >= 60 :
            self.minute += 1
            self.second -= 60
        if self.minute >= 60 :
            self.hour += 1
            self.minute -= 60

    def minus(self) :

        if self.second == 0 and self.minute == 0 and self.second == 0 :
            return
        if self.second > 0 :
            self.second -= 1
        elif self.minute > 0 :
            self.minute -= 1
            self.second = 59
        elif self.hour > 0 :
                self.hour -= 1
                self.minute = 59
>>>>>>> 6728bcf5d32f2f5a1539c3c4d5760f434ef7b9da
                self.second = 59