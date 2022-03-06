# PythonStackOverFlow Documentation

##Requirements <br>
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

**Design** <br>
When programming, it's a common procedure to look up an error that you are facing when y ou don't know hwat is inherently wrong with your code. It is time consuming to open up a new tab, find the right StackOverFlow page and switch back from your editor to the tab to implement that solution. StackOverFlowAPI is the solution to this problem. To make the functionality as clean as possible, we wanted the design to avoid dependencies.  <br>

Within the code, the auto-lookup will nest around the code as such:
```
If name == “__main__”:
	Try:
		#your code here
	Except(e)
		StackOverflowAPI(e)
```


**Extensibility** <br>





