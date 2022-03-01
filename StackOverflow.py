import requests
import traceback
import sys
import json


stack_data_keys = ['tags', 'owner', 'is_answered', 'view_count', 'accepted_answer_id', 'answer_count', 'score',
                   'last_activity_date', 'creation_date', 'last_edit_date', 'question_id', 'content_license', 'link',
                   'title']

'''
This is a class which searches and returns information about queries to stack overflow. 
removing the need to search for things on a web browser by handling everything within the IDE


NOTE: we will probably need to extend the print_exception() method inside of python/lib/traceback.py for our project.
'''
class StackOverflowAPI():

    def __init__(self, exception):
        self.BASEURL = "https://api.stackexchange.com/2.2/"
        self.meta_data = {}
        self.stack_data = {}
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
        self.search(''.join(tb.format_exception_only()))

        #TODO ADD THE INFO NEEDED TO THE STACKTRACE AND THEN RERAISE THE EXCEPTION WITH THE INFO ATTACHED


    #calls the stackoverflow API to find posts that include a given search string, then chooses the post_chosen'th
    #post to save information and meta data on.
    # PARAMS: search_string, an string describing what is being searched on stack overflow, similar to how a user
    #                       might search stack overflow on the website.
    # PARAMS: post_chosen, a search string will most likely return more than one post, which post should be selected
    #                      is decided based on the priority that they are returned in the Stackoverflow API
    def search(self, search_string, post_chosen=0):
        print("searching")
        #todo use requests to search stack overflow API, store appropriate data in self.meta_data and self.stack_data
        url = self.BASEURL + "search"
        params = {
            "site": "stackoverflow",
            "intitle": search_string,
            "order": "desc",
            "sort": "votes",
            "tagged": "python"
        }
        r = requests.get(url, params=params)
        self.meta_data = {"Status Code": r.status_code, "API URL": r.url, "HEADERS": r.headers}
        self.stack_data = list(json.loads(r.content)['items'])[0]

        #TODO GET THIS TO WORK SO THAT WE CAN GET THE QUESTION ITSELF IN OUR STACKTRACE
        url_answers = self.BASEURL + "questions/{"+ str(self.stack_data['question_id'])+ ";}/answers"
        print(url_answers)
        r = requests.get(url_answers)
        print(r)
        #print(self.stack_data)


    # gets the title to the post searched
    def get_title(self):
        return self.stack_data['title']

    #gets the content written by the author of the post, usually describing the problem they are facing.
    def get_content(self):
        return None
        #todo get the content of the post from self.stack_data

    #returns the URL of the stack overflow post searched
    def get_url(self):
        return self.stack_data['link']

    #returns all of the comments underneath the post searched.
    def get_comments(self):
        return None
        #todo return the comments under the post via information in self.stack_data




#this is an example of how our code will be used

a = 1
b = 0
try:
    c = a/b
except Exception as e:
    a = StackOverflowAPI(e) #for now this does nothing with the exception

