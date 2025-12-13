

import tkinter as tk

class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()

        self.welcomeLabel = tk.Label(self.mainWin, text = "Welcome")
        self.welcomeLabel.grid(row = 2, column = 2)

        self.quitButton = tk.Button(self.mainWin)
        self.quitButton["text"] = "Quit"
        self.quitButton.grid(row = 1, column = 1)
        self.quitButton["command"] = self.quit_callback

        self.helloButton = tk.Button(self.mainWin)
        self.helloButton["text"] = "Hello"
        self.helloButton.grid(row = 2, column = 1)
        self.helloButton["command"] = self.hello_callback

        self.goodbyeButton = tk.Button(self.mainWin)
        self.goodbyeButton["text"] = "Goodbye"
        self.goodbyeButton.grid(row = 3, column = 1)
        self.goodbyeButton["command"] = self.goodbye_callback

    def run(self):
        self.mainWin.mainloop()

    def quit_callback(self):
        self.mainWin.destroy()

    def hello_callback(self):
        self.welcomeLabel.config(text = "Hello")

    def goodbye_callback(self):
        self.welcomeLabel.config(text = "Goodbye")

myGui = BasicGui()
myGui.run()