# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(2),3)
        self.assertEqual(utils.fact(3),6)
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,4,4),(-2))
        self.assertEqual(utils.roots (1,6,9),(-3))
        
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
