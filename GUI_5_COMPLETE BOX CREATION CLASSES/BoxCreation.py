import httplib2
from tkinter import *
import time
import sys
import valueHolder

class BoxCreation:

     """
     Basic window value instantiations, like the basic window itself
     """
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

     """
     Funtion that runs the function when called.
     """
     def runWindow(self):
        self.root.mainloop()

     """
     Closes the window when the ok button is clicked.
     """
     def buttonCallbackClose(self):
         exit()

     """
     Creates the close button.
     """
     def addCloseButton(self):
         self.frame3 = Frame(self.root)
         self.frame3.pack()
         closeButton = Button(self.frame3, text="Close", command=self.buttonCallbackClose())
         closeButton.pack()

     """
     Adds an image to the window. Doesn't animate.
     """
     def addPicture(self, label, pictureFileName):
         self.photo = PhotoImage(file=pictureFileName)
         label2 = Label(self.root, image=self.photo)
         label2.pack()

     """
     Adds a basic label with a simple text to the window.
     For the sake of creating consistency in appearance,
     keep all label text the same length, rounding out with
     spaces as needed.
     """
     def addLabel(self, label, labelText): ### SEEMS TO BE FIXED
         self.frame5 = Frame(self.root)
         self.frame5.pack()
         labelMake = Label(self.root, text=labelText)
         label =labelMake
         label.pack()

     """
     Adds an entry field with a label. Again, be mindful
     of the length of the label text.
     """
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


     """
     Adds a button which saves the data entered by the user
     in entry fields to an outside variable.
     SHOULD ONLY MAKE ONE OF THESE.
     """
     def addConfirmSearchButton(self, button, listOfEntryFields): ### SEEMS TO BE FIXED
         self.frame4 = Frame(self.root)
         self.frame4.pack()
         searchButton = Button(self.frame4, text="ok", command=lambda: self.buttonCallbackSearchConfirm(listOfEntryFields))
         label = Label(self.frame4, text = "")
         label.pack(side = LEFT)
         button = searchButton
         button.pack()

     """
     The function which the ok button executes when it is clicked.
     """
     def buttonCallbackSearchConfirm(self, listOfEntryFields):
         global finalUserEnteredValues
         valuesToReturn = []
         for value in listOfEntryFields:
             valuesToReturn.append(value.get())
         valueHolder.finalUserAnswers = valuesToReturn
         self.checkForEntryErrors(valueHolder.finalUserAnswers)
         self.root.quit()

     """
     Adds an extra search field to search for more data.
     """
     def addAdditionalSearchField(self, listOfEnters):

         entryBox = Entry()
         textForBox = "Additional data to search for:"
         self.addEntry(entryBox, textForBox, listOfEnters)

     """
     Adds the button which creates another search field.
     """
     def addExtraSearchFieldButton(self, button, listOfEnters):
         self.frame6 = Frame(self.root)
         self.frame6.pack()
         addExtraFieldButton = Button(self.frame6, text="Add Extra Field", command = lambda : self.addAdditionalSearchField(listOfEnters))
         label = Label(self.frame6, text = "")
         label.pack(side=LEFT)
         addExtraFieldButton.pack(side=BOTTOM)

     """
     Work in progress:
     checks if the value entered for the URL is valid.
     """
     def checkForEntryErrors(self, urlToValidate):
         for everyValue in urlToValidate:
             if everyValue is "":
                warningBoxRoot = Tk()
                warningBoxLabel = Label(warningBoxRoot, text="One of the fields was left blank. Please check entries.")
                warningBoxLabel.pack()
                warningBoxRoot.mainloop()
         try:
          h=httplib2.Http()
          resp, content=h.request(urlToValidate[-1]) # this is where the problem is occuring
         except httplib2.RelativeURIError:
          warningBoxRoot2 = Tk()
          warningBoxLabel2 = Label(warningBoxRoot2, text="URL is malformed or website does not exist.")
          warningBoxLabel2.pack()
          warningBoxRoot2.mainloop()
