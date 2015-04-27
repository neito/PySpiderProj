from tkinter import *
import time

class ResultsWindow():
    def __init__(self):
        self.window = Tk()

        self.root = Frame(self.window, height=500,width=500)
        self.root.pack()
        self.root.pack_propagate(0)
        self.window.title('PySpider')

        self.root.mainloop()

    def runWindow(self):
        ResultsWindow()
        time.sleep(5)
        self.root.quit()
