import arcade
from game import constants
from game.ship import Ship

class Player_Test_Ship(Ship):
    # this is the testing player ship this is one of many ships the will be in the game
    def __init__(self):
        super().__init__("project\images\Galaga_ship.png")
        
        self.time_since_last_firing = 0.0 
        self._attack_speed = 0.5
        self._ship_speed = 250
        self._defence = 3
        self.right_movment = False
        self.left_movment = False
        

        
    def on_update(self, delta_time: 1 / 60):
        # Update this sprite. 
        if self.left < 0:
            self.left = 1

        if self.right > constants.SCREEN_WIDTH:
            self.right = constants.SCREEN_WIDTH - 1

        if self.right_movment == True:
            self.center_x += self._ship_speed * delta_time

        if self.left_movment == True:
            self.center_x -= self._ship_speed * delta_time

    


        
    def action(self, ship_action, status):
        # takes in input from the game and turns it into player actions
        if ship_action == "right":
            self.right_movment = status

        if ship_action == "left":
            self.left_movment = status

        if ship_action == "shoot":
            self.shooting = status
        

    