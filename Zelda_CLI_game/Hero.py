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

    name is purely descriptive (no impact on game implementation details)
    Therefore, name is the only mutable value, able to be set via constructor.
    '''


    def __init__(self,name):
        self._name = name
        self.__health = 200
        self.__defense_mode = False
        self.__bombs = 20
        self.__elixers = 5
        self.__arrows = 10
    
    def __repr__(self):
        '''Returns Hero attributes. 
    (health and defense_mode are implementation details)'''
        return "Health: {} / 200\n\
    Bombs: {} / 20\n\
    Elixers: {} / 6\n\
    Arrows: {} / 10".format(self.__health, self.__bombs, self.__elixer, self.__arrows)

    
    def __str__(self):
        '''Returns Hero description'''
        return "{}, a young warrior, clad in green".format(self.__name)
    
    
    def health_bar(self):
        '''Returns Hero health points vs. max health points.'''
        return "{}/200".format(self.__health)
    
    ###Basic. Defense and Special attack for hero, overriden from Enemy.
    def basic_attack(self, enemy):
        '''Offensive attack that leaves Hero vulnerable.'''
        self.__defense_mode = False
        enemy.do_Damage(50)
    
    def basic_name(self):
        '''Provides name for Hero basic attack.'''
        return "used the Master sword"
    
    def defense_attack(self, enemy):
        '''Parry attack that bolsters hero defense
        while also doing small amount of damage to enemy.'''        
        self.__defense_mode = True
        enemy.do_Damage(20)
    
    def defense_name(self):
        '''Returns the name for Hero defense attack'''
        return "shield strike"
    
    def special_attack(self, enemy):
        '''A Powerful attack that does higher amount of damage 
    and also swaps defense mode. If defense mode is true,
    does the standard amount of damage. If false, does 
    greater damage but also hurts the Hero.
        '''
        if self.__bombs:
            if self.__defense_mode:
                self.__defense_mode = False
                enemy.do_damage(75)
                return "The bomb had a Direct Hit.\nYour enemy recoils"
            else:
                self.__defense_mode = True
                enemy.do_damage(110)
                self.__health -= 20
                return "The bomb was very powerful.\n\
            Your enemy was badly injured,\n\
            but you were damaged as well by the shrapnel"
        else:
            return "no bombs remaining.\nCannot use Special attack."

    def special_name(self):
        '''Returns the name of the special attack.'''
        return "Used a bomb"
    
    #Hero unique moves- Arrow and Elixer
    def use_arrow(self, enemy):
        '''Projectile attack:
        highly effective, has no effect on defense mode.
        but limited availability/ uses- 10 available arrows per game.'''        
        enemy.do_Damage(95)
        self.__arrows= self.__arrows - 1
    
    def arrow_name(self):
        '''Returns the name of arrow attack.'''
        return "{} fired an arrow".format(self.__name)
    
    def arrow_count(self):
        '''Returns the number of arrows remaining vs. maximum.'''
        return "{} / 10".format(self.__arrows)
    
    def elixer(self):
        '''Replenishes half of the Heros max health point.
    but limited uses, also turns defense mode to false.
        '''
        self.__defense_mode = False
        self.__health + 100
        self.__elixers - 1
    
    def elixer_name(self):
        '''Returns the name of the elixer move.'''
        return "drank an elixer"
    
    def elixer_count(self):
        '''Returns the amount of remaining elixers vs max elixers.'''
        return "{} / 5".format(self.__elixers)

    def do_damage(self, damage):
        '''
    subtracts damage argument from Hero health.
    If Defense mode is true, cuts value of damage argument in half.
        '''
        if(self.__defense_Mode):
            self.__health -= damage // 2
        else:
            self.__health -= damage

    def reset_health(self):
        '''Sets the health points of Hero to maximum.'''
        self.__health = 200

    def reset_ammo(self):
        '''Sets all the ammunititions to the max/initial value'''
        self.__arrows = 10
        self.__elixers = 5


if __name__ == "__main__":
    print("Running in standby mode")