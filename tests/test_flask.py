import unittest
import requests
import json
import sys

sys.path.append('.')

import backend.app as app

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        response = self.get('/')
        self.assertEqual(response, "<h1>Homepage</h1>")

if __name__ == "__main__":
    unittest.main()