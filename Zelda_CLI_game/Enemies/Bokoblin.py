"""
Creator: Ben Sehnert
Date: 8/28/2020
Game: Bokoblin class
Software: Zelda CLI mini-game

Module Level Docstring: 
Implements the Bokoblin-
the second weakest, more common enemy
"""

#imports the ABC this object overrides
from Enemy import Enemy

class Bokoblin:
    '''Class Level Docstring:

    '''
    version = 2.0


    def __init__(self,name):
        self.__name__ = "Bokoblin"
        self.name = name
        self.__health = 120
        self.defense_mode = True

    def __str__(self):
        return "{} named {} is attacking ".format(self.get_description(), self.get_name())
    
    def get_health(self, numeric = False):
        """returns foes' current health
        
        numeric = False - default : return UI oriented string (CHP/HP)
        numeric = True - returns health of foe, cast to integer
        """
        return int(self.__health) if numeric else "{} / 80".format(self.__health) 


    def get_name(self):
        return self.name
    
    def get_description(self):
        return "A meager Bokoblin with a sword and shield.\n\
            You can overpower it if you are sneaky"

    def basic_attack(self, enemy):
        self.defense_mode = False
        enemy.do_damage(25)
    
    def basic_name(self):
        return "slice"
    
    def defense_attack(self, enemy):
        self.defense_mode = True
        enemy.do_damage(30)

    def defense_name(self):
        return "jump smash!"
        

    def special_attack(self, enemy):
        self.defense_mode = False
        enemy.do_damage(50)

    def special_name(self):
        return "poison bite"

    def do_damage(self, damage):
        '''blocks opponent attack if defense mode is true'''
        if self.defense_mode:
                self.__health -= damage // 2
        else:
            self.__health -= damage
    
    def reset_health(self):
        self.__health = 120

if __name__ == "__main__":
    print("Running in standby mode")
