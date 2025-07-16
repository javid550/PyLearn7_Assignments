import arcade

class Heart (arcade.Sprite) :

    def __init__(self , x) :
        super().__init__("Space_Shooter\heart.png")
        self.width = 22
        self.height = 22
        self.center_x = x
        self.center_y = 20
