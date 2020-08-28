"""
Creator: Ben Sehnert
Date: 8/28/2020
Game: Moblin class
Software: Zelda CLI mini-game

Module Level Docstring: 
Implements the Moblin-
second most powerful foe.
"""

#imports the ABC this object overrides
from Enemy import Enemy

class Moblin(Enemy):
    """
    Class level Docstring:


    """
    version = 2.0

    def __init__(self,name):
        """
        Constructs a Moblin

        name : str - provides a nickname
        """
        self.__name__ = "Moblin"
        self.name = name
        self.__health = 160
        self.defense_mode = True

    def __str__(self):
        return "{} named {} is attacking ".format(self.get_description(), self.get_name())
    
    def get_health(self, numeric = False):
        """returns foes' current health
        
        numeric = False - default : return UI oriented string (CHP/HP)
        numeric = True - returns health of foe, cast to integer
        """
        return int(self.__health) if numeric else "{} / 80".format(self.__health) 

    
    def get_name(self):#returns name
        return self.name    
    
    def get_description(self):#returns description
        return "A big, ugly moblin with a pointy snout.\n\
        \r\rBe careful: he is powerful and tough."
    
    def basic_attack(self, enemy):
        '''the most common enemy attack.
        sets d_mode false'''
        #cant defend while using basic attack
        self.defense_mode = False
        enemy.do_damage(20)
    
    def basic_name(self):
        return "Kick"
    
    def defense_attack(self, enemy):#defense attack
        self.defense_mode = True
        enemy.do_damage(10)
    
    def defense_name(self):#defense name
        return "waves his lantern in defense!"
    
    def special_attack(self, enemy):
        self.defense_mode = True
        enemy.do_damage(45)
    
    def special_name(self):
        '''returns name of special attack'''
        return "belch-roar-jab-strike!"
    
    def do_damage(self, damage):    
        if self.defense_mode:
            self.__health -= damage - 10
        else:
            self.__health -= damage
    
    def reset_health(self):
        self.__health = 160

if __name__ == "__main__":
    print("Running in standby mode")
    M = Moblin('Thornicus')
    print(M.get_description())