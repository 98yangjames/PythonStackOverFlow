import requests
import traceback
import sys
import json
import re
import warnings
import pandas as pd


# todo document the types of all of these keys
stack_data_keys = ['tags', 'comments', 'answers', 'owner', 'delete_vote_count', 'reopen_vote_count', 'close_vote_count',
                   'is_answered', 'view_count', 'favorite_count', 'accepted_answer_id', 'answer_count', 'score',
                   'last_activity_date', 'creation_date', 'last_edit_date', 'question_id', 'link', 'title', 'body']


'''
This is a class which searches and returns information about queries to stack overflow. 
removing the need to search for things on a web browser by handling everything within the IDE

Queries StackOverflow using their API, meaning that many subsequent calls will result in 24 hour ban from queries.
'''


class StackOverflowAPI():
    def __init__(self, exception):
        self.API_URL = "https://api.stackexchange.com/2.2/"
        self.meta_data = {}
        self.stack_data = {}
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
        if(tb.exc_type == None):
            warnings.warn("Currently no exception being raised", RuntimeWarning)
            return
        self.search(''.join(tb.format_exception_only()))
        raise type(exception)("\n \033[93m ----STACK OVERFLOW INFORMATION FROM LOOKUP----\033[0m \n " +
                              "\033[93m STACK OVERFLOW LINK: \033[0m" + self.get_url() + " \033[0m \n" +
                              "\033[93m QUESTION ASKED:\033[0m \n " + self.get_question() + "\033[0m \n" +
                              "\033[93m ANSWER GIVEN: \033[0m \n" + self.get_answer() + "\033[0m \n") from exception

    # calls the stackoverflow API to find posts that include a given search string, then chooses the post_chosen'th
    # post to save information and meta data on.
    # PARAMS: search_string, an string describing what is being searched on stack overflow, similar to how a user
    #                       might search stack overflow on the website.
    # PARAMS: post_chosen, a search string will most likely return more than one post, which post should be selected
    #                      is decided based on the priority that they are returned in the Stackoverflow API
    def search(self, search_string, post_chosen=0):
        url = self.API_URL + "search"
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
        print(self.stack_data)

    # gets the title to the post searched
    def get_title(self):
        return self.stack_data['title']

    # gets the content written by the author of the post, usually describing the problem they are facing.
    def get_question(self):
        return self._cleanhtml_(self.stack_data["body"])

    # returns the URL of the stack overflow post searched as a string
    def get_url(self):
        return self.stack_data['link']

    # returns all of the comments underneath the post searched as a a list of strings
    def get_comments(self):
        comments = []
        for comment_info in self.stack_data["comments"]:
            comment = comment_info["body"]
            comments.append(self._cleanhtml_(comment))
        return comments

    def get_answer(self):
        return self._cleanhtml_(self.stack_data["answers"][0]["body"])

    # returns a dictionary of meta data about the API request including:
    # the request Status code: 200/404/ect
    # the API url hit beginning with self.API_URL
    # the headers sent with the request.
    def get_meta_data(self):
        return self.meta_data

    # removes all the HTML elements from a string, helps us clean the commments and questions which come in HTML form
    def _cleanhtml_(self, raw_html, cleaner=re.compile('<.*?>')):
        return re.sub(cleaner, '', raw_html).strip()
