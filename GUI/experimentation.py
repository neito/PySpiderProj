import httplib2
from tkinter import *
import time
import main
import loadingWindow
import sys

class InitialWindow():

    userEnteredValues = []

    def __init__(self):
        self.window = Tk()
        self.root = Frame(self.window, height=300,width=300)
        self.root.pack()
        self.root.pack_propagate(0)

        #self.frameInitial = Frame()
        #self.frameInitial.pack()
        self.frame1 = Frame(self.root)
        self.frame1.pack()
        self.frame2 = Frame(self.root)
        self.frame2.pack()
        self.frame3 = Frame(self.root)
        self.frame3.pack()
        self.frame4 = Frame(self.root)
        self.frame4.pack()
        self.frame5 = Frame(self.root)
        self.frame5.pack()
        self.label = Label(self.root, text="PySpider GUI")
        self.label.pack()

        self.enter1 = Entry(self.frame1)
        self.enter1.pack(side=RIGHT)
        self.enter2 = Entry(self.frame2)
        self.enter2.pack(side=RIGHT)
        self.enter3 = Entry(self.frame3)
        self.enter3.pack(side=RIGHT)

        self.okButton = Button(self.frame5, text="OK",command=self.callback)
        self.okButton.pack(side=RIGHT)

        self.label1 = Label(self.frame1, text="Enter URL:                                  ")
        self.label1.pack(side=LEFT)
        self.label2 = Label(self.frame2, text="Enter type of data to look for:")
        self.label2.pack(side=LEFT)
        self.label3 = Label(self.frame3, text="Enter location to store data:   ")
        self.label3.pack(side=LEFT)


    def OKButtonReturn(self, term, searchTerm, whereToStore):
      global userEnteredValues
      userEnteredValues = [term, searchTerm, whereToStore]
      main.testGetUserValues = userEnteredValues
      print("the test variable ", main.testGetUserValues)


    def callback(self):
      entryBox1 = (self.enter1.get())
      entryBox2 = (self.enter2.get())
      entryBox3 = (self.enter3.get())

      try:
          h=httplib2.Http()
          resp, content=h.request(entryBox1) # this is where the problem is occuring
      except httplib2.RelativeURIError:
          warningBoxRoot2 = Tk()
          warningBoxLabel2 = Label(warningBoxRoot2, text="URL is malformed or website does not exist.")
          warningBoxLabel2.pack()
          warningBoxRoot2.mainloop()

      if entryBox1 is "" or entryBox2 is "" or entryBox3 is "":
          warningBoxRoot = Tk()
          warningBoxLabel = Label(warningBoxRoot, text="One of the fields was left blank. Please check entries.")
          warningBoxLabel.pack()
          warningBoxRoot.mainloop()

      self.OKButtonReturn(entryBox1, entryBox2, entryBox3)
      self.root.destroy()




