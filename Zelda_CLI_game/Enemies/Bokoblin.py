'''
Ben Sehnert
##8/15/2018
##CS 172 Bokoblin class

Module Level Docstring

'''
#import ABC enemy
from Enemy import Enemy

class Bokoblin:
    '''Class Level Docstring:

    '''
    version = 2.0


    def __init__(self,name):
        self.name = name
        self.__health = 120
        self.defense_mode = True

    def __str__(self):
        return "a Bokoblin named {} is partying nearby".format(self.name)
    
    def get_health(self, numeric = False):
        '''returns a UI friendly health bar or
        purely numeric value depending on if
        numeric is overridden in runtime.'''
        if numeric: return int(self.__health)
        return "{} / 120".format(self.__health)
    
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
    from Moblin import Moblin
    print("Running in standby mode")
    B = Bokoblin('Dutch')
    M = Moblin('Gary')
    M.special_attack(B)
    M.basic_attack(B)
    print(B.get_health())