import BoxCreation
import httplib2
from tkinter import *
import time
import sys
import valueHolder
import loadingScreen


"""
Here's a sample GUI that seems to have the spacing issues sorted out. When building the boxes,
it is VERY IMPORTANT that the url box is created first, as the manner in which data entries are checked
is based on this box's entries being placed in the list first.
"""

textBoxTest=BoxCreation.BoxCreation()
listOfEntries = []

e = Entry()
textBoxTest.addEntry(e, "Enter URL:                               ", listOfEntries)

e2 = Entry()
textBoxTest.addEntry(e2, "Enter data to search for:       ", listOfEntries)

e3 = Entry()
textBoxTest.addEntry(e3, "Enter location to store data:", listOfEntries)

b = Button()
textBoxTest.addConfirmSearchButton(b, listOfEntries)

addExtraFieldB = Button()
textBoxTest.addExtraSearchFieldButton(addExtraFieldB, listOfEntries) #added this second parameter

textBoxTest.runWindow()

"""
Use the variable from the valueHolder class to access user entered data.
"""

print("THE VALUE HOLDER ", valueHolder.finalUserAnswers)

runLoadingWindow = loadingScreen.LoadingWindow()
