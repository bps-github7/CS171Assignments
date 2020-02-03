##Ben Sehnert
##8/15/2018
##cs 172 darknut class
from enemy import *#import statements
class Darknut:
    def __init__(self, name):#initializes instances of the class darknut
        self.__name = name;
        self.__health = 450;
        self.__defense_Mode = True;
    def __str__(self):#prints monster name and approach info
        return "a darknut named {} is attacking from the rear".format(self.__name)
    #accessor methods
    def getHealth(self):#returns health
        return self.__health;
    def getName(self):#returns name
        return self.__name;
    def getDesc(self):#returns description
        return "An powerful darknut with a cape and inpenetrable armor.\n good luck with this one G"
    #attack methods
    def basic_Attack(self, enemy):
        self.__defense_mode = True;#can defend while using basic attack
        enemy.do_Damage(20);
    def basic_Name(self):
        return "sword strike";
    def defense_Attack(self, enemy):
        self.__defense_Mode = True;
    def defense_Name(self):
        return "pary";
    def special_Attack(self, enemy):
        self.__defense_mode = True;
        enemy.do_Damage(40);
    def special_Name(self):
        return "body slam";
    #damage mechanism
    def do_Damage(self, damage):
        if(self.__defense_Mode == True):
            self.__health = self.__health-(damage//2);
        else:
            self.__health = self.__health - damage;
    def resetHealth(self):#resets enemy health
        self.__health = 450;
#if name == main thing
if __name__ == "__main__":
    print("Running in standby mode");