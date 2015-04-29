import httplib2
from tkinter import *
import time
import sys
import valueHolder

class BoxCreation:
     indexForEntryListInsertion = 0
     finalUserEnteredValues = []
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

     def buttonCallbackClose(self):
         exit()

     def addCloseButton(self):
         self.frame3 = Frame(self.root)
         self.frame3.pack()
         closeButton = Button(self.frame3, text="Close", command=self.buttonCallbackClose())
         closeButton.pack()

     def addPicture(self, label, pictureFileName):
         self.photo = PhotoImage(file=pictureFileName)
         label2 = Label(self.root, image=self.photo)
         label2.pack()

     def addLabel(self, label, labelText): ### SEEMS TO BE FIXED
         self.frame5 = Frame(self.root)
         self.frame5.pack()
         labelMake = Label(self.root, text=labelText)
         label =labelMake
         label.pack()

     def addEntry(self, entryBox, labelForBox, listOfEnters): ### SEEMS TO BE FIXED
        global indexForEntryListInsertion
        indexForEntryListInsertion = 0

        self.frame2 = Frame(self.root)
        self.frame2.pack()
        textBox = Entry(self.frame2)
        entryBox = textBox

        listOfEnters.insert(indexForEntryListInsertion, textBox)
        indexForEntryListInsertion = indexForEntryListInsertion + 1

        entryBox.pack(side=RIGHT)
        boxLabel = Label(self.frame2, text=labelForBox)
        boxLabel.pack(side=LEFT)


     def addConfirmSearchButton(self, button, listOfEntryFields): ### SEEMS TO BE FIXED
         self.frame4 = Frame(self.root)
         self.frame4.pack()
         searchButton = Button(self.frame4, text="ok", command=lambda: self.buttonCallbackSearchConfirm(listOfEntryFields))
         label = Label(self.frame4, text = "")
         label.pack(side = LEFT)
         button = searchButton
         button.pack()

     def buttonCallbackSearchConfirm(self, listOfEntryFields):
         global finalUserEnteredValues
         valuesToReturn = []
         for value in listOfEntryFields:
             valuesToReturn.append(value.get())
         valueHolder.finalUserAnswers = valuesToReturn
         self.root.quit()

     def addExtraSearchFieldButton(self, button):
         self.frame6 = Frame(self.root)
         self.frame6.pack()
         addExtraFieldButton = Button(self.frame6, text="Add Extra Field")
         label = Label(self.frame6, text = "")
         label.pack(side=LEFT)
         addExtraFieldButton.pack(side=BOTTOM)


textBoxTest=BoxCreation()
listOfEntries = []

e = Entry()
textBoxTest.addEntry(e, "Enter URL:                   ", listOfEntries)

e2 = Entry()
textBoxTest.addEntry(e2, "Enter data to search for:    ", listOfEntries)

e3 = Entry()
textBoxTest.addEntry(e3, "Enter location to store data:", listOfEntries)

b = Button()
textBoxTest.addConfirmSearchButton(b, listOfEntries)

addExtraFieldB = Button()
textBoxTest.addExtraSearchFieldButton(addExtraFieldB)

textBoxTest.runWindow()

print("THE VALUE HOLDER ", valueHolder.finalUserAnswers)