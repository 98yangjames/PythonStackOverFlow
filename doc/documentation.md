# PythonStackOverFlow Documentation
A summary of the StackExchange PythonStackOverFlow project by James Yang and Arik Shurygin

## Requirements <br>
PythonStackOverFlow doesn't require any dependencies. All imports should be built in already.
```
import requests
import traceback
import sys
import json
import re
import warnings
```
Tested on Python 3.8 env.

## Design <br>
When programming, it's a common procedure to look up an error that you are facing when you don't know what is inherently wrong with your code. It is time consuming to open up a new tab, find the right StackOverFlow page and switch back from your editor to the tab to implement that solution. StackOverFlowAPI is a solution to this problem. To make the functionality as clean as possible, we wanted the design to avoid dependencies.  <br>

Within the code, the auto-lookup will nest around the code as such:
```
If name == “__main__”:
	Try:
		#your code here
	Except(e)
		StackOverflowAPI(e)
```
The goal of this was to create a simple error display where users can access information within StackOverFlow nested in a try, except format. Currently, the getter functions can pull the following values:
``` def search(self, search_string) ``` which will input the following params into StackExchange: <br>
``` 
params = {"site": "stackoverflow", 
"intitle: search_string", 
"order": "desc", 
"sort": "votes", 
"tagged": "python", 
"filter": "!-MBrU_IzpJ5H-AG6Bbzy.X-BYQe(2v-.J"} 
```

The ```site:``` needs to reference stackoverflow. <br>
The ```title:``` is the given error in the form of a string <br>
The ```order:``` is what order the information is given. In this case, we want it to be descending because ascending gives the oldest answer rather than the newest. <br>
The ```tagged:``` is Python answers because this functionality is built for Python and not other languages. <br>
The ```filter:``` is a specific filter for StackExchange that gives the body of the answers. (https://stackapps.com/questions/4213/get-questions-with-body-and-answers) <br>

The getter functions are: <br> 
```get_title()``` which returns the title of the stack_data pulled from the search. <br>
```get_question()``` which returns the question that was asked to StackOverFlow. <br>
```get_url()``` which returns the URL of the stack overflow post searched as a string. <br>
```get_comments()``` which returns all of the comments underneath the post searched as a list of strings. <br>
```get_answer()``` which returns the answer of the question. <br>
```get_meta_data()``` which returns the dictionary of meta data about the API request including: <br>
	-The request status (200/400/404/etc) <br>
	-The API url hit beginning with self.API_URL <br>
	-The headers sent with the request. <br>
## Extensibility <br>





