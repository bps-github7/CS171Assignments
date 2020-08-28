"""
Creator: Ben Sehnert
Date: 8/28/2020
Game: Chuchu class
Software: Zelda CLI mini-game

Module Level Docstring: 
Implements the Chuchu, the weakest and most common enemy
in the game.
"""

#imports the ABC this object overrides
from Enemy import Enemy

class Chuchu(Enemy):
    """
    Class Level Docstring:

    Purpose: creates the ChuChu monster,
    A gelatinous, amorphous ball of animosity and rebellion.
    It is the most common, easy to dispatch enemy in this game.
    """
    version = 2.0
    __name__ = "Chuchu"

    def __init__(self,name):
        """
    Constructs a Chuchu monster

    name : str - Gives the chuchu a nickname.
        """
        self.name = name
        self.__health = 80
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
        """returns the monster nickname."""
        return self.name
    
    def get_description(self):
        return "A gelatinous, colorful Chuchu"

    def basic_attack(self, enemy):
        """
        enemy : Hero object
        
        Does a very small amount of damage to enemy
        Sets defense mode to False.
        """
        self.defense_mode = False, enemy.do_damage(12)
    
    def basic_name(self):
        """Returns the name of monsters' basic attack"""
        return "pounce"
    
    def defense_attack(self, enemy):
        '''Does not do anything with defense mode
        because te Chuchu is weakest enemy.
        '''
        self.defense_mode = True

    def defense_name(self):
        return "lurch"

    def special_attack(self, enemy):
        self.defense_mode = False
        enemy.do_damage(25)

    def special_name(self):
        return "dangerously high bounce!"

    def do_damage(self, damage):
        if self.defense_mode:
            self.__health -= damage // 2
        else:
            self.__health -= damage
    
    def reset_health(self):
        self.__health = 80

if __name__ == "__main__":
    C = Chuchu('Barney')
    print("Running in standby mode")
    C.defense_name()