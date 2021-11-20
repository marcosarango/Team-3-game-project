import arcade
from scripts import constants
from scripts.game import GameView
from scripts.character_selection import Character_selection


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.play_button = False
        self.menu_Background = "project\images\menu_background.jpg"
        self.Play_Button = "project\images\playbutton.png"
        self.play_hover = False

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, constants.WIDTH, constants.HEIGHT, arcade.load_texture(self.menu_Background))
        arcade.draw_texture_rectangle(constants.WIDTH // 2, 600, 200, 100, arcade.load_texture(self.Play_Button))
            
        if self.play_hover == True:
            arcade.draw_rectangle_outline(constants.WIDTH // 2, 600, 200, 100, arcade.color.GRAY, 3)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _button == arcade.MOUSE_BUTTON_LEFT:
            if _x >= constants.WIDTH // 2 - 100 and _x <= constants.WIDTH // 2 + 100 and _y <= 650 and _y >= 550:
                    character_selection = Character_selection()
                    self.window.show_view(character_selection)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if x >= constants.WIDTH // 2 - 100 and x <= constants.WIDTH // 2 + 100 and y <= 650 and y >= 550:
            self.play_hover = True

        else:
            self.play_hover = False

