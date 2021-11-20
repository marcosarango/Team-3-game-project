import arcade 
from scripts.game import GameView
from scripts import constants
from scripts.test_ship import Test_Ship

class Character_selection(arcade.View):
    def __init__(self):
        super().__init__()
        self.menu_Background = "project\images\menu_background.jpg"
        self.ship_number = 0
        self.test_ship = Test_Ship()
        self.ship_list = [Test_Ship()]
        self.ship_types = [self.test_ship.get_sprit()]
    
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.WIDTH, constants.HEIGHT, arcade.load_texture("project\images\menu_background.jpg"))
        arcade.draw_texture_rectangle(constants.WIDTH // 2, 600, 200, 100, arcade.load_texture(self.ship_types[self.ship_number])) # this code will change when real ships are added
        


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
            game = GameView(self.ship_list[self.ship_number])
            self.window.show_view(game)
