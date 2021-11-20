import arcade 
from scripts.game import GameView
from scripts import constants

class Character_selection(arcade.View):
    def __init__(self):
        super().__init__()
        self.menu_Background = "spacegame\images\space.jpg"
        self.ship_number = 0
        self.ship_types = [arcade.color.BLUE,arcade.color.GREEN,arcade.color.RED,arcade.color.PURPLE]
    
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.WIDTH, constants.HEIGHT, arcade.load_texture("spacegame\images\space.jpg"))
        arcade.draw_rectangle_filled(constants.WIDTH // 2,constants.HEIGHT // 2, 100, 100, self.ship_types[self.ship_number]) # this code will change when real ships are added


    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.RIGHT:
            self.ship_number += 1
            self.ship_number = self.ship_number % len(self.ship_types)
        if key == arcade.key.LEFT:
            self.ship_number -= 1
            self.ship_number = self.ship_number % len(self.ship_types)
        if key == arcade.key.SPACE:
            # pass self, the current view, to preserve this view's state
            game = GameView()
            self.window.show_view(game)
