import random
import arcade


class Ball(arcade.Sprite) :
    def __init__(self , game) :
        super().__init__()
        self.color = arcade.color.YELLOW
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = random.choice([-1 , 1])
        self.change_y = random.choice([-1 , 1])
        self.radians = 15 # 15*2=30
        self.width = self.radians * 2
        self.height = self.radians * 2 
        self.speed = 5

    def move(self) :
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self) :
        arcade.draw_circle_filled(self.center_x , self.center_y , self.radians , self.color)
        
