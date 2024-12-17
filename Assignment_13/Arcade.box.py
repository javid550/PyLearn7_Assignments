import arcade 

Column_spacing = 20
Row_specing = 20
left_margin = 110
right_margin = 110

arcade.open_window(400,400,"Square Whit Lozenges")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()


for row in range(10):
    for column in range(10):
        x = column * Column_spacing + left_margin
        y = row * Row_specing + right_margin

        if row % 2 == 0 and column % 2 == 0 or row % 2 != 0 and column % 2 != 0 :
            arcade.draw_rectangle_filled( x , y , 9 , 9 , arcade.color.BLUE , 45 )

        else :
            arcade.draw_rectangle_filled( x , y , 9 , 9 , arcade.color.RED , 45 )


arcade.finish_render()

arcade.run()