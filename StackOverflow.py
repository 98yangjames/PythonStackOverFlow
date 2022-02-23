import requests

'''
This is a class which searches and returns information about queries to stack overflow. 
removing the need to search for things on a web browser by handling everything within the IDE


NOTE: we will probably need to extend the print_exception() method inside of python/lib/traceback.py for our project.
'''
class StackOverflowAPI():

    #todo, decide whether or not we want the user to specifiy a search string upon initialization of the class, or later
    # in the search method below.
    def __init__(self, exception):
        print("initializing...")
        self.meta_data = {}
        self.stack_data = {}

    #calls the stackoverflow API to find posts that include a given search string, then chooses the post_chosen'th
    #post to save information and meta data on.
    # PARAMS: search_string, an string describing what is being searched on stack overflow, similar to how a user
    #                       might search stack overflow on the website.
    # PARAMS: post_chosen, a search string will most likely return more than one post, which post should be selected
    #                      is decided based on the priority that they are returned in the Stackoverflow API
    def search(self, search_string, post_chosen=0):
        print("todo")
        #todo use requests to search stack overflow API, store appropriate data in self.meta_data and self.stack_data

    # gets the title to the post searched
    def get_title(self):
        print("todo")
        #todo get the title of the post via self.stack_data

    #gets the content written by the author of the post, usually describing the problem they are facing.
    def get_content(self):
        print("todo")
        #todo get the content of the post from self.stack_data

    #returns the URL of the stack overflow post searched
    def get_url(self):
        print("todo")
        #todo get the link via self.meta_data

    #returns all of the comments underneath the post searched.
    def get_comments(self):
        print("todo")
        #todo return the comments under the post via information in self.stack_data




#this is an example of how our code will be used

a = 1
b = 0
try:
    c = a/b
except Exception as e:
    StackOverflowAPI(e) #for now this does nothing with the exception

