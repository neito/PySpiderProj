So far, I have it so that when the program is run, a box appears where you enter the
url to scape, the type of data to look for, and where you want to store anything you find.
If you enter a bas url, the program should catch it. You need the httplib2 library
for this to work. Also, if you leave a input blank, it should also catch it.

WHAT WORKS:
When the program is run, the enter box appears and you can enter the data. It stores
this data in a variable to be passed on to whatever search function is used in our program.
The crawling spider box should appear.

WHAT DOESN'T WORK:
The crawling spider box works if run seperately, but it fails to run properly if it is run along
with the search box. I don't quite get why this is, but I'll work on it. Also the result
box is not working yet, but I don't think this is a major concern. 

The biggest issue now is making the
boxes appear serially. To run the program, use the RunProgramFile.py, not main.py.
The names are currently pretty messy right now as a result of issues I've been having,
but I'll clear this up for the final version.