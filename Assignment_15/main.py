import arcade
from fruit import Apple
from fruit import Pear
from fruit import Shit
from snake import Snake



class Game(arcade.Window) :
    def __init__(self) :
        super().__init__(width=500 , height=500 , title=" Snake_game 🐍 V.1 ")
        arcade.set_background_color(arcade.color.KHAKI)
        self.GameOver_background = arcade.load_texture("png\game over.png")
        self.GameOver = False
        self.score = 0
        self.apple = Apple(self)
        self.pear = Pear(self)
        self.shit = Shit(self)
        self.snake = Snake(self)
        # self.Run = True

        # self.food = []
        # self.food.extend([self.food_1 ,  self.food_2 ,  self.food_3])
        

    # def food(self) :
        # self.food.extend([Apple(self) , Pear(self) , Shit(self)])
        # /
        # self.food.append(Apple(self))
        # self.food.append(Pear(self))
        # self.food.append(Shit(self))


    def del_food(self) :
        del self.apple
        del self.pear
        del self.shit

        self.apple = Apple(self)
        self.pear = Pear(self)
        self.shit = Shit(self)



    def on_draw(self):
        arcade.start_render()

        if self.GameOver :
            arcade.set_background_color (arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured (0 , 0 , self.width , self.height , self.GameOver_background)
            # self.Run = False
            
        else :
            # for food in self.food :
            #     food.draw()
            self.apple.draw()
            self.pear.draw()
            self.shit.draw()

            self.snake.draw()

            arcade.draw_text(f"Score:{self.snake.score}" , self.width-120 , 15 , font_size=20 , color=arcade.color.RED)

        arcade.finish_render()



    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP :
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN :
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.LEFT :
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif symbol == arcade.key.RIGHT :
            self.snake.change_x = 1
            self.snake.change_y = 0



    def on_update(self, delta_time: float):

        if self.GameOver == False :
            self.snake.move()

        if (self.snake.center_x > self.width) or (self.snake.center_x < 0) or (self.snake.center_y > self.height) or (self.snake.center_y < 0) or (self.score < 0):
            self.GameOver = True

        for count , part in enumerate(self.snake.body) :
            for i in range (count+1 , len(self.snake.body)) :
                if part['x'] == self.snake.body[i]['x'] and part['y'] == self.snake.body[i]['y'] :
                    self.GameOver = True


        if  self.snake.score < 0 :
            self.GameOver = True

        
        if arcade.check_for_collision(self.snake , self.apple) :
            self.snake.score += 1
            self.del_food()
           

        if arcade.check_for_collision(self.snake , self.pear) :
            self.snake.score += 2
            self.del_food()


        if arcade.check_for_collision(self.snake , self.shit) :
            self.snake.score -= 1
            self.del_food()



if __name__ == "__main__" :
    game = Game()
    arcade.run()


 