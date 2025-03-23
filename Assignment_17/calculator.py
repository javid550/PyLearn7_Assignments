import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

app = QApplication([])

loader = QUiLoader()
main_window = loader.load("calculator\window.ui")
main_window.show()


def Ac() :
    main_window.txtbox.setText("")

def num(x) :
    main_window.txtbox.text()
    main_window.txtbox.setText(main_window.txtbox.text() + x)

def dot() :
    main_window.txtbox.setText(main_window.txtbox.setText.text() + ".")

def sum():
    global a , operator
    operator = "sum"
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")

def sub():
    global a , operator
    operator = "sub"
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")

def div() :
    global a , operator
    operator = "div"
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")

def mul() :
    global a , operator
    operator = "mul"
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")

def sqr() :
    a = float(main_window.txtbox.text())
    b = math.sqrt(a)
    main_window.txtbox.setText(str(b))

def sin() :
    a = float(main_window.txtbox.text())
    a = a / 180 * math.pi
    b =  math.sin(a)
    main_window.txtbox.setText(str(b))
    
def cos() :
    a = float(main_window.txtbox.text())
    a = a / 180 * math.pi
    b =  math.cos(a)
    main_window.txtbox.setText(str(b))

def tan() :
    a = float(main_window.txtbox.text())
    a = a / 180 * math.pi
    b =  math.tan(a)
    main_window.txtbox.setText(str(b))

def cot() :
    a = float(main_window.txtbox.text())
    a = a / 180 * math.pi
    b =  math.cot(a)
    b = 1 / a
    main_window.txtbox.setText(str(b))

def log() :
    a = float(main_window.txtbox.text())
    b =  math.log(a)
    main_window.txtbox.setText(str(b))

def per() :
    global percent
    percent = True

def minus() :
    global negative
    negative = True


def result() :
    b = float(main_window.txtbox.text())

    if operator == "sum" :
        if negative == True :
            c = a - b
        else :
            if percent == True :
                b = a * b / 100
                c = a + b
            else :
                c = a + b

    elif operator == "sub" :
        if negative == True :
            c = a + b
        else :
            if percent == True :
                b = a * b / 100
                c = a - b
            else :
                c = a - b

    elif operator == "div" :
        if percent == True :
            b = a * b / 100
            c = a / b
        else :
            c = a / b

    elif operator == "mul" :
        if percent == True :
            b = a * b / 100
            c = a * b
        else :
            c = a * b

    main_window.txtbox.setText(str(c))

# Numbers
main_window.AC.clicked.connect(Ac)
main_window.Button_0.clicked.connect(partial(num , "0"))
main_window.Button_1.clicked.connect(partial(num , "1"))
main_window.Button_2.clicked.connect(partial(num , "2"))
main_window.Button_3.clicked.connect(partial(num , "3"))
main_window.Button_4.clicked.connect(partial(num , "4"))
main_window.Button_5.clicked.connect(partial(num , "5"))
main_window.Button_6.clicked.connect(partial(num , "6"))
main_window.Button_7.clicked.connect(partial(num , "7"))
main_window.Button_8.clicked.connect(partial(num , "8"))
main_window.Button_9.clicked.connect(partial(num , "9"))
main_window.Button_dot.clicked.connect(partial(num , "."))

# Operators
negative = False
percent = False
main_window.Sum_Button.clicked.connect(sum)
main_window.Sub_Button.clicked.connect(sub)
main_window.Mul_Button.clicked.connect(mul)
main_window.Div_Button.clicked.connect(div)
main_window.Sin_Button.clicked.connect(sin)
main_window.Cos_Button.clicked.connect(cos)
main_window.Tan_Button.clicked.connect(tan)
main_window.Cot_Button.clicked.connect(cot)
main_window.Sqr_Button.clicked.connect(sqr)
main_window.Log_Button.clicked.connect(log)
main_window.minus_Button.clicked.connect(minus)
main_window.Equal_Button.clicked.connect(result)

app.exec()