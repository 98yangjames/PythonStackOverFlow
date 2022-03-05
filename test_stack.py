import unittest
import StackOverflow
import traceback
import sys
import pandas as pd
"""
This is our StackOverflowAPI testing class which does not interact with the actual API via the internet,
instead it returns dummy values.
"""

class getterTesting(StackOverflow.StackOverflowAPI):

    def __init__(self, exception):
        self.meta_data = {}  # todo fill these with our appropriate values.
        self.stack_data = {'tags': ['python'], 'comments': [{'owner': {'reputation': 330022, 'user_id': 908494, 'user_type': 'registered', 'accept_rate': 25, 'profile_image': 'https://www.gravatar.com/avatar/7e41acaa8f6a0e0f5a7c645e93add55a?s=256&d=identicon&r=PG', 'display_name': 'abarnert', 'link': 'https://stackoverflow.com/users/908494/abarnert'}, 'edited': False, 'score': 2, 'creation_date': 1429839652, 'post_id': 29836964, 'comment_id': 47801181, 'body': 'What value do you want for <code>1&#47;0</code>? For <code>0&#47;0</code>, any value at all makes some sense (because <code>x&#47;y==z</code> still implies <code>z**y==x</code>), but for anything else divided by 0, no value makes sense (unless you have an infinite integer, and define <code>infinity*0 == 0</code>).'}, {'owner': {'reputation': 3538, 'user_id': 925592, 'user_type': 'registered', 'accept_rate': 50, 'profile_image': 'https://i.stack.imgur.com/e3X1a.jpg?s=256&g=1', 'display_name': 'RufusVS', 'link': 'https://stackoverflow.com/users/925592/rufusvs'}, 'edited': False, 'score': 0, 'creation_date': 1627436557, 'post_id': 29836964, 'comment_id': 121154019, 'body': 'There is an error in your logic if you come across a situation where you are dividing by zero.'}], 'answers': [{'tags': ['python'], 'owner': {'reputation': 166347, 'user_id': 416467, 'user_type': 'registered', 'accept_rate': 100, 'profile_image': 'https://www.gravatar.com/avatar/32cad7487ccecc3740a62e797fc326dc?s=256&d=identicon&r=PG', 'display_name': 'kindall', 'link': 'https://stackoverflow.com/users/416467/kindall'}, 'is_accepted': True, 'score': 67, 'last_activity_date': 1637275638, 'last_edit_date': 1637275638, 'creation_date': 1429837608, 'answer_id': 29836987, 'question_id': 29836964, 'link': 'https://stackoverflow.com/questions/29836964/error-python-zerodivisionerror-division-by-zero/29836987#29836987', 'title': 'Error python : [ZeroDivisionError: division by zero]', 'body': "<p>Catch the error and handle it:</p>\n<pre><code>try:\n    z = x / y\nexcept ZeroDivisionError:\n    z = 0\n</code></pre>\n<p>Or check before you do the division:</p>\n<pre><code>if y == 0:\n    z = 0\nelse:\n    z = x / y\n</code></pre>\n<p>The latter can be reduced to:</p>\n<pre><code>z = 0 if y == 0 else (x / y) \n</code></pre>\n<p>Or if you're sure <code>y</code> is a number, which implies it`s truthy if nonzero:</p>\n<pre><code>z = (x / y) if y else 0\nz = y and (x / y)   # alternate version\n</code></pre>\n"}, {'tags': ['python'], 'owner': {'reputation': 1157, 'user_id': 8234870, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/aa94b5af8b4585d838685b291e550607?s=256&d=identicon&r=PG&f=1', 'display_name': 'Dev Parzival', 'link': 'https://stackoverflow.com/users/8234870/dev-parzival'}, 'is_accepted': False, 'score': 0, 'last_activity_date': 1636539630, 'creation_date': 1636539630, 'answer_id': 69911495, 'question_id': 29836964, 'link': 'https://stackoverflow.com/questions/29836964/error-python-zerodivisionerror-division-by-zero/69911495#69911495', 'title': 'Error python : [ZeroDivisionError: division by zero]', 'body': "<pre><code># we are dividing until correct data is given\nexecuted = False\nwhile not executed:\n    try:\n        a = float(input('first number --&gt; '))\n        b = float(input('second number --&gt; '))\n        z = a / b\n        print(z)\n        executed = True\n    except ArithmeticError as arithmeticError:\n        print(arithmeticError)\n    except ValueError as valueError:\n        print(valueError)\n    except Exception as exception:\n        print(exception)\n</code></pre>\n"}], 'owner': {'reputation': 9829, 'user_id': 4744765, 'user_type': 'registered', 'accept_rate': 84, 'profile_image': 'https://www.gravatar.com/avatar/197b8e8a4085b5cb60ecf4b58b566aa3?s=256&d=identicon&r=PG&f=1', 'display_name': 'markov zain', 'link': 'https://stackoverflow.com/users/4744765/markov-zain'}, 'delete_vote_count': 0, 'reopen_vote_count': 0, 'close_vote_count': 0, 'is_answered': True, 'view_count': 113396, 'favorite_count': 5, 'accepted_answer_id': 29836987, 'answer_count': 2, 'score': 23, 'last_activity_date': 1637275638, 'creation_date': 1429837466, 'last_edit_date': 1618712260, 'question_id': 29836964, 'link': 'https://stackoverflow.com/questions/29836964/error-python-zerodivisionerror-division-by-zero', 'title': 'Error python : [ZeroDivisionError: division by zero]', 'body': '<p>I faced an error when I run my program using python:\nThe error is like this:</p>\n<pre><code>ZeroDivisionError: division by zero\n</code></pre>\n<p>My program is similar to this:</p>\n<pre><code>In [55]:\n\nx = 0\ny = 0\nz = x/y\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n&lt;ipython-input-55-30b5d8268cca&gt; in &lt;module&gt;()\n      1 x = 0\n      2 y = 0\n----&gt; 3 z = x/y\n\nZeroDivisionError: division by zero\n</code></pre>\n<p>Thus, I want to ask, how to avoid that error in python. My desired output is <code>z = 0</code></p>\n'}
  # todo fill these with our appropriate values

class APITesting(StackOverflow.StackOverflowAPI):
    def __init__(self, exception):
        self.API_URL = "https://api.stackexchange.com/2.2/"
        self.meta_data = {}
        self.stack_data = {}
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
        self.search(''.join(tb.format_exception_only()))

class TestingGetters(unittest.TestCase):

    def test_get_title(self):

        a = 1
        b = 0
        try:
            a.append("0")
        except Exception as e:
            a = getterTesting(e)

            print(a.get_title())
            self.assertEqual(a.get_title(), "Error python : [ZeroDivisionError: division by zero]")

    def test_get_url(self):
        a = 1
        b = 0
        try:
            a.append("0")
        except Exception as e:
            a = getterTesting(e)
            print(a.get_url())
            self.assertEqual(a.get_url(), "https://stackoverflow.com/questions/29836964/error-python-zerodivisionerror-division-by-zero")


    def test_get_comments(self):
        a = 1
        b = 0
        try:
            a.append("0")
        except Exception as e:
            a = getterTesting(e)
            print(a.get_comments())
            answers = ['What value do you want for 1&#47;0? For 0&#47;0, any value at all makes some sense (because x&#47;y==z still implies z**y==x), but for anything else divided by 0, no value makes sense (unless you have an infinite integer, and define infinity*0 == 0).', 'There is an error in your logic if you come across a situation where you are dividing by zero.']

            self.assertEqual(a.get_comments(),
                             answers)


class TestingApiConnection(unittest.TestCase):

    #this will just run the most basic API call to make sure we are connected to the internet
    def test_api_connection(self):
        a = 1
        b = 0
        try:
            a.append("0")
        except Exception as e:
            a = APITesting(e)
            print(a.meta_data)
            self.assertEqual(a.meta_data['Status Code'], 200)

    def test_initialization(self):
        a = 1
        b = 0
        try:
            a.append("0")
        except Exception as e:
            a = APITesting(e)
            self.assertTrue(a.meta_data)
            self.assertTrue(a.stack_data)

    def test_search(self): #stack data, meta data
        self.assertEqual(True, False)


class TestingTraceback(unittest.TestCase):

    #create some known error so that Stack Overflow can provide a solution within our traceback.
    #no need to check any information beyond the URL to know we got what we expected.
    def basic_pandas_error(self):

        try:
            a = pd.read_csv("notafile.csv")
        except Exception as e:
            a = getterTesting(e)

            print(e)
            self.assertEqual(a, "FileNotFoundError: [Errno 2] No such file or directory: 'notafile.csv'")


class NullTest(unittest.TestCase):

    def test_no_input(self):#null values, try to call api with no error,
        StackOverflow.StackOverflowAPI(BaseException)
        self.assertEqual(True, True)

    def test_no_stack(self):
        StackOverflow.StackOverflowAPI("duwahduwhdoawwdjawoidjawoidafhoifafw")
        # try:
        #     raise custom_error = "fadiuwhdaisjdawdawd"

if __name__ == '__main__':
    unittest.main()


