import unittest
from homeworks import (
    add_tuple_to_list, swap_elements_in_tuple_list, check_condition_in_tuple_list,
    find_car_by_model, find_car_by_year_range, find_unique_characters,
    take_elements_from_list, add_numbers, multiply_numbers
)

class TestHomeworks(unittest.TestCase):

    def test_add_tuple_to_list(self):
        lst = [(1, 2)]
        tpl = (3, 4)
        self.assertEqual(add_tuple_to_list(lst, tpl), [(1, 2), (3, 4)])

    def test_swap_elements_in_tuple_list(self):
        lst = [(1, 2), (3, 4)]
        self.assertEqual(swap_elements_in_tuple_list(lst, 0, 1), [(2, 1), (4, 3)])

    def test_check_condition_in_tuple_list(self):
        lst = [(1, 2), (3, 4)]
        self.assertEqual(check_condition_in_tuple_list(lst, 0, lambda x: x > 1), [(3, 4)])

    def test_find_car_by_model(self):
        cars = [{'model': 'A', 'year': 2000}, {'model': 'B', 'year': 2005}]
        self.assertEqual(find_car_by_model(cars, 'A'), [{'model': 'A', 'year': 2000}])

    def test_find_car_by_year_range(self):
        cars = [{'model': 'A', 'year': 2000}, {'model': 'B', 'year': 2005}]
        self.assertEqual(find_car_by_year_range(cars, 2000, 2003), [{'model': 'A', 'year': 2000}])

    def test_find_unique_characters(self):
        self.assertEqual(set(find_unique_characters('hello')), set(['h', 'e', 'l', 'o']))

    def test_take_elements_from_list(self):
        lst = [1, 2, 3, 4, 5]
        indexes = [0, 2, 4]
        self.assertEqual(take_elements_from_list(lst, indexes), [1, 3, 5])

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
