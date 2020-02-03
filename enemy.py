##Ben Sehnert
##8/15/18
##CS172-HW3 'enemy' abstract base class

#import statement #imports ABC module for creation of 'enemy' ABC
import abc

class enemy(metaclass = abc.ABCMeta):
    #init and str methods left empty. Must be initialized by child classes
    def __init__(self):
        pass
    def __str__(self):
        pass
    #abstract methods for accessor/mutator methods
    @abc.abstractmethod
    def getName(self):
        pass
    @abc.abstractmethod
    def getDescription(self):
        pass
    @abc.abstractmethod
    def getHealth(self): #enemy with health zero is unconcsious
        pass
    @abc.abstractmethod#used by the other enemy
    def doDamage(self, damage):#positive int = damage, negative int = heal
        pass
    #Reset Health for next match
    @abc.abstractmethod
    def resetHealth(self):
        pass
#enemy moveset:  basic attack move, defense move, special attack move
    #You are passed the monster you are fighting
    @abc.abstractmethod
    def basicAttack(self,enemy):
        pass	
    #Print the name of the attack used
    @abc.abstractmethod
    def basicName(self):
        pass
    #lets the monster defend itself
    @abc.abstractmethod
    def defenseAttack(self,enemy):
        pass	
    #Print out the name of the attack used
    @abc.abstractmethod
    def defenseName(self):
        pass	
    #Special Attack
    @abc.abstractmethod
    def specialAttack(self,enemy):
        pass
    #prints name of special attack
    @abc.abstractmethod
    def specialName(self):
        pass