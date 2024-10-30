import unittest

class TestFunc(unittest.TestCase):
    def test_func(self):
        from message import func
        self.assertIsNone(func("Hello World!"))
        
