'''
Programmer: Ben Sehnert
Program: Hero Class
Date: 8/15/2018
Software: Zelda CLI mini game

Module Level Docstring: Implements a Hero class which 
creates the playable character in the cmd line game.
'''
import random
import sys
from Enemies.Enemy import Enemy

class Hero(Enemy):
    '''Class Level Docstring: Hero Object has six attributes,
    most of which are nessecary for gameplay mechanisms.

    Name is purely descriptive (no impact on game implementation details)
    Therefore, name is the only mutable value, able to be set via constructor.
    '''
    version = 2.0

    def __init__(self,name = "Link"):
        self.name = name
        self.__health = 200
        self.defense_mode = False
        self.bombs = 20
        self.elixers = 5
        self.arrows = 10
    
    def __str__(self):
        '''Returns Hero attributes. 
    (health and defense_mode are implementation details)'''
        return "Health: {} / 200\n\
    \r\rBombs: {} / 20\n\
    \r\rElixers: {} / 6\n\
    \r\rArrows: {} / 10".format(self.__health, self.bombs,
    self.elixers, self.arrows)

    def get_name(self):
        return self.name
    
    def get_description(self):
        return "{}\na young warrior - clad in green".format(self.name)
    
    
    def get_health(self, numeric = False):
        if numeric: return int(self.__health)
        return "{} / 200".format(self.__health)
    
    def basic_attack(self, enemy):
        '''Offensive attack that leaves Hero vulnerable.'''
        self.defense_mode = False
        enemy.do_damage(random.randint(40, 70))
    
    def basic_name(self):
        '''Provides name for Hero basic attack.'''
        return random.choice(("vertical slash", "horizontal slash",
        "thrust", "spin attack", "parry attack", "jump attack",
        "mortal blow", "back slice", "helm splitter","great spin",
        "huricane spin"))
    
    def defense_attack(self, enemy):
        '''Parry attack that bolsters hero defense
        while also doing very small amount of damage to enemy.'''        
        self.defense_mode = True
        enemy.do_damage(random.randint(2,12))
    
    def defense_name(self):
        '''Returns the name for Hero defense attack'''
        return random.choice(("shield parry strike", "weasel artilleru dodge",
        "straif left", "straif right", "straif back", "shield strike"))
    
    def special_attack(self, enemy):
        '''A Powerful attack that does higher amount of damage 
    and also swaps defense mode. If defense mode is true
    does the standard amount of damage. If false, does 
    greater damage but also hurts the Hero.
        '''
        if self.bombs:
            if self.defense_mode:
                self.defense_mode = False
                enemy.do_damage(55)
                return "The bomb had a direct Hit.\nYour enemy recoils"
            else:
                self.defense_mode = True
                enemy.do_damage(75)
                self.__health -= 20
                return "The bomb was very powerful.\n\
            \r\rYour enemy was badly injured,\n\
            \r\rbut you were damaged as well by the shrapnel"
        else:
            return "No bombs remaining.\nCannot use Special attack."

    def special_name(self):
        '''Returns the name of the special attack.'''
        return "a bomb"
    
    def use_arrow(self, enemy):
        '''Projectile attack:
        highly effective, has no effect on defense mode.
        but limited availability/ uses- 10 available arrows per game.'''        
        enemy.do_damage(95)
        self.arrows -= 1
    
    def arrow_name(self):
        '''Returns the name of arrow attack.'''
        return "{} fired an arrow".format(self.name)
    
    def arrow_count(self):
        '''Returns the number of arrows remaining vs. maximum.'''
        return "{} / 10".format(self.arrows)
    
    def elixer(self):
        '''Replenishes half of the Heros max health point.
    but limited uses, also turns defense mode to false.
        '''
        self.defense_mode = False
        self.__health + 100
        self.elixers - 1
    
    def elixer_name(self):
        '''Returns the name of the elixer move.'''
        return "{} drank an elixer".format(self.name)
    
    def elixer_count(self):
        '''Returns the amount of remaining elixers vs max elixers.'''
        return "{} / 5".format(self.elixers)

    def do_damage(self, damage):
        '''Blocks attack if defense mode is true'''
        if self.defense_mode:
            return True
        else:
            self.__health -= damage
    
    def reset_health(self):
        '''Sets the health points of Hero to maximum.'''
        self.__health = 200

    def reset_ammo(self):
        '''Sets all the munititions to the max/initial value'''
        self.arrows = 10
        self.elixers = 5

if __name__ == "__main__":
    print("Running in standby mode")
    test = Hero('linko')
    print(test)