"""
Creator: Ben Sehnert
Date: 8/28/2020
Game: Darknut class
Software: Zelda CLI mini-game

Module Level Docstring: 
Implements the Darknut-
The strongest, most dangerous foe in the game.
An intimidating, armor clad, giant foe with a collasal sword and sturdy shield.
"""
#imports the ABC this object overrides
from Enemy import Enemy

class Darknut(Enemy):
    """Class Level Docstring: 
    
    A Subclass of Enemy ABC which implements a powerful foe.
    
    __init__(self, name) : constructs a Darknut enemy
    __str__(self) : return description + name
    get_health(self): Returns foe health.
    get_name(self): Returns foe name.
    get_description(self): Returns foe description.
    basic_attack(self, enemy): Does average damage, sets defense mode to true.
    basic_name(self): Returns name of basic attack.
    defesnse_attack(self, enemy): Sets defense to true, does damage.
    defense_name(self): Returns name of defense attack. 
    special_attack(self, enemy): self sabotaging, very powerful attack.
    special_name(self): Returns name of special attack.
    do_damage(self, other): a private method used in opponent attacks to apply damage to the monster
    reset_health(self): Applies full recovery- returning health to max.
    """
    version = 2.0
    __name__ = "Darknut"

    def __init__(self,name):
        """
    Constructs a Darknut object.

    name : str - provides a nickname for the monster.
        """
        self.name = name
        self.__health = 200
        self.defense_mode = True

    def __str__(self):
        return "{} named {} is attacking ".format(self.get_description(), self.get_name())
    
    def get_health(self, numeric = False):
        """Returns foes' current health.
        
        numeric = False - default : return UI oriented string (CHP/HP).
        numeric = True - returns health of foe, cast to integer.
        """
        return int(self.__health) if numeric else "{} / 80".format(self.__health) 

    def get_name(self):
        """Returns foe name."""
        return self.name
    
    def get_description(self):
        """Returns foes description."""
        return "An intimidating, armor clad, giant foe with a collasal sword and sturdy shield."

    def basic_attack(self, enemy):
        """Does average damage, sets defense mode to true."""
        self.defense_mode = True, enemy.do_damage(25)
    
    def basic_name(self):
        """Returns name of basic attack."""
        return random.choice(("judo chop","soy sauce spalsh",
        "serbian sword slash","tickle-o'de-tiger","sausage throw"))
    
    def defense_attack(self, enemy):
        """Sets defense to true, does considerable damage
        relative to other opponents."""
        self.defense_mode = True
        enemy.do_damage(30)


    def defense_name(self):
        """Returns name of defense attack."""
        return random.choice(("supa dupa dodge", "weasel spread manuver", "octopus slide",
        "festive basset-hound entaglement", "colombian hair net toss", "very linty blanket plunge" ))

    def special_attack(self, enemy):
        """self sabotaging, very powerful attack.
        greater effect when defense_mode is false.
        ie. deals more damage to self and enemy. 
        same idea with less damage when defense_mode is True.

        enemy : Hero object.
        """
        if self.defense_mode:
            self.__health -= 20
            enemy.do_damage(50)
        else:
            self.__health -= 50
            enemy.do_damage(70)
    
    def special_name(self):
        """Returns name of special attack."""
        return random.choice(("haymaker","molerat stampede", "crusty eskimo rat punch" ,"spinach rake serve","lucid charge"))

    def do_damage(self, damage):
        """
        a private method used in opponent attacks 
        to apply damage to the monster
        
        damage : int - amount of health points to take away.
        """
        if self.defense_mode:
            #defense mode is less effective for stronger enemies
            #to make it easier/ more likely to defeat them.
            self.__health -= damage - 20
        else:
            self.__health -= damage
    
    def reset_health(self):
        """Applies full recovery- returning health to max."""
        self.__health = 200

if __name__ == "__main__":
    print("{} class: running in standby mode".format(Darknut.__name__))