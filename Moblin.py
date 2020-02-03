##B Sehnert
##8.15.2018
##cs 172 moblin class
from enemy import *
class Moblin:
    def __init__(self,name):#initializes instances of the moblin class
        self.__name = name;
        self.__health = 300;
        self.__defense_Mode = True;
    def __str__(self):
        return "a moblin named {} is attacking".format(self.__name)#returns monster name and approach info
    def getHealth(self):#returns health
        return self.__health;
    def getName(self):#returns name
        return self.__name;    
    def getDesc(self):#returns description
        return "A big, ugly moblin with a pointy snout.\nBe careful: he is powerful and tough"
    def basic_Attack(self, enemy):#basic attack
        self.__defense_mode = False;#cant defend while using basic attack
        enemy.do_Damage(15);
    def basic_Name(self):#basic attack name
        return "Kick";
    def defense_Attack(self, enemy):#defense attack
        self.__defense_Mode = True;
    def defense_Name(self):#defense name
        return "waves his lantern in defense!";
    def special_Attack(self, enemy):#special attack
        self.__defense_mode = True;
        enemy.do_Damage(45);
    def special_Name(self):#special attack name
        return "belch-roar! jab-strike!";
    def do_Damage(self, damage):#damage mechanism
        if(self.__defense_Mode == True):
            self.__health = self.__health-(damage//2);
        else:
            self.__health = self.__health - damage;
    def resetHealth(self):#resets health
        self.__health = 300;
#if name == main thing
if __name__ == "__main__":
    print("Running in standby mode");