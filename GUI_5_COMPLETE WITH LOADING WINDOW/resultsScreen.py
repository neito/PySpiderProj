import BoxCreation
import httplib2
from tkinter import *
import time
import sys
import valueHolder

class ResultsWindow():
    def __init__(self):
        self.window = Tk()

        self.root = Frame(self.window, height=300,width=300)
        self.root.pack()

        self.label = Label(self.root, text="")

        self.root.mainloop()

app = ResultsWindow()