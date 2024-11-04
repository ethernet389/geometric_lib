import unittest
import itertools as iter
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
        self.__same_values_test(tests, rectangle.area, "Not work with same values!")

    def test_perimeter_same_values(self):
        tests = [(0, 0),
                 (1, 4),
                 (5, 20),
                 (10**100, 4*10**100),
                 (10**1000, 4*10**1000),
                 (1.2, 4.8),
                 (0.01, 0.04)]
        self.__same_values_test(tests, rectangle.perimeter, "Not work with same values!")