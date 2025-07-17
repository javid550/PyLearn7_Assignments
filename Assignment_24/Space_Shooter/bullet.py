<<<<<<< HEAD
import arcade

class Bullet(arcade.Sprite) :
    
    def __init__(self , owner) :
        super().__init__(":resources:images/space_shooter/LaserRed01.png")
        self.center_x = owner.center_x
        self.center_y = owner.center_y
        self.speed = 3
        self.change_x = 0
        self.change_y = 1

    def move(self):
=======
import arcade

class Bullet(arcade.Sprite) :
    
    def __init__(self , owner) :
        super().__init__(":resources:images/space_shooter/LaserRed01.png")
        self.center_x = owner.center_x
        self.center_y = owner.center_y
        self.speed = 3
        self.change_x = 0
        self.change_y = 1

    def move(self):
>>>>>>> 6728bcf5d32f2f5a1539c3c4d5760f434ef7b9da
        self.center_y += self.speed