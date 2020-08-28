'''
Module Level Docstring:
Ben Sehnert
Chuchu class for Zelda CLI Mini-game
8/15/2018

Module Level Docstring

'''
from Enemy import Enemy

class Chuchu:
    '''Class Level Docstring:
    Creates the ChuChu monster,
    the most convenient and common enemy.
    '''
    version = 2.0

    def __init__(self,name):
        self.__name__ = "Chuchu"
        self.name = name
        self.__health = 80
        self.defense_mode = True

    def __str__(self):
        return "a young Chuchu named {} is chuggin' away nearby".format(self.name)
    
    def get_health(self, numeric = False):
        '''returns a UI friendly health bar or
        purely numeric value depending on if
        numeric is overridden in runtime.'''
        if numeric: return int(self.__health)
        return "{} / 80".format(self.__health)
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return "A gelatinous, colorful Chu lurches forward"

    def basic_attack(self, enemy):
        self.defense_mode = False
        enemy.do_damage(12)
    
    def basic_name(self):
        return "pounce"
    
    def defense_attack(self, enemy):
        '''Does not do anything with defense mode
        because te Chuchu is weakest enemy.
        '''
        enemy.do_damage(5)

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
    print("Running in standby mode")