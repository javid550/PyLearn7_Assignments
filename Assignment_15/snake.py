import arcade


class Snake(arcade.Sprite) :
    def __init__(self , game) :
        super().__init__()
        self.width = 30
        self.height = 30
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = 0
        self.change_y = 0
        self.speed = 3
        self.score = 0
        self.body = []
        self.color = arcade.color.GREEN
        self.color1 = arcade.color.RED
        

    def draw(self) :
        arcade.draw_circle_filled(self.center_x , self.center_y , self.height / 2 , self.color)

        for count , part in enumerate (self.body) :
            # part = self.body[i]
            if count % 2 == 0 :
                arcade.draw_circle_filled(part['x'] , part['y'] , self.height // 2 , self.color )
            else :
                arcade.draw_circle_filled(part['x'] , part['y'] , self.height // 2 , self.color1 )
    


    def eat(self , food) :
        self.score += food.score
        del food
        # return self.score

    
    def move(self) :
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        self.body.append({'x':self.center_x , 'y':self.center_y})

        if len(self.body) > self.score :
            self.body.pop(0)


    # def move_AI(self , center_x , center_y) :
    #     self.body.append({'x':self.center_x , 'y':self.center_y})

    #     if len(self.body) > self.score :
    #         self.body.pop(0)

    #     if self.center_y > center_y :
    #         self.center_y -= self.speed
        
        

