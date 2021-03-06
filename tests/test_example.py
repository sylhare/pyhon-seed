import unittest

from src.example import hello, root_path


class ExampleTest(unittest.TestCase):

    def setUp(self):
        print("\nSet up - Before each test")

    def test_hello_world(self):
        self.assertEqual("Hello World!", hello())

    def test_root_path(self):
        self.assertTrue("python-seed" in root_path())

    def tearDown(self):
        print("Tear Down - After each Test\n")


if __name__ == "__main__":
    unittest.main()
