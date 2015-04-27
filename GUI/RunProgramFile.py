import httplib2
from tkinter import *
import time
import loadingWindow
import experimentation
import ResultsScreen



runInitialWindow = experimentation.InitialWindow().root.mainloop()
newLoadingWindow = loadingWindow.LoadingWindow()
newLoadingWindow.runWindow()
#ResultsScreen.ResultsWindow()