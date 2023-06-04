#!/usr/bin/python3
""" Unittest for the max_integer module"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Testcase for the max_integer function"""

    def test_empty_list(self):
        """ Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_at_the_end(self):
        """Test a list where max value is at the end"""
        max_at_the_end = [1, 3, 2, 4]
        self.assertEqual(max_integer(max_at_the_end), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 1, 3, 2]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_unique_element_list(self):
        """Test a list with a single element."""
        unique_element = [40]
        self.assertEqual(max_integer(unique_element), 40)

    def test_ints_and_floats_list(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_float_list(self):
        """Test a list of floats."""
        float = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(float), 15.2)

    def test_string_list(self):
        """Test a string."""
        string = "Terry"
        self.assertEqual(max_integer(string), 'y')

    def test_neg_float_list(self):
        """Test negative floats"""
        neg_float = [-5.55, -66.66, -111.1]
        self.assertEqual(max_integer(neg_float), -5.55)

    def test_diff_datatypes(self):
        """ Test different data types"""
        with self.assertRaises(TypeError):
            max_integer([1, "1"])

    def test_list_list(self):
        """ Test nested list"""
        list = [[1, 2], [2, 1]]
        self.assertEqual(max_integer(list), [2, 1])


if __name__ == "__main__":
    unittest.main()
