# GUI to reverse and display inputted string

import tkinter as tk

class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()

        self.instructionLabel = tk.Label(self.mainWin, text = "Type in a phrase and hit return to reverse it")
        self.instructionLabel.grid(row = 1, column = 1)

        self.entryWidget = tk.Entry(self.mainWin)
        self.entryWidget.grid(row = 2, column = 1)
        self.entryWidget.bind("<Return>", self.entry_response)

        self.reverseLabel = tk.Label(self.mainWin, text = "")
        self.reverseLabel.grid(row = 3, column = 1)

    def run(self):
        self.mainWin.mainloop()

    def entry_response(self, event):
        text = self.entryWidget.get()
        reverse_text = text[::-1]
        self.reverseLabel.config(text = reverse_text)


myGui = BasicGui()
myGui.run()