'''
Programmer: Ben Sehnert
Program: Hero Class
Date: 8/15/2018
Software: Zelda CLI mini game

Module Level Docstring: Implements a Hero class which 
creates the playable character in the cmd line game.
'''
from Enemy import Enemy

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
    
    
    def get_health(self):
        return "{} / 200".format(self.__health)
    
    def basic_attack(self, enemy):
        '''Offensive attack that leaves Hero vulnerable.'''
        self.defense_mode = False
        enemy.do_damage(50)
    
    def basic_name(self):
        '''Provides name for Hero basic attack.'''
        return "Used the Master Sword"
    
    def defense_attack(self, enemy):
        '''Parry attack that bolsters hero defense
        while also doing small amount of damage to enemy.'''        
        self.defense_mode = True
        enemy.do_damage(20)
    
    def defense_name(self):
        '''Returns the name for Hero defense attack'''
        return "Shield strike"
    
    def special_attack(self, enemy):
        '''A Powerful attack that does higher amount of damage 
    and also swaps defense mode. If defense mode is true,
    does the standard amount of damage. If false, does 
    greater damage but also hurts the Hero.
        '''
        if self.bombs:
            if self.defense_mode:
                self.defense_mode = False
                enemy.do_damage(75)
                return "The bomb had a Direct Hit.\nYour enemy recoils"
            else:
                self.defense_mode = True
                enemy.do_damage(110)
                self.health -= 20
                return "The bomb was very powerful.\n\
            Your enemy was badly injured,\n\
            but you were damaged as well by the shrapnel"
        else:
            return "No bombs remaining.\nCannot use Special attack."

    def special_name(self):
        '''Returns the name of the special attack.'''
        return "Used a bomb"
    
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
        return "Drank an elixer"
    
    def elixer_count(self):
        '''Returns the amount of remaining elixers vs max elixers.'''
        return "{} / 5".format(self.elixers)

    def do_damage(self, damage):
        if self.defense_mode:
            self.__health -= damage // 2
        else:
            self.__health -= damage
    
    def reset_health(self):
        '''Sets the health points of Hero to maximum.'''
        self.__health = 200

    def reset_ammo(self):
        '''Sets all the ammunititions to the max/initial value'''
        self.arrows = 10
        self.elixers = 5

if __name__ == "__main__":
    print("Running in standby mode")
    test = Hero('linko')
    print(test)