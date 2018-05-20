from tkinter import *
from ViewModel import *
from PIL import ImageTk, Image

class Application(Frame):

    def onleft(self):
        self.menu.prev()
        self.updateDisplay()
    def onright(self):
        self.menu.next()
        self.updateDisplay()
    def onpush(self):
        selected = self.menu.menuItems[self.menu.selectedMenuItem]
        print("Selected: " + selected)
    def updateDisplay(self):
        img = ImageTk.BitmapImage(self.menu.generateView())
        self.panel.configure(image=img)
        self.panel.image = img
    
    def createWidgets(self):
        self.left = Button(self)
        self.left["text"] = "Left"
        self.left["command"] = self.onleft
        self.left.pack({"side": "left"})

        self.push = Button(self)
        self.push["text"] = "Push"
        self.push["command"] = self.onpush
        self.push.pack({"side": "left"})

        self.right = Button(self)
        self.right["text"] = "Right"
        self.right["command"] = self.onright
        self.right.pack({"side": "left"})

        items = ["Start", "Set Agitation", "Set Temperature"]
        self.menu = MenuViewModel(items)
        im = self.menu.generateView()
        img = ImageTk.BitmapImage(im)
        self.panel = Label(self, image = img, foreground="black")
        self.panel.photo = img
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()