import unittest
import StackOverflow
import pandas

"""
This is our StackOverflowAPI testing class which does not interact with the actual API via the internet,
instead it returns dummy values.
"""
class APITesting(StackOverflow.StackOverflowAPI):
    meta_data = {}  # todo fill these with our appropriate values.
    stack_data = {}  # todo fill these with our appropriate values


class TestingGetters(unittest.TestCase):

    def test_get_title(self):
        self.assertEqual(True, False)

    def test_get_content(self):
        self.assertEqual(True, False)

    def test_get_url(self):
        self.assertEqual(True, False)

    def test_get_comments(self):
        self.assertEqual(True, False)


class TestingApiConnection(unittest.TestCase):
    stack = StackOverflow.StackOverflowAPI()

    #this will just run the most basic API call to make sure we are connected to the internet
    def test_api_connection(self):
        self.assertEqual(True, False)

    def test_initialization(self):
        self.assertEqual(True, False)

    def test_search(self):
        self.assertEqual(True, False)


class TestingTraceback(unittest.TestCase):

    #create some known error so that Stack Overflow can provide a solution within our traceback.
    #no need to check any information beyond the URL to know we got what we expected.
    def basic_pandas_error(self):
        self.assertEqual(True, False)




if __name__ == '__main__':
    unittest.main()
