import unittest
import sys
import os
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from methods import *

def function1(x: float):
    return x

def derivative_function1(x: float):
    return 1

def function2(x: float):
    return math.sqrt(x) - 2

def derivative_function2(x: float):
    return 1/ (2 * math.sqrt(x))

def function3(x: float):
    return math.sin(x)

def derivative_function3(x: float):
    return math.cos(x)

class TestBisectionMethod(unittest.TestCase):
    def test_bisection_function1(self):
        self.assertAlmostEqual(bisection_method([-1, 1], function1, 10**(-10))[0], 0.0, delta=10**(-10))
        
    def test_bisection_function2(self):
        self.assertAlmostEqual(bisection_method([2, 5], function2, 10**(-10))[0], 4.0, delta=10**(-10))
        
    def test_bisection_function3(self):
        self.assertAlmostEqual(bisection_method([math.pi / 2, math.pi * 3/2], function3, 10**(-10))[0], math.pi, delta=10**(-10))

class TestNewtonMethod(unittest.TestCase):
    def test_newton_function1(self):
        self.assertAlmostEqual(newton_method([-1, 1], function1, derivative_function1, 10**(-10))[0], 0.0, delta=10**(-10))
        
    def test_newton_function2(self):
        self.assertAlmostEqual(newton_method([2, 5], function2, derivative_function2, 10**(-10))[0], 4.0, delta=10**(-10))
        
    def test_newton_function3(self):
        self.assertAlmostEqual(newton_method([math.pi / 2, math.pi * 3/2], function3, derivative_function3, 10**(-10))[0], math.pi, delta=10**(-10))

class TestModifiedNewtonMethod(unittest.TestCase):
    def test_modified_newton_function1(self):
        self.assertAlmostEqual(modified_newton_method([-1, 1], function1, derivative_function1, 10**(-10))[0], 0.0, delta=10**(-10))
        
    def test_modified_newton_function2(self):
        self.assertAlmostEqual(modified_newton_method([2, 5], function2, derivative_function2, 10**(-10))[0], 4.0, delta=10**(-10))
        
    def test_modified_newton_function3(self):
        self.assertAlmostEqual(modified_newton_method([math.pi / 2, math.pi * 3/2], function3, derivative_function3, 10**(-10))[0], math.pi, delta=10**(-10))

class TestSecantMethod(unittest.TestCase):
    def test_secant_function1(self):
        self.assertAlmostEqual(secant_method([-1, 1], function1, 10**(-10))[0], 0.0, delta=10**(-10))
        
    def test_secant_function2(self):
        self.assertAlmostEqual(secant_method([2, 5], function2, 10**(-10))[0], 4.0, delta=10**(-10))
        
    def test_secant_function3(self):
        self.assertAlmostEqual(secant_method([math.pi / 2, math.pi * 3/2], function3, 10**(-10))[0], math.pi, delta=10**(-10))

class TestRootsSeparation(unittest.TestCase):
    def test_separation_function1(self):
        self.assertEqual(len(roots_separation(-1, 1, 20, function1)), 1)
        self.assertAlmostEqual(roots_separation(-1, 1, 20, function1)[0][0], 0.0, delta=0.1)
        self.assertAlmostEqual(roots_separation(-1, 1, 20, function1)[0][1], 0.0, delta=0.1)

    def test_separation_function2(self):
        self.assertEqual(len(roots_separation(0, 10, 100, function2)), 1)
        self.assertAlmostEqual(roots_separation(0, 10, 100, function2)[0][0], 4.0, delta=0.1)
        self.assertAlmostEqual(roots_separation(0, 10, 100, function2)[0][1], 4.0, delta=0.1)
    
    def test_separation_function3(self):
        self.assertEqual(len(roots_separation(0, math.pi + 0.1, 32, function3)), 2)
        self.assertAlmostEqual(roots_separation(0, math.pi + 0.01, 32, function3)[0][0], 0.0, delta=0.1)
        self.assertAlmostEqual(roots_separation(0, math.pi + 0.01, 32, function3)[0][1], 0.0, delta=0.1)
        self.assertAlmostEqual(roots_separation(0, math.pi + 0.01, 32, function3)[1][0], math.pi, delta=0.1)
        self.assertAlmostEqual(roots_separation(0, math.pi + 0.01, 32, function3)[1][1], math.pi, delta=0.1)

if __name__ == '__main__':
    unittest.main()
