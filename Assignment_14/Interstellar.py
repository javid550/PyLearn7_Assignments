import time
import arcade
from spaceship import Spaceship
from heart import Heart
from enemy import Enemy

class Game(arcade.Window) :

    def __init__(self) :
        super().__init__(width=600 , height=600 , title="Spaceship Game 🚀 ")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.GameOver_background = arcade.load_texture("session 14\game over.png")

        self.me = Spaceship(self.width , "Javid")

        self.enemies = []
        self.enemy_speed = 3
        self.timer = time.time()

        self.scoreboard = 0

        self.mode = None

        self.heart_list = []
        self.heart_x = 15
        self.heart_number = 3
        for h in range(self.heart_number) :
            new_heart = Heart(self.heart_x)
            self.heart_list.append(new_heart)
            self.heart_x += 25

        self.shot_voice = arcade.load_sound(":resources:sounds/laser2.wav")
        self.burst_voice = arcade.load_sound(":resources:sounds/gameover3.wav")

        


    # display
    def  on_draw(self):

        arcade.start_render()

        if self.mode == "Game_Over" :
            arcade.set_background_color (arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured (0 , 0 , self.width , self.height , self.GameOver_background)
            score_text = f" Your score : { self.scoreboard}"
            arcade.draw_text ( score_text , (self.width // 2) - 110 , 35 , arcade.color.WHITE_SMOKE , 25 )
            arcade.finish_render()

        else :
            arcade.set_background_color (arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured(0 , 0 , self.width , self.height , self.background)

            self.me.draw()

            for enemy in self.enemies :
                enemy.draw()

            for bullet in self.me.bullet_list :
                bullet.draw()

            for heart in self.heart_list :
                heart.draw()

            score_text = f" Score : {self.scoreboard}"
            arcade.draw_text ( score_text , self.width - 130 , 12 , arcade.color.WHITE )

    def on_key_press(self, symbol: int, modifiers: int):
        # print("one key pressed")
        # print(symbol)
        # print("arcade.key.LEFT") => 97
        # print("arcade.key.RIGHT") => 100
        
        if symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D :
            self.me.change_x = 1
        elif symbol == arcade.key.UP or symbol == arcade.key.SPACE :
            self.me.fire()
            arcade.play_sound( self.shot_voice )


    def on_key_release(self, symbol: int, modifiers: int):

        self.me.change_x = 0 


    # A function that run automaticly 
    # logic
    def on_update(self, delta_time: float):

        self.me.move()

        for enemy in self.enemies :
            enemy.move()
        
        for bullet in self.me.bullet_list :
            bullet.move()

        for enemy in self.enemies :
            if enemy.center_y <= 0 and len(self.heart_list) > 0 :
                self.enemies.remove(enemy)
                self.heart_list.pop(self.heart_number - 1)
                self.heart_number -= 1

        for bullet in self.me.bullet_list :
            if bullet.center_y >= self.height :
                self.me.bullet_list.remove(bullet)

        if time.time() >= self.timer + 3 :
            new_enemy = Enemy (self , self.enemy_speed)
            self.enemies.append(new_enemy)
            self.enemy_speed += 0.1
            self.timer = time.time()

        if self.heart_number == 0 :
            self.mode = "Game_Over"


        for enemy in self.enemies :
            if arcade.check_for_collision(self.me , enemy) :
                self.mode = "Game_Over"

        for enemy in self.enemies :
            for bullet in self.me.bullet_list :
                if arcade.check_for_collision(enemy , bullet) :
                    self.enemies.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    arcade.play_sound(self.burst_voice)
                    self.scoreboard += 1


window = Game()

arcade.run() 
