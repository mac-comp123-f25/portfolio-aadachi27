# create canvas, move text around canvas using wasd and arrow keys

import tkinter as tk

class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()

        self.mainCanvas = tk.Canvas(self.mainWin)
        self.mainCanvas["bg"] = "pink"
        self.mainCanvas.grid(row = 1, column = 1)
        self.textID = self.mainCanvas.create_text(100, 100, text = "Annabelle", fill = "dark blue")

        self.mainWin.bind("w", self.move_callback)
        self.mainWin.bind("a", self.move_callback)
        self.mainWin.bind("s", self.move_callback)
        self.mainWin.bind("d", self.move_callback)
        self.mainWin.bind("<Left>", self.move_callback)
        self.mainWin.bind("<Right>", self.move_callback)
        self.mainWin.bind("<Up>", self.move_callback)
        self.mainWin.bind("<Down>", self.move_callback)

    def run(self):
        self.mainWin.mainloop()

    def move_callback(self, event):
        new_event = event.keysym
        if event.keysym == "w" or event.keysym == "Up":
            self.mainCanvas.move(self.textID, 0, -10)
        elif event.keysym == "s" or event.keysym == "Down":
            self.mainCanvas.move(self.textID, 0, 10)
        elif event.keysym == "a" or event.keysym == "Left":
            self.mainCanvas.move(self.textID, -10, 0)
        elif event.keysym == "d" or event.keysym == "Right":
            self.mainCanvas.move(self.textID, 10, 0)



myGui = BasicGui()
myGui.run()


