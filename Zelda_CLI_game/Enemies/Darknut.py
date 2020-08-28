'''
Ben Sehnert
start: 8/15/2018
finish: 8/13/2020
Darknut class

Module Level Docstring: 
Implements the Darknut-
The strongest, most dangerous foe
in the game.
'''
from Enemy import Enemy

class Darknut(Enemy):
    '''Class Level Docstring:
    to make the foe threatening we gave them 500 HP and
    methods that assure defense_mode stays active throughout play.
    '''
    version = 2.0
    def __init__(self,name):
        self.__name__ = "Darknut"
        self.name = name
        self.__health = 200
        self.defense_mode = True

    def __str__(self):
        return "a Darknut named {} is attacking ".format(self.name)
    
    def get_health(self, numeric = False):
        '''returns a UI friendly health bar or
        purely numeric value depending on if
        numeric is overridden in runtime.'''
        if numeric: return int(self.__health)
        return "{} / 200".format(self.__health)
    
    def get_name(self):
        '''returns the name.'''
        return self.name
    
    def get_description(self):
        '''returns the description'''
        return "Darknut clad in heavy duty armor\nHe towers over you."

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