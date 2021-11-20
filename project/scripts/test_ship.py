from scripts.player_ship import Player_Ship
import arcade
from scripts import constants

class Test_Ship(Player_Ship):

    def __init__(self):
        super().__init__()
        self.sprit =  "project\images\\test_ship.png"