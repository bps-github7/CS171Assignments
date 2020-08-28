"""
Creator: Ben Sehnert
Date: 8/28/2020
Game: Chuchu class
Software: Zelda CLI mini-game

Module Level Docstring: 
Implements the Chuchu, the weakest and most common enemy
in the game- a squishy, gelatinous ball of energy and danger
"""

#imports the ABC this object overrides
from Enemy import Enemy

class Chuchu(Enemy):
    """Class Level Docstring: 
    
    A Subclass of Enemy ABC which implements a powerful foe.
    
    __init__(self, name) : Constructs a Darknut enemy.
    __str__(self) : Return description + name.
    get_health(self): Returns foe health.
    get_name(self): Returns foe name.
    get_description(self): Returns foe description.
    basic_attack(self, enemy): Does a very small amount of damage to enemy.
    basic_name(self): Returns name of basic attack.
    defesnse_attack(self, enemy): Does not do anything with defense mode because Chuchu is weakest enemy.
    defense_name(self): Returns name of defense attack.
    special_attack(self, enemy): Sets defense to false and does damage to opponent.
    special_name(self): Returns name of special attack.
    do_damage(self, other): Private method for applying damage to this enemy.
    reset_health(self): Applies full recovery- health returned to max.
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
        """Returns the foe description."""
        return "a squishy, gelatinous ball of energy and danger"

    def basic_attack(self, enemy):
        """
        Does a very small amount of damage to enemy,
        Sets defense mode to False.
        
        enemy : Hero object
        """
        self.defense_mode = False
        enemy.do_damage(12)
    
    def basic_name(self):
        """Returns the name of basic attack."""
        return "pounce"
    
    def defense_attack(self, enemy):
        """Does not do anything with defense mode because Chuchu is weakest enemy."""
        self.defense_mode = True

    def defense_name(self):
        """Returns name of defense attack."""
        return random.choice(("lurch", "slop", "splash", "pass"))

    def special_attack(self, enemy):
        """Sets defense to false and does damage to opponent."""
        self.defense_mode = False
        enemy.do_damage(25)

    def special_name(self):
        """Returns name of special attack."""
        return "dangerously high bounce!"

    def do_damage(self, damage):
        """Private method for applying damage to self."""
        if self.defense_mode:
            self.__health -= damage // 2
        else:
            self.__health -= damage
    
    def reset_health(self):
        """Applies full recovery- health returned to max."""
        self.__health = 80

if __name__ == "__main__":
    print("{} class: running in standby mode.".format(Chuchu.__name__))