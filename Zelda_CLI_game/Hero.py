'''
Programmer: Ben Sehnert
Program: Hero Class
Date: 8/15/2018
Software: Zelda CLI mini game

Module Level Docstring
'''
#must be something wrong with package/ import path
from Enemy import Enemy

class Hero:
    '''Class Level Docstring:
    
    '''


    def __init__(self,name):
        self.__name = name
        self.__health = 200
        self.__defense_Mode = True
        self.__elixers = 6
        self.__arrows = 10
    
    def __str__(self):
        '''
    Returns all properties attached to the hero
        '''
        return "Health: {} / 200\n\
        Elixers: {} / 6\n\
        Arrows: {} / 10".format(self.__health, self.__elixer, self.__arrows)  

    def getHealth(self):
        '''

        '''        
        return self.__health
    
    def healthBar(self):
        '''

        '''        
        return "{}/200".format(self.__health)
    
    def getName(self):
        '''

        '''        
        return self.__name
    
    def getDesc(self):
        '''

        '''        
        return "{} has {} elixers in his pouch and {} arrows in his quiver".format(self.__name, self.__elixers, self.__arrows) 
    
    #attack methods
    
    def basic_Attack(self, enemy):
        '''

        '''        
        self.__defense_mode = True
        enemy.do_Damage(50)
    
    def basic_Name(self):
        '''

        '''        
        return "the master sword"
    
    def defense_Attack(self, enemy):
        '''

        '''        
        self.__defense_Mode = True
    
    def defense_Name(self):
        '''

        '''        
        return "shield strike"
    
    def special_Attack(self, enemy):
        '''

        '''        
        self.__defense_mode = True
        enemy.do_Damage(60)
    
    def special_Name(self):
        '''

        '''        
        return "threw a bomb"
    
    #hero exclusive moves 
    
    def use_Arrow(self, enemy):
        '''

        '''        
        enemy.do_Damage(95)
        self.__arrows= self.__arrows - 1
    
    def arrow_Name(self):
        '''

        '''
        return "an arrow"
    
    def arrow_Count(self):
        '''
    returns the number of arrows remaining
        '''
        return self.__arrows
    
    def elixer(self):
        '''

        '''
        self.__health + 100
        self.__elixers - 1
    
    def elixer_name(self):
        '''

        '''
        return "{} drank an elixer".format(self.__name)
    
    def elixer_Count(self):
        '''

        '''
        return self.__elixers

    def do_Damage(self, damage):
        '''

        '''
        if(self.__defense_Mode):
            self.__health = self.__health-(damage//2)
        else:
            self.__health = self.__health - damage

    def resetHealth(self):
        '''

        '''
        self.__health = 100

if __name__ == "__main__":
    print("Running in standby mode")