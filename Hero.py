##Ben Sehnert
##8/15/2018
##cs 172- hero class

#Imports enemy ABC
from enemy import *
class Hero:
    def __init__(self,name):#initializes instances of the hero class
        self.__name = name;
        self.__health = 200;
        self.__defense_Mode = True;
        self.__elixers = 6;
        self.__arrows = 10;
    #string method prints out hero info
    def __str__(self):
        return "a brave young hylian clad in green \nsome know him as link, some call him {}".format(self.__name)
    #accessor methods
    def getHealth(self):
        return self.__health;
    def healthBar(self):
        return "{}/200".format(self.__health);
    def getName(self):
        return self.__name;
    def getDesc(self):
        return "{} has {} elixers in his pouch and {} arrows in his quiver".format(self.__name, self.__elixers, self.__arrows) 
    #attack methods
    def basic_Attack(self, enemy):
        self.__defense_mode = True;#can defend while using basic attack
        enemy.do_Damage(50);
    def basic_Name(self):
        return "the master sword";
    def defense_Attack(self, enemy):
        self.__defense_Mode = True;
    def defense_Name(self):
        return "shield strike";
    def special_Attack(self, enemy):
        self.__defense_mode = True;
        enemy.do_Damage(60);
    def special_Name(self):
        return "threw a bomb";
    #hero exclusive moves 
    def use_Arrow(self, enemy):
        enemy.do_Damage(95);
        self.__arrows= self.__arrows - 1;
    def arrow_Name(self):#returns name of the attack
        return "an arrow";
    def arrow_Count(self):#returns the number of arrows remaining
        return self.__arrows
    def elixer(self):#handles the mechanics of elixer taking
        self.__health + 100;
        self.__elixers - 1;
    def elixer_name(self):#returns that elixer was drank
        return "{} drank an elixer".format(self.__name);
    def elixer_Count(self):
        return self.__elixers
    #damage mechanism
    def do_Damage(self, damage):
        if(self.__defense_Mode):
            self.__health = self.__health-(damage//2);
        else:
            self.__health = self.__health - damage;
    #resets health
    def resetHealth(self):
        self.__health = 100;
#name == main thing
if __name__ == "__main__":
    print("Running in standby mode");