<<<<<<< HEAD
import random
import arcade


class Enemy(arcade.Sprite) :

    def __init__ (self , game , speed) :
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0 , game.width)
        self.center_y = game.height
        self.width = 48
        self.height = 48 
        self.angle = 180
        self.speed = speed
        self.change_x = 0
        self.change_y = -1

    def move(self) :
        self.center_y -= self.speed
=======
import random
import arcade


class Enemy(arcade.Sprite) :

    def __init__ (self , game , speed) :
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0 , game.width)
        self.center_y = game.height
        self.width = 48
        self.height = 48 
        self.angle = 180
        self.speed = speed
        self.change_x = 0
        self.change_y = -1

    def move(self) :
        self.center_y -= self.speed
>>>>>>> 6728bcf5d32f2f5a1539c3c4d5760f434ef7b9da
