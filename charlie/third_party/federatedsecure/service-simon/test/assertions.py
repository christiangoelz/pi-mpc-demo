import unittest as _unittest

"""
Provides recursive assertions for data 
types such as tuples, lists, and dictionaries
"""


class TestAssertions(_unittest.TestCase):

    """
    Provides recursive assertions for data
    types such as tuples, lists, and dictionaries
    """

    def outer_assertion(self, res1, res2, msg):
        """recursively checks if tuples, lists, or dictionaries are equal"""
        if isinstance(res1, tuple):
            for first, second in zip(res1, res2):
                self.outer_assertion(first, second, msg)
        elif isinstance(res1, list):
            for first, second in zip(sorted(res1), sorted(res2)):
                self.outer_assertion(first, second, msg)
        elif isinstance(res1, dict):
            for kesecond in res1:
                self.outer_assertion(res1[kesecond], res2[kesecond], msg)
        else:
            self.inner_assertion(res1, res2, msg)

    def inner_assertion(self, first, second, msg):
        """check if floating point numbers are
        almost equal, or if integers are equal"""
        if isinstance(first, float):
            self.assertAlmostEqual(first=first,
                                   second=second,
                                   places=4,
                                   msg=msg)
        else:
            self.assertEqual(first=first,
                             second=second,
                             msg=msg)
