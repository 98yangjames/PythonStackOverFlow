import requests
import traceback
import sys
import json
import re

#todo document the types of all of these keys
stack_data_keys = ['tags', 'comments', 'answers', 'owner', 'delete_vote_count', 'reopen_vote_count', 'close_vote_count',
                   'is_answered', 'view_count', 'favorite_count', 'accepted_answer_id', 'answer_count', 'score',
                   'last_activity_date', 'creation_date', 'last_edit_date', 'question_id', 'link', 'title', 'body']


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
            "tagged": "python",
            "filter": "!-MBrU_IzpJ5H-AG6Bbzy.X-BYQe(2v-.J"
        }
        r = requests.get(url, params=params)
        self.meta_data = {"Status Code": r.status_code, "API URL": r.url, "HEADERS": r.headers}
        self.stack_data = list(json.loads(r.content)['items'])[0]


    # gets the title to the post searched
    def get_title(self):
        return self.stack_data['title']

    #gets the content written by the author of the post, usually describing the problem they are facing.
    def get_question(self):
        return self.stack_data["body"]

    #returns the URL of the stack overflow post searched
    def get_url(self):
        return self.stack_data['link']

    #returns all of the comments underneath the post searched.
    def get_comments(self):
        return self.stack_data["comments"][0]

    def get_answer(self):
        return self.stack_data["answers"][0]["body"]

    def _cleanhtml_(self, raw_html, cleaner=re.compile('<.*?>')):
        cleantext = re.sub(cleaner, '', raw_html)
        return cleantext



#this is an example of how our code will be used

a = 1
b = 0
try:
    c = a/b
except Exception as e:
    a = StackOverflowAPI(e) #for now this does nothing with the exception

