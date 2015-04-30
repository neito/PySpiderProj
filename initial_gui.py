from tkinter import Tk, Frame, BOTH, button, style
from ttk import *
#A class that can be initiated to create an initial gui for the PySpider program.
#(May accidentially include some code from the TKinter tutorial at http://zetcode.com/gui/tkinter/introduction/)
class initial_gui(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background = "white")
		self.parent = parent
		self.createUI()
	
	def createUI():
		self.parent.title("PySpider GUI Mode")
		self.style = Style()
		self.style.theme_use("default")
		
		submit_button = Button(self, text="Submit", command = NULL)
		clear_button = Button(self, text="Clear", command = NULL)
		site_url = Entry(self, textvariable = site_url)
