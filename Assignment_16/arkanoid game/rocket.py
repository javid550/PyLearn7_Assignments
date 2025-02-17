import arcade

class Rocket(arcade.Sprite) :
    def __init__(self , w , n) :
        super().__init__("arkanoid game\pictures\Rocket.png")
        self.width = 80
        self.height = 30
        self.center_x = w // 2
        self.center_y = 70
        self.change_x = 0
        self.change_y = 0
        self.name = n
        self.speed = 8
        self.game_width = w


    def move(self) :
        if self.change_x == -1 :
            if self.center_x > 40 :
                self.center_x = self.center_x - self.speed
        elif self.change_x == 1 :
            if self.center_x < self.game_width - 40 :    
                self.center_x = self.center_x + self.speed

        # if self.me.width - 40 < x < self.width - 35 :
        #     self.me.center_x = x
        