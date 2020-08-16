'''


Module Docstring:
B Sehnert
8.13.2020
cs 172 moblin class


'''
from Enemy import Enemy
class Moblin(Enemy):
    '''
Class Docstring:
    '''
    version = 2.0

    def __init__(self,name):
        '''Constructs a Moblin.'''
        self.name = name
        self.__health = 300
        self.defense_mode = True

    def __str__(self):
        return "a Moblin named {} is attacking".format(self.name)

    
    def get_health(self):#returns health
        return "Remaining health: {} / 300"\
        .format(self.__health)
    
    def get_name(self):#returns name
        return " A Moblin named {} is attacking!.format".format(self.name)    
    
    def get_description(self):#returns description
        return "A big, ugly moblin with a pointy snout.\n\
        \r\rBe careful: he is powerful and tough."
    
    def basic_attack(self, enemy):
        '''the most common enemy attack.
        sets d_mode false'''
        #cant defend while using basic attack
        self.defense_mode = False
        enemy.do_damage(25)
    
    def basic_name(self):
        return "Kick"
    
    def defense_attack(self, enemy):#defense attack
        self.defense_mode = True
    
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
            return True
        else:
            self.__health -= damage
    
    def reset_health(self):
        self.__health = 300

if __name__ == "__main__":
    print("Running in standby mode")
    M = Moblin('Thornicus')
    print(M.get_description())