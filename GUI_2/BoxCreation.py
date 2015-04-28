import httplib2
from tkinter import *
import time
import sys

class BoxCreation:
     # creates a basic box
     def __init__(self):
        self.window = Tk()
        self.root = Frame(self.window, height=300,width=300)
        self.root.pack()
        self.root.pack_propagate(0)
        self.frame1 = Frame(self.root)
        self.frame1.pack()
        self.label = Label(self.root, text="PySpider GUI")
        self.label.pack()

     def runWindow(self):
        self.root.mainloop()

     def addBox(self, labelForBox):
        self.frame2 = Frame(self.root)
        self.frame2.pack()
        textBox = Entry(self.frame2)
        textBox.pack(side=RIGHT)
        boxLabel = Label(self.frame2, text=labelForBox)
        boxLabel.pack(side=LEFT)

     def buttonCallbackClose(self):
         exit()

     def addCloseButton(self):
         self.frame3 = Frame(self.root)
         self.frame3.pack()
         closeButton = Button(self.frame3, text="Close", command=self.buttonCallbackClose())
         closeButton.pack()

     def buttonCallbackSearchConfirm(self):
         print()###working on current;y 4/28/2015 - 12:16 AM

     def addConfirmSearchButton(self):
         self.frame4 = Frame(self.root)
         self.frame4.pack()
         searchButton = Button(self.frame4, text="ok", command=self.buttonCallbackSearchConfirm())
         searchButton.pack()


     def addPicture(self, pictureFileName):
         self.photo = PhotoImage(file=pictureFileName)
         label2 = Label(self.root, image=self.photo)
         label2.pack()





textBoxTest=BoxCreation()
#textBoxTest.addPicture("dstogether.png")
textBoxTest.runWindow()



