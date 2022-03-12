import requests
import traceback
import sys
import json
import re
import warnings


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
        if tb.exc_type is None:
            warnings.warn("Currently no exception being raised", RuntimeWarning)
            return
        self.search(''.join(tb.format_exception_only()))
        raise type(exception)("\n \033[93m ----STACK OVERFLOW INFORMATION FROM LOOKUP----\033[0m \n " +
                              "\033[93m STACK OVERFLOW LINK: \033[0m" + self.get_url() + " \033[0m \n" +
                              "\033[93m QUESTION ASKED:\033[0m \n " + self.get_question() + "\033[0m \n"+
                              "\033[93m ANSWER GIVEN: \033[0m \n" + self.get_answer() + "\033[0m \n") from exception

    # calls the stackoverflow API to find posts that include a given search string, then chooses the post_chosen'th
    # post to save information and meta data on.
    # PARAMS: search_string, an string describing what is being searched on stack overflow, similar to how a user
    #                       might search stack overflow on the website.
    # PARAMS: post_chosen, a search string will most likely return more than one post, which post should be selected
    #                      is decided based on the priority that they are returned in the Stackoverflow API
    # PARAMS: tags: search tags applied to the API call, default="python" this library is designed for python
    # PARAMS: order: the order in which answers and posts are displayed, possible values: "desc" "asc"
    # PARAMS: sorting: how the answers and posts are sorted,
    #                   possible values: "activity", "votes", "creation", "relevance". Default = "votes"
    # PARAMS: site: the stackexchange site to search, default = stackoverflow
    # for more API info see: https://api.stackexchange.com/docs
    def search(self, search_string, post_chosen=0, tags="python", order="desc", sorting="votes", site="stackoverflow"):
        url = self.API_URL + "search"
        params = {
            "site": site,
            "intitle": search_string,
            "order": order,
            "sort": sorting,
            "tagged": tags,
            "filter": "!-MBrU_IzpJ5H-AG6Bbzy.X-BYQe(2v-.J"
        }
        try:
            r = requests.get(url, params=params)
        except requests.exceptions.RequestException:
            print("The attempt to request data from the StackExchange API has failed, check your internet connection.")
            return
        self.meta_data = {"Status Code": r.status_code, "API URL": r.url, "HEADERS": r.headers}
        #checking if stackexchange api actually gave us a question/answer with a link, if not, expand the search
        if "items" in json.loads(r.content).keys() and len(list(json.loads(r.content)['items'])) > 0:
            self.stack_data = list(json.loads(r.content)['items'])[post_chosen]
        else:
            #we are now expanding our search using looser parameters, this will return more general results
            url = self.API_URL + "similar"
            params = {
                "site": "stackoverflow",
                "title": search_string,
                "order": "desc",
                "sort": "votes",
                "tagged": "python",
                "filter": "!-MBrU_IzpJ5H-AG6Bbzy.X-BYQe(2v-.J"
            }
            try:
                r_similar = requests.get(url, params=params)
            except requests.exceptions.RequestException:
                print("The attempt to request data from the StackExchange API has failed")
                return
            if "items" in json.loads(r_similar.content).keys() and list(json.loads(r_similar.content)['items']):
                self.stack_data = list(json.loads(r_similar.content)['items'])[0]
            else:
                self.stack_data = {}

    # gets the title to the post searched
    def get_title(self):
        if self.stack_data:
            return self.stack_data['title']
        return ""

    # gets the content written by the author of the post, usually describing the problem they are facing.
    def get_question(self):
        if self.stack_data:
            return self._cleanhtml_(self.stack_data["body"])
        return ""

    # returns the URL of the stack overflow post searched as a string
    def get_url(self):
        if self.stack_data:
            return self.stack_data['link']
        return ""

    # returns all of the comments underneath the post searched as a a list of strings
    def get_comments(self):
        if self.stack_data:
            comments = []
            for comment_info in self.stack_data["comments"]:
                comment = comment_info["body"]
                comments.append(self._cleanhtml_(comment))
            return comments
        return []

    #returns the highest voted answer on the question searched.
    #@throws: an out of index error if index > # of answers on the post.
    def get_answer(self):
        if self.stack_data:
            return self._cleanhtml_(self.stack_data["answers"][0]["body"])
        return ""

    #returns all answers on the post in decending order of votes.
    #Returns empty array if StackOverflow API was unable to find a post for the error code.
    def get_answers(self):

        if self.stack_data:
            answers = []
            for answer_info in self.stack_data["answers"]:
                answer = answer_info["body"]
                answers.append(self._cleanhtml_(answer))
            return answers
        return []

    # returns a dictionary of meta data about the API request including:
    # the request Status code: 200/404/ect
    # the API url hit beginning with self.API_URL
    # the headers sent with the request.
    def get_meta_data(self):
        if self.meta_data:
            return self.meta_data
        return ""

    # removes all the HTML elements from a string, helps us clean the commments and questions which come in HTML form
    def _cleanhtml_(self, raw_html, cleaner=re.compile('<.*?>')):
        return re.sub(cleaner, '', raw_html).strip()

    #if this object is printed, it will simply print into the console the exact same error code it raises upon init
    def __print__(self):
        return "\n \033[93m ----STACK OVERFLOW INFORMATION FROM LOOKUP----\033[0m \n " +\
                              "\033[93m STACK OVERFLOW LINK: \033[0m" + self.get_url() + " \033[0m \n" +\
                              "\033[93m QUESTION ASKED:\033[0m \n " + self.get_question() + "\033[0m \n" +\
                              "\033[93m ANSWER GIVEN: \033[0m \n" + self.get_answer() + "\033[0m \n"