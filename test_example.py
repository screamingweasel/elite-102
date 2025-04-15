import unittest
import example

class TestMain(unittest.TestCase):

    def test_add_two(self):
        result = example.add_two(1,1)
        self.assertEqual(result, 2)

    # This should fail
    def test_open_connection(self):
        result = example.open_connection()
        self.assertIsNotNone(result)

    def test_add_account(self):
        result = example.add_account("First", "Last", "foo@bar.com", "1234", False)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    print("Performing Tests")
    unittest.main()