"""
Creator: Ben Sehnert
Date: 8/28/2020
Game: Moblin class
Software: Zelda CLI mini-game

Module Level Docstring: 
Implements Moblin-
The second most powerful foe.
a large pig-like beast that carries a lantern and large spear.
"""

#imports the ABC this object overrides
from Enemy import Enemy
import random

class Moblin(Enemy):
    """Class Level Docstring: 
    
    A Subclass of Enemy ABC which implements a medium powered foe.
    
    __init__(self, name) : Constructs a Moblin enemy.
    __str__(self) : return description + name
    get_health(self, numeric = False): returns foe health as string or int
    get_name(self): Returns foe name.
    get_description(self): Returns foe description.
    basic_attack(self, enemy): Sets defense_mode to false, deals damage to enemy. 
    basic_name(self): Returns name of basic attack.
    defesnse_attack(self, enemy): Like Basic attack but switches defense mode and does less damage.
    defense_name(self): Returns name of defense attack.
    special_attack(self, enemy): Sets defense to true and deals decent damage.
    special_name(self): Returns name of special attack.
    do_damage(self, other): Private method for dealing damage to self.
    reset_health(self): Applies full recovery- returns health to maxium.
    """

    version = 2.0

    def __init__(self,name):
        """
        Constructs a Moblin object

        name : str - provides a nickname
        """
        self.__name__ = "Moblin"
        self.name = name
        self.__health = 300
        self.defense_mode = True

    def __str__(self):
        return "{} named {} is attacking ".format(self.get_description(), self.get_name())
    
    def get_health(self, numeric = False):
        """returns foes' current health
        
        numeric = False - default : return UI oriented string (CHP/HP)
        numeric = True - returns health of foe, cast to integer
        """
        return int(self.__health) if numeric else "{} / 300".format(self.__health) 

    
    def get_name(self):
        """Returns foe name."""
        return self.name    
    
    def get_description(self):
        """Returns foe desription."""
        return "a huge, pig-like beast that carries a lantern and large spear."
    
    def basic_attack(self, enemy):
        """Sets defense_mode to false, deals damage to enemy.
        
        enemy : Hero object
        """
        #cant defend while using basic attack
        self.defense_mode = False
        enemy.do_damage(20)
    
    def basic_name(self):
        """Returns name of basic attack."""
        return random.choice(("Kick", "punch", "spear-jab",
        "devestating roar", "angry-stomp", "ferocious slice"))
    
    def defense_attack(self, enemy):
        """Like basic attack but switches
        defense mode and does less damage.
        
        enemy : Hero object
        """
        self.defense_mode = True
        enemy.do_damage(10)
    
    def defense_name(self):
        """Returns name of defense attack."""
        return "waves his lantern in defense!"
    
    def special_attack(self, enemy):
        """Sets defense to true and deals decent amount of damage.
        
        enemy : Hero object
        """
        self.defense_mode = True
        enemy.do_damage(45)
    
    def special_name(self):
        '''Returns name of special attack.'''
        return "belch-roar-jab-strike!"
    
    def do_damage(self, damage):
        """Private method for dealing damage to self."""    
        if self.defense_mode:
            self.__health -= damage // 2
        else:
            self.__health -= damage
    
    def reset_health(self):
        """Applies full recovery - returning health to maximum."""
        self.__health = 300

if __name__ == "__main__":
    print("{} class: running in standby mode".format(Moblin.__name__))
