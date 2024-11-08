import unittest
import itertools as iter
import math
import circle, rectangle, square, triangle

def gen_commutative_tuples(lst: list[int]):
    return list(iter.permutations(lst, r=len(lst)))

class RectangleTestCase(unittest.TestCase):
    def __commutativity_test(self, function, msg):
        test1 = gen_commutative_tuples([1, 2])
        test2 = gen_commutative_tuples([10**12, 10**24])
        test3 = gen_commutative_tuples([1.2, 2.5])
        test4 = gen_commutative_tuples([0, 0])

        tests = [test1, test2, test3, test4]
        for test in tests:
            for a, b in iter.permutations(test, r=2):
                self.assertEqual(function(*a), function(*b), f'{msg} : {a} | {b}')

    def test_area(self):
        tests = [(1, 2, 2),
                 (1, 0, 0),
                 (2, 8, 16),
                 (10**10, 3**10, 30**10),
                 (0.1, 2, 0.2)]
        for test in tests:
            args = test[0:2]
            self.assertEqual(rectangle.area(*args), test[2], "Area don't work!")

    def test_perimeter(self):
        tests = [(1, 2, 6),
                 (1, 0, 2),
                 (2, 8, 20),
                 (10**10, 3**10, 2*10**10 + 2*3**10),
                 (0.1, 2, 4.2)]
        for test in tests:
            args = test[0:2]
            self.assertEqual(rectangle.perimeter(*args), test[2], "Perimeter don't work!")

    def test_area_commutativity(self):
        self.__commutativity_test(rectangle.area, "Area not commutative!")


    def test_perimeter_commutativity(self):
        self.__commutativity_test(rectangle.perimeter, "Perimeter not commutative!")

    def __same_values_test(self, tests, function, msg=None):
        for test in tests:
            args = (test[0], test[0])
            self.assertEqual(function(*args), test[1], f'{msg} : {args}')
        
    def test_area_same_values(self):
        tests = [(0, 0),
                 (1, 1),
                 (5, 25),
                 (10**100, 10**200),
                 (10**1000, 10**2000),
                 (1.2, 1.44),
                 (0.01, 0.0001)]
        self.__same_values_test(tests, rectangle.area, "Area not work with same values!")

    def test_perimeter_same_values(self):
        tests = [(0, 0),
                 (1, 4),
                 (5, 20),
                 (10**100, 4*10**100),
                 (10**1000, 4*10**1000),
                 (1.2, 4.8),
                 (0.01, 0.04)]
        self.__same_values_test(tests, rectangle.perimeter, "Perimeter not work with same values!")


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        tests = [(0, 0),
                 (1, math.pi),
                 (4, math.pi * 16),
                 (0.1, math.pi * 0.01),
                 (10**100, math.pi * 10**200)]
        for test in tests:
            self.assertEqual(circle.area(test[0]), test[1], "Area don't work!")

    def test_perimeter(self):
        tests = [(0, 0),
                 (1, 2 * math.pi),
                 (4, math.pi * 8),
                 (0.1, math.pi * 0.2),
                 (10**100, math.pi * 2 * 10**100)]
        for test in tests:
            self.assertEqual(circle.perimeter(test[0]), test[1], "Perimeter don't work!")

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        tests = [(0, 0), (1, 1), (2, 4), (10**10, 10**20)]
        for test in tests:
            self.assertEqual(square.area(test[0]), test[1], "Area don't work")
        self.assertEqual(format(square.area(0.1), ".2f"), "0.01", "Area don't work")

    def test_perimeter(self):
        tests = [(0, 0), (1, 4), (2, 8), (0.1, 0.4), (10**10, 4*10**10)]
        for test in tests:
            self.assertEqual(square.perimeter(test[0]), test[1], "Perimeter don't work")