import random
import arcade
from spaceship import Spaceship


class Enemy(arcade.Sprite) :
    def __init__ (self , w , h) :
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0 , w)
        self.center_y = h + 24
        self.width = 48
        self.height = 48 
        self.angle = 180
        self.speed = 1


class Game(arcade.Window) :

    def __init__(self) :
        super().__init__(width=600 , height=600 , title="Spaceship Game 🚀 ")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)
        self.enemy = Enemy(self.width , self.height)

    # display
    def  on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0 , 0 , self.width , self.height , self.background)

        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        # print("one key pressed")
        # print(symbol)
        
        if symbol == 97 : # Left
            self.me.center_x -= self.me.speed
        elif symbol == 100 : # Right
            self.me.center_x += self.me.speed


    # A function that run automaticly 
    def on_update(self, delta_time: float):
        self.enemy.center_y -= self.enemy.speed
        



window = Game()

arcade.run() 