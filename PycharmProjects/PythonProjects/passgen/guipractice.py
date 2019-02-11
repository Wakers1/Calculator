from tkinter import *


class GUI(Frame):
    def __init__(self, master):
        frame = Frame(master, width=300, height=300)
        frame.pack()
        self.master = master
        self.master.title("Password Generator")
        #Frame.__init__(self, master)

        self.master = master
        self.charLabel = Label(root, "How large of a password: ")
        self.userEntry = Entry(root)
        self.genButton = Button(root, text="Generate Password", fg='Black')
        self.saveButton = Button(root, text="Save Password", fg='Black')

        self.charLabel.pack(side=LEFT)
        self.userEntry.pack(side=RIGHT)
        self.genButton.pack(side=LEFT)
        self.saveButton.pack(side=RIGHT)

root = Tk()

app = GUI(root)

root.mainloop()
#
# topmenu = Menu(root)
# # edit_menu options
#
# # file_menu options
# file_menu = Menu(topmenu, tearoff=False)
# file_menu.add_command(label="New Password", command=self.client_generate)
# # file_menu.add_command(label="Exit", command=self.client_exit)
#
# edit_menu = Menu(topmenu, tearoff=False)
# edit_menu.add_command(label="Edit")
#
# # view_menu options
# view_menu = Menu(topmenu, tearoff=False)
# view_menu.add_command(label="View")
#
# # tools_menu options
# tools_menu = Menu(topmenu, tearoff=False)
# tools_menu.add_command(label="Tools")
#
# topmenu.add_cascade(label="File", menu=file_menu)
# topmenu.add_cascade(label="Edit", menu=edit_menu)
# topmenu.add_cascade(label="View", menu=view_menu)
# topmenu.add_cascade(label="Tools", menu=tools_menu)