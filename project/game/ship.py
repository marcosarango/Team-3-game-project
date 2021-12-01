import arcade

from game.entity import Entity
from game import constants

class Ship(Entity):
    # a sub class of entity that helps make ship type objects
    def __init__(self, texture):
        super().__init__(texture, scale= constants.SHIP_SPRITE_SCALING)

        self._ship_texture = texture
        self._attack_speed = 5
        self._ship_speed = 150
        self._defence = 3
        self.ship_scale = 0.5

    def get_speed(self):
        # returns the ships speed
        return self._ship_speed

    def get_defence(self):
        # returns the ships defence
        return self._defence

    def get_attack_speed(self):
        # returns the ships attack speed
        return self._attack_speed
    
    def get_texture(self):
        # returns the texture of the ship
        return self._ship_texture