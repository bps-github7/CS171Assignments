##Ben Sehnert
##8/15/2018
##CS 172 Bokoblin class

#import ABC enemy
from enemy import *
class Bokoblin:#initializes instances of the class bokoblin
    def __init__(self,name):
        self.__name = name;
        self.__health = 120;
        self.__defense_Mode = True;
    #monster title
    def __str__(self):
        return "a bokoblin named {} is partying nearby".format(self.__name)
    #accessor methods
    def getHealth(self):
        return self.__health;
    def getName(self):
        return self.__name;
    def getDesc(self):
        return "A meager Bokoblin with a sword and shield.\nYou can overpower it if you are sneaky"
    #attack methods
    def basic_Attack(self, enemy):
        self.__defense_mode = True;#can defend while using basic attack
        enemy.do_Damage(25);
    def basic_Name(self):
        return "slice";
    def defense_Attack(self, enemy):
        self.__defense_Mode = True;
    def defense_Name(self):
        return "jump!";
    #special attack deals damage and has defense mode 
    def special_Attack(self, enemy):
        self.__defense_mode = True;
        enemy.do_Damage(40);
    def special_Name(self):
        return "poison bite";
    #damage mechanism
    def do_Damage(self, damage):#same damage mechanics as every other class
        if(self.__defense_Mode == True):
            self.__health = self.__health-(damage//2);
        else:
            self.__health = self.__health - damage;
    def resetHealth(self):
        self.__health = 120;#reset health to max
#if name == main thing
if __name__ == "__main__":
    print("Running in standby mode");