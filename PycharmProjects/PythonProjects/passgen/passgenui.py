from tkinter import *


class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.master.title = "Password Generator"

        self.toolbar = Frame(root)
        self.toolbar.pack(side=TOP)

        self.charLabel = Label(self.toolbar, "How large of a password: ")
        self.userEntry = Entry(self.toolbar)
        self.genButton = Button(self.toolbar, text="Generate Password", fg='Black')
        self.saveButton = Button(self.toolbar, text="Save Password", fg='Black')

        self.charLabel.pack(side=LEFT)
        self.userEntry.pack(side=RIGHT)
        self.genButton.pack(side=LEFT)
        self.saveButton.pack(side=RIGHT)

    def ui_generate(self):
        pass

    def ui_savefile(self):
        pass

    def ui_exit(self):
        Window.destroy()

root = Tk()

GUI = Window()

root.mainloop()
