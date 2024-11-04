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
                self.assertEqual(function(*a), function(*b), msg)

    def test_area_commutativity(self):
        self.__commutativity_test(rectangle.area, "Area not commutative!")


    def test_perimeter_commutativity(self):
        self.__commutativity_test(rectangle.perimeter, "Perimeter not commutative!")