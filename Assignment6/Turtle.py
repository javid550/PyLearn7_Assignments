from turtle import Turtle

tur = Turtle()
tur.shape('turtle')
tur.speed(1)
x = 25
y = -15
tur.penup()
tur.goto(x,y)
tur.pendown()
for i in range(10) :
    for j in range(i+3) :
        tur.left(360/(i+3))
        tur.forward(50)
    x += 0.3
    y -= 8
    tur.penup()
    tur.goto(x,y)
    tur.pendown()