"""
Creator: Ben Sehnert
Date: 8/28/2020
Game: Darknut class
Software: Zelda CLI mini-game

Module Level Docstring: 
Implements the Darknut-
The strongest, most dangerous foe
in the game.
"""
#imports the ABC this object overrides
from Enemy import Enemy

class Darknut(Enemy):
    """Class Level Docstring: 
    
    A Subclass of Enemy ABC which implements a powerful foe.
    
    __init__(self, name) : constructs a Darknut enemy
    __str__(self) : return description + name
    
    """
    version = 2.0
    def __init__(self,name):
        """
    Constructs a Darknut.

    name : str - provides a nickname for the monster.
        """
        self.__name__ = "Darknut"
        self.name = name
        self.__health = 200
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
        """Returns foe name."""
        return self.name
    
    def get_description(self):
        """Returns foes description"""
        return "Darknut clad in armor head to toe."

    def basic_attack(self, enemy):
        '''consistent relative to every other enemy attack.'''
        self.defense_mode = True
        enemy.do_damage(25)
    
    def basic_name(self):
        '''returns name of basic attack
        '''
        return "JUDO CHOP"
    
    def defense_attack(self, enemy):
        '''deals considerable damage. Always makes d_mode true     
        '''
        self.defense_mode = True
        enemy.do_damage(30)


    def defense_name(self):
        return "Supa Dupa Dodge"

    def special_attack(self, enemy):
        if self.defense_mode:
            self.__health -= 20
            enemy.do_damage(50)
        else:
            self.__health -= 50
            enemy.do_damage(70)
    
    def special_name(self):
        ''' '''
        return "haymaker"

    def do_damage(self, damage):
        if self.defense_mode:
            self.__health -= damage - 20
        else:
            self.__health -= damage
    
    def reset_health(self):
        self.__health = 200

if __name__ == "__main__":
    D = Darknut("Samuel L. Jackson")
    print(D.special_name())