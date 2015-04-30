import BoxCreation
import httplib2
from tkinter import *
import time
import sys
import valueHolder

class LoadingWindow():
    def __init__(self):
        self.sec = 0

        self.window = Tk()
        self.window.title('PySpider Working')

        self.imgFrame = Frame(self.window)
        self.imgFrame.pack(side=BOTTOM)

        self.textFrame = Frame(self.window)
        self.textFrame.pack(side=BOTTOM)

        #self.imgFrame.pack_propagate(0)

        self.photo = PhotoImage(file="crawlingSpider.png")

        self.label = Label(self.imgFrame, image=self.photo)
        self.label.pack()

        self.label2 = Label(self.textFrame, text="Working")
        self.label2.pack()

        self.timerUpdate()
        self.window.mainloop()

    def timerUpdate(self):
        self.sec += 1

        if self.sec % 2 is 1:
            self.photo = PhotoImage(file="crawlingSpider.png")
            self.label2.configure(text="Working   ")
        else:
            self.photo = PhotoImage(file="crawlingSpider_2.png")
            self.label2.configure(text="Working...")

        self.label.configure(image=self.photo)
        self.imgFrame.after(500, self.timerUpdate)

    def runWindow(self):
        self.imgFrame.mainloop()
        time.sleep(5)
        self.imgFrame.destroy()

# window = LoadingWindow() # display window
