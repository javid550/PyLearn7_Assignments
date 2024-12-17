import arcade

class Spaceship(arcade.Sprite) :

    def __init__(self , game ) :
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = game.width // 2
        self.center_y = 80
        self.width = 48
        self.height = 48 

        self.speed = 10