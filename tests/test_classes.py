import unittest
from source.classes import WebScript


class TestSeleniumWebScript(unittest.TestCase):
    def test_class_cannot_be_instantiated(self):
        with self.assertRaises(Exception) as context:
            WebScript()
        self.assertIn("Can't instantiate abstract class", str(context.exception))
