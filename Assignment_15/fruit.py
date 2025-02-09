import random 
import arcade


class Fruit(arcade.Sprite) :
    def __init__(self,game):
        super().__init__(game)
        self.width = 28
        self.height = 28
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
        self.score = 0


class Apple(Fruit) :
    def __init__(self , game) :
        super().__init__("png\Apple.png")
        self.width = 28
        self.height = 28
        self.center_x = random.randint(10 , game.width-10)
        self.center_y = random.randint(10 , game.height-10)
        self.change_x = 0
        self.change_y = 0
        self.score = 1


class Pear(Fruit) :
    def __init__(self , game) :
        super().__init__("png/Pear.png")
        self.width = 28
        self.height = 28
        self.center_x = random.randint(10 , game.width-10)
        self.center_y = random.randint(10 , game.height-10)
        self.change_x = 0
        self.change_y = 0
        self.score = 2


class Shit(Fruit) :
    def __init__(self , game) :
        super().__init__("png/Shit.png")
        self.width = 35
        self.height = 35
        self.center_x = random.randint(10 , game.width-10)
        self.center_y = random.randint(10 , game.height-10)
        self.change_x = 0
        self.change_y = 0
        self.score = -1
