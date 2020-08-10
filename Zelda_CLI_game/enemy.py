'''
Programmer: Ben Sehnert
Program: Enemy Abstract base class
Date: 8/1/2020
Software: Zelda CLI mini-game.

Module Level Docstring: Implements an 'enemy' abstract base class (ABC)
which provides the structure and documentation for all in-game objects.
'''

import abc
from abc import ABCMeta

#cant figure out how to inherit from metaclass = ABCe
class Enemy(metaclass = abc.ABCMeta):
    '''Class Level Docstring: creates signitures/ abstract methods
    for init (constructor), __str__ (string repr.) and all helper
    methods for gameplay.

    NOTE: getter methods are retained from version 1, despite
    this class adhering to the Descriptor protocol/ being a 
    new style class.
    
    This is done in order to facilitate documentation. 
    When users implement the enemy class they will understand 
    how use of their object attributes makes gameplay/ battle possible.
    '''

    version = 2.0

    @abc._abc_init
    def __init__(self):
        '''Construct enemy by passing in name, desc & health as args.'''
        pass
    
    @abc.abstractmethod
    def __str__(self):
        '''Returns all attributes/properties of the enemy.'''
        return NotImplemented

    @property
    @abc.abstractmethod
    def get_name(self):
        '''Returns the enemy name.'''
        return NotImplemented
    
    @property
    @abc.abstractmethod
    def get_description(self):
        '''Returns a short message describing
    the enemy and providing any nessecary information.
        '''
        return NotImplemented
    
    @property
    @abc.abstractmethod
    def get_health(self):
        '''An enemy with 0 health is defeated.'''
        return NotImplemented
    
    #gamified versions of setters/mutator methods

    @abc.abstractmethod
    def do_damage(self, damage):
        '''Positive numeric argument does damage,
        and negative numeric argument heals enemy.'''
        return NotImplemented
    
    @abc.abstractmethod
    def reset_health(self):
        '''Returns health to starting HP.'''
        return NotImplemented

    # the attacks include: basic attack, defensive attack, special attack
    # each of these has a corresponding method for returning the attack name.  
    
    @abc.abstractmethod
    def basic_attack(self, enemy):
        '''A less powerful, more commonly used attack.'''
        return NotImplemented	
    
    @abc.abstractmethod
    def basic_name(self):
        '''returns basic attack name.'''
        return NotImplemented

    @abc.abstractmethod
    def defense_attack(self, enemy):
        '''Defensive move that counters or blocks an opponent
    attack. some may infrequently do damage to opponent.
        '''
        return NotImplemented

    @abc.abstractmethod
    def defense_name(self):
        '''Returns defense attack name.'''
        return NotImplemented
	
    @abc.abstractmethod
    def special_attack(self, enemy):
        '''Special attack which has limited availability, that may deal 
    extra damanage, have increased accurarcy, or some other desired effect.
        '''
        return NotImplemented
    
    @abc.abstractmethod
    def special_name(self):
        '''Returns name of special attack,'''
        return NotImplemented
