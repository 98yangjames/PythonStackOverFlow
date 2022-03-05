# PythonStackOverFlow

By importing this StackOverFlowAPI class, you are able to get direct error analysis on the problem you are facing at hand without having to open up another tab and copy and paste the error.

![alt text](doc/diagram.jpg)

Example of the code:
```
try:
    a = 1
    b = 0
    c = a/b
except Exception as e:
    StackOverflowAPI(e)
```
