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
        self.__name = name
        self.__health = 120
        self.__defense_Mode = True

    def __str__(self):
        '''
        
        '''
        return "a bokoblin named {} is partying nearby".format(self.__name)
    
    def get_health(self):
        '''

        '''
        return self.__health
    
    def get_name(self):
        '''

        '''
        return self.__name
    
    def get_desc(self):
        '''
        
        '''
        return "A meager Bokoblin with a sword and shield.\n\
            You can overpower it if you are sneaky"

    def basic_Attack(self, enemy):
        '''
    #what is defense mode?
        '''
        self.__defense_mode = True
        enemy.do_Damage(25)
    
    def basic_Name(self):
        '''

        '''
        return "slice"
    
    def defense_Attack(self, enemy):
        '''
        
        '''
        self.__defense_Mode = True
    
    def defense_Name(self):
        '''
        
        '''
        return "jump!"
        enemy.do_Damage(40)

    def special_Name(self):
        '''
        
        '''
        return "poison bite"

    def do_Damage(self, damage):
        '''
        
        '''
        if(self.__defense_Mode == True):
            self.__health = self.__health-(damage//2)
        else:
            self.__health = self.__health - damage
    
    #reset health to max
    def resetHealth(self):
        '''
        
        '''
        self.__health = 120

if __name__ == "__main__":
    print("Running in standby mode")