#!/usr/bin/env python3

import inspect
import re
import unittest

from src.lengths import lengths


def source_rows(func):
    """Count non-empty, non-comment statement rows in func's source."""
    src = inspect.getsource(func)
    lines = [line.strip() for line in re.split(r'\n|;', src)
             if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)


class TestLengths(unittest.TestCase):

    def test_function_exists(self):
        try:
            lengths([[1]])
        except Exception as e:
            self.fail(
                "lengths should be callable as lengths([[1]]). "
                "Got exception: %r" % (e,))

    def test_return_type_is_list(self):
        result = lengths([[1]])
        self.assertTrue(
            type(result) == list,
            msg="lengths is expected to return a value which is of type "
            "list, now it returns a value %s which is of type %s, when it "
            "is called with the parameter lengths([[1]])."
            % (result, type(result).__name__))

    def test_function_body_is_short(self):
        max_lines = 2
        lines = source_rows(lengths)
        self.assertTrue(
            lines <= max_lines,
            msg="Function lengths must have at most %d rows in this "
            "exercise.\nThe function now has a total of %d rows "
            "(excluding empty rows and comments)." % (max_lines, lines))

    def test_worked_example_1(self):
        test_case = [[1, 2], [3, 4]]
        expected = [2, 2]
        result = lengths(test_case)
        self.assertEqual(
            result, expected,
            msg="The function is expected to return the following list:\n"
            "%s\nwhen it is called with the parameter %s\nnow the "
            "function returns\n%s" % (expected, test_case, result))

    def test_worked_example_2(self):
        test_case = [[1, 2, 3], [4, 3, 2, 1], [1, 2, 1, 2, 1, 2]]
        expected = [3, 4, 6]
        result = lengths(test_case)
        self.assertEqual(
            result, expected,
            msg="The function is expected to return the following list:\n"
            "%s\nwhen it is called with the parameter %s\nnow the "
            "function returns\n%s" % (expected, test_case, result))

    def test_worked_example_3(self):
        test_case = [[1, 2, 3, 1, 2, 3], [1, 2, 3, 4, 5, 4, 3, 2, 1], [1], [1]]
        expected = [6, 9, 1, 1]
        result = lengths(test_case)
        self.assertEqual(
            result, expected,
            msg="The function is expected to return the following list:\n"
            "%s\nwhen it is called with the parameter %s\nnow the "
            "function returns\n%s" % (expected, test_case, result))

    def test_empty_list_of_lists(self):
        result = lengths([])
        self.assertEqual(
            result, [],
            msg="lengths([]) should return an empty list, since there are "
            "no inner lists to measure.")


if __name__ == '__main__':
    unittest.main()
