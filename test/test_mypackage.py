import unittest

import mypackage


class GeneralTests(unittest.TestCase):
    def test_basics(self):
        self.assertEqual('result', mypackage.a_function_of_mine())
        
        m = mypackage.MyClass()
        self.assertEqual('another result', m.a_method_of_mine())
