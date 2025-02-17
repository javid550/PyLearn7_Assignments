import arcade
from rocket import Rocket
from blocks import Block
from heart import Heart
from ball import Ball


class Game(arcade.Window) :
    def __init__(self) :
        super().__init__(width= 400 , height= 600 , title= "Arkanoid Game ⚾")
        self.background = arcade.load_texture("arkanoid game\pictures\Background.jpg")
        self.GameOver_background = arcade.load_texture("arkanoid game\pictures\Game_over.jpg")
        self.me = Rocket(self.width , "Javid")
        self.ball = Ball(self)
        self.mode = None
        self.score = 0

        self.heart_list = []
        self.heart_x = 15
        self.heart_number = 3
        for h in range(self.heart_number) :
            new_heart = Heart(self.heart_x)
            self.heart_list.append(new_heart)
            self.heart_x += 25

        self.color = [arcade.color.YELLOW , arcade.color.RED , arcade.color.GREEN , arcade.color.PURPLE , arcade.color.ORANGE]

        self.blocks = []
        self.x = 25
        self.y = 380
        for i in range(5) :
            for _ in range(10) :
                self.block = Block(self.x , self.y , self.color[i])
                self.blocks.append(self.block)
                self.x += 58
            self.y += 25
            self.x = 25

    
    def  on_draw(self):

        arcade.start_render()

        if self.mode == "Game_Over" :
            arcade.set_background_color (arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured (0 , 0 , self.width , self.height , self.GameOver_background)
            score_text = f" Your score : { self.score}"
            arcade.draw_text ( score_text , (self.width // 2) - 110 , 35 , arcade.color.WHITE_SMOKE , 25 )
            arcade.finish_render()

        else :
            arcade.set_background_color (arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured(0 , 0 , self.width , self.height , self.background)

            self.me.draw()
            self.ball.draw()

            for heart in self.heart_list :
                heart.draw()

            for block in self.blocks :
                block.draw()

            score_text = f" Score : {self.score}"
            arcade.draw_text ( score_text , self.width - 110 , 10 , arcade.color.FLORAL_WHITE , font_size= 15 )

    def on_key_press(self, symbol: int , modifiers: int) :
        if symbol == arcade.key.LEFT :
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT :
            self.me.change_x = 1

    def on_key_release(self, symbol: int, modifiers: int):

        self.me.change_x = 0 



    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) :
        if self.me.width - 40 < x < self.width - 40 :
            self.me.center_x = x


    def on_update(self, delta_time: float):

        self.me.move()
        self.ball.move()

        if arcade.check_for_collision(self.me , self.ball) :
            self.ball.change_y = 1
            
        if self.ball.center_x < 10 or self.ball.center_x > self.width - 10 :
            self.ball.change_x *= -1

        if self.ball.center_y > self.height - 10 :
            self.ball.change_y *= -1


        for count , block in enumerate(self.blocks):
            if arcade.check_for_collision(self.ball , block):
                self.ball.change_y *= -1
                self.ball.speed += 0.2 
                self.me.speed += 0.1
                self.score += 1
                del self.blocks[count] 

        
        if self.ball.center_y <= 0 and len(self.heart_list) > 0 :
            del self.ball
            self.ball = Ball(self)
            self.heart_list.pop(self.heart_number - 1)
            self.heart_number -= 1
            self.score -= 1

        if self.heart_number == 0 or self.score < 0 :
            self.mode = "Game_Over"



window = Game()

arcade.run() 
        