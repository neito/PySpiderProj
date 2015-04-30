import BoxCreation
import httplib2
from tkinter import *
import time
import sys
import valueHolder

class LoadingWindow():
    def __init__(self):
        self.window = Tk()

        self.root = Frame(self.window, height=300,width=300)
        self.root.pack()
        self.root.pack_propagate(0)
        self.window.title('PySpider')
        self.photo = PhotoImage(file="crawlingSpider.png")
        self.label = Label(self.root, image=self.photo)
        self.label.pack()
        self.sec = 0
        self.label2 = Label(self.root, text="Working")
        self.label2.pack()

        self.timerupdate()
        self.root.mainloop()

    def timerupdate(self):
        self.sec = self.sec + 1

        if self.sec % 2 is 1:
            self.photo = PhotoImage(file="crawlingSpider.png")
            self.label2.configure(text="working   ")
        else:
            self.photo = PhotoImage(file="crawlingSpider 2.png")
            self.label2.configure(text="working...")

        self.label.configure(image=self.photo)
        self.root.after(1000, self.timerupdate)

    def runWindow(self):
        self.root.mainloop()
        time.sleep(5)
        self.root.destroy()