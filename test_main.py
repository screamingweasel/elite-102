import unittest
import main

class TestMain(unittest.TestCase):

    def test_add_two(self):
        result = main.add_two(1,1)
        self.assertEquals(result, 2)

    # This should fail
    def test_open_connection(self):
        result = main.open_connection()
        self.assertIsNotNone(result)

    def test_add_account(self):
        result = main.add_account("First", "Last", "foo@bar.com", "1234", False)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    print("Foo")
    unittest.main()