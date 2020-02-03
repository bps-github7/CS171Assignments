##Ben Sehnert
##8/15/2018
##cs 172 chuchu class

#imports enemy ABC
from enemy import *
class Chuchu:
    def __init__(self,name):#initializes instance of the class chuchu
        self.__name = name;
        self.__health = 50;
        self.__defense_Mode = False;
    #string method
    def __str__(self):
        return "a chuchu named {} approaches".format(self.__name)
    #accessor methods
    def getHealth(self):
        return self.__health;
    def getName(self):
        return self.__name;    
    def getDesc(self):
        return "A colorful & gelatinous monster.\nDefeat it to collect its gelatinous elixer ingredients"
    #Attack methods
    def basic_Attack(self, enemy):
        self.__defense_mode = False;#cant defend while using basic attack
        enemy.do_Damage(5);
    def basic_Name(self):
        return "Wap!";
    def defense_Attack(self, enemy):
        self.__defense_Mode = False;#cant defend    
    def defense_Name(self):
        return "rolls away in defense!";
    def special_Attack(self, enemy):
        self.__defense_mode = False;
        enemy.do_Damage(12);    
    def special_Name(self):
        return "pounce strike";
    #damage mechanism
    def do_Damage(self, damage):
        if(self.__defense_Mode == True):
            self.__health = self.__health-(damage//2);
        else:
            self.__health = self.__health - damage;
    #resets health    
    def resetHealth(self):
        self.__health = 50;
#if name == main thing
if __name__ == "__main__":
    print("Running in standby mode");