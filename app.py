from tkinter import *

splashMain = Tk()

class App:
    def __init__(self, splashMain):
        self.splashMain = splashMain

        #Center splash window
        scWidth, scHeight = self.splashMain.winfo_screenwidth(), self.splashMain.winfo_screenheight()
        apWidth, apHeight = 700, 200
        reWidth, reHeight = int((scWidth-apWidth)/2), int((scHeight-apHeight)/2)
        formatStr = "{}x{}+{}+{}".format(apWidth, apHeight, reWidth, reHeight)

        self.splashMain.config(bg="#2c3643")
        self.splashMain.geometry(formatStr)
        self.splashMain.overrideredirect(True)

        splashLabel= Label(self.splashMain,
            text= "Análisis AFM",
            font= ('Times New Roman', 40),
            fg="white",
            bg="#2c3643"
        )
        splashLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.splashMain.after(2000, self.main)

        mainloop()

    def main(self):
        self.window= Tk()
        self.splashMain.destroy()
        self.window.title("Main Window")
        self.window.geometry("800x500")

        self.FrameMenu()
        self.Frame1()

    def FrameMenu(self):
        #Frame configuration
        self.frameMenu = Frame(self.window,
            bg="#2c3643"
        )
        self.frameMenu.pack(side="left", fill="y")

        #Frame widgets
        self.frameMenu_button1 = Button(self.frameMenu,
            text="Menú",
            width=5,
            fg="white",
            bg="#2c3643",
            bd=0,
            activebackground="#008fd1",
            activeforeground="white",
            command = self.openMenu
        )
        self.frameMenu_button1.pack(side="top")

        self.menuContract = False

    def openMenu(self):
        print("k mlnj")
        if self.menuContract:
            self.frameMenu_button1.config(width=5)
            self.menuContract=False
        else:
            self.frameMenu_button1.config(width=20)
            self.menuContract=True

    def Frame1(self):
        self.frame1 = Frame(self.window,
            bg="#262d34"
        )
        self.frame1.pack(side="right", fill="both", expand=True)

# Create a window and pass it to the Application object
App(splashMain)