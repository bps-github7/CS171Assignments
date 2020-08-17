'''Module Level Docstring:
Programmer: Ben Sehnert
Program: Ben Sehnert
Date: 8/14/2020
'''

import unittest
# from CS171Assignments.Zelda_CLI_game.Hero import Hero
from Hero import Hero
from Bokoblin import Bokoblin

class TestHero(unittest.TestCase):
    '''Class level Docstring: Ensures reliability of Hero class.'''
    
    
    def setUp(self):
        self.m = Hero("SkonadloneS")
        self.n = Bokoblin("Gary")

    def tearDown(self):
        del self.m, self.n

    #Hero Attack testing- basic, defense, special
    def test_basic_attack(self):
        m.basic_attack(n)
        self.assertEqual()

    def test_defense_attack(self):
        m.defense_attack(n)
        self.assertEqual()

    def test_special_attack(self):
        m.special_attack(n)
        self.assertEqual()

    #attack name tests
    def test_basic_name(self):
        self.assertEqual(self.m.basic_name(), "Used the Master Sword")

    def test_defense_name(self):
        self.assertEqual(self.m.defense_name(), "Shield strike")

    def test_special_name(self):
        self.assertEqual(self.m.special_name(), "Used a bomb")

    def test_use_arrow(self):
        self.assertEqual()

    def test_arrow_name(self):
        self.assertEqual()

    def test_arrow_count(self):
        self.assertEqual()

    def test_elixer(self):
        self.assertEqual()

    def test_elixer_name(self):
        self.assertEqual()

    def test_do_damage(self):
        self.assertEqual()

    def test_reset_health(self):
        self.assertEqual()
    
    def test_reset_ammo(self):
        self.assertEqual()

#using Global variables to reduce code redundancy
m, n = Hero(), Bokoblin("Gary")

if __name__ == "__main__":
    # visual_main()
    unittest.main()