from tkinter import *

window=Tk()

class App:
    def __init__(self, window):
        self.window = window
        self.window.title("GUI_Python")
        self.window.geometry("410x320")

        self.window.mainloop()


# Create a window and pass it to the Application object
App(window)