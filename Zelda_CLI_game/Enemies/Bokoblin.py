"""
Creator: Ben Sehnert
Date: 8/28/2020
Game: Bokoblin class
Software: Zelda CLI mini-game

Module Level Docstring: 
Implements the Bokoblin-
the second weakest, more common enemy
a smaller blue pig-like beast which carries a wooden whacking-stick (a stick for whacking things with.)
"""

#imports the ABC this object overrides
from Enemy import Enemy

class Bokoblin:
    """Class Level Docstring: 
    
    A Subclass of Enemy ABC which implements the second weakest foe.
    
    __init__(self, name) : Constructs a Bokoblin object.
    __str__(self) : Returns description + name.
    get_health(self, numeric = False): Returns foe health as string or int.
    get_name(self): Returns foe name.
    get_description(self): Returns foe description.
    basic_attack(self, enemy): Makes self vulreble while dealing decent amount of damage.
    basic_name(self): Returns name of basic attack.
    defense_attack(self, enemy): Returns name of defense attack.
    defense_name(self): Makes defense mode true and deals considerable damage.
    special_attack(self, enemy): Returns name of special attack.
    special_name(self): Makes self vulnerable while dealing high amount of damage.
    do_damage(self, other): Private method for applying damage to self.
    reset_health(self): Applies full recovery - returns health to maximum.
    """
    __name__ = "Bokoblin"
    version = 2.0


    def __init__(self,name):
        """
        Constructs a Bokoblin object

        name : str - provides foe with nickname.
        """
        self.name = name
        self.__health = 120
        self.defense_mode = True

    def __str__(self):
        return "{} named {} is attacking ".format(self.get_description(), self.get_name())
    
    def get_health(self, numeric = False):
        """returns foe current health
        
        numeric = False - default : return UI oriented string (CHP/HP)
        numeric = True - returns health of foe, cast to integer
        """
        return int(self.__health) if numeric else "{} / 80".format(self.__health) 


    def get_name(self):
        """Returns foe name."""
        return self.name
    
    def get_description(self):
        """Returns foe description."""
        return "A meager Bokoblin \n\
        \r\ra small, blue, pig-like beast which carries a\n\
        \r\rwooden whacking-stick (a stick for whacking things with.)"

    def basic_attack(self, enemy):
        """Makes self vulreble while dealing decent amount of damage.
        
        enemy : Hero object
        """
        self.defense_mode = False
        enemy.do_damage(25)
    
    def basic_name(self):
        """Returns name of basic attack."""
        return "slice"
    
    def defense_attack(self, enemy):
        """Makes defense true and applies considerable damage
        
        enemy : Hero object
        """
        self.defense_mode = True
        enemy.do_damage(35)

    def defense_name(self):
        """Returns name of defense attack."""
        return "jump smash!"
        

    def special_attack(self, enemy):
        """"makes self vulreble and deals high amount of damage."""
        self.defense_mode = False
        enemy.do_damage(50)

    def special_name(self):
        """Returns name of special attack."""
        return "poison bite"

    def do_damage(self, damage):
        '''Private method for applying damage to self.'''
        if self.defense_mode:
                self.__health -= damage // 2
        else:
            self.__health -= damage
    
    def reset_health(self):
        """Applies full recovery - returns health to maximum."""
        self.__health = 120

if __name__ == "__main__":
    print("{} class: running in standby mode".format(Bokoblin.__name__))
